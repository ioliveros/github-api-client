"""
    github
    ~~~~~~~~~

    This module serves as base class for GitHub API integration

    @author: Ian Oliveros <ioliveros.dev@gmail.com>
    @date: December 2019
"""
import requests
import settings


class Github(object):

    def __init__(self, *args, **kwargs):
        """initialize github-api parameter variables"""
        
        self.current_result = dict()

        self.owner = kwargs['owner']
        self.resources = kwargs.get('resources', 
            settings.GITHUB_SETTINGS['GITHUB_SUPPORTED_RESOURCES']
        )

        self.page = kwargs.get('page', settings.DEFAULT_PAGE)
        self.per_page = kwargs.get('per_page', settings.DEFAULT_PER_PAGE)                
        
        self.repo_list = self._get_repo_list(**kwargs)

        self.repo_done = []
        self.current_repo = None        


    def get_list(self, *args, **kwargs):
        """reusable helper to get list of information from Github API
        eg.
            users/:user/repos
            :user/:repo/commits
            :user/:repo/issues
            :user/:repo/pulls
        """            
        response = requests.get('{api_endpoint}'.format(**kwargs),
            headers={'User-Agent':'Google-Bot'},
            params={
                'page':kwargs.get('page', self.page),
                'per_page':kwargs.get('per_page', self.per_page)
            }
        )          
        return response.json()   

    def _get_repo_list(self, *args, **kwargs):
        """this will get repo-list"""                
        repo_list = kwargs['repositories'] if kwargs.get('repositories', None) else self.get_list(
            api_endpoint=settings.GITHUB_SETTINGS['GITHUB_USER_REPO_API'].format(**kwargs)
        )
        for r in repo_list:
            if isinstance(r, dict):
                yield r['name']
            else:
                 yield r

    def _get_resource(self, *args, **kwargs):
        """this will get reosource [GITHUB_SUPPORTED_RESOURCES]"""
        r = []
        if kwargs['resource'] in self.resources:
            r = self.get_list(
                api_endpoint=settings.GITHUB_SETTINGS['GITHUB_USER_REPO_API'].format(**kwargs)
            )
        else:
            ValueError("{resource} - Resource Not Supported".format(**kwargs))        
        return r

    def build_resource(self, *args, **kwargs):
        """build github data per resource"""
        r = {}
        for current_resource in self.resources:
            item = self._get_resource(
                repo=self.current_repo, owner=self.owner, 
                resource=current_resource, **kwargs
            )
            if not item: continue
            r[current_resource] = item

        return r

    def read(self, *args, **kwargs):
        """will request data to github api"""

        if not self.current_repo:
            # get the first available repository
            self.current_repo = next(self.repo_list)

        if self.current_repo in self.repo_done:
            try:
                # get the next available repository
                self.current_repo = next(self.repo_list)
                # call self to get the next iteration            
                self.read()                      
            except StopIteration:
                raise("repository exhausted")

        else:
            # iterate to get all data until (GITHUB_SUPPORTED_RESOURCES is exhausted)
            resource = self.build_resource(page=self.page, per_page=self.per_page)
            if resource:                                            
                if self.current_result.get(self.current_repo, None):
                    self.current_result['owner'] = self.owner
                    self.current_result['repo'] = self.current_repo
                    self.current_result['resource'] = resource                
                else:                                                         
                    self.current_result['resource'] = resource                
                self.current_result['page'] = self.page
                self.current_result['per_page'] = self.per_page    
                
                # increment pagination
                self.page += settings.DEFAULT_PAGE
                self.per_page += settings.DEFAULT_PER_PAGE
            else:
                self.repo_done.append(self.current_repo)
                # reset pagination
                self.page = settings.DEFAULT_PAGE
                self.per_page = settings.DEFAULT_PER_PAGE
                          
        return self.current_result