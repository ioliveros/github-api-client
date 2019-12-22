"""
    app
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

        self.current_repo = None
        self.owner = kwargs['owner']

        self.page = kwargs.get('page', settings.DEFAULT_PAGE)
        self.per_page = kwargs.get('per_page', settings.DEFAULT_PER_PAGE)                
        print('==> ', settings.GITHUB_SETTINGS['GITHUB_USER_REPO_API'])
        self.repo_list = kwargs['repositories'] if kwargs.get('repositories', None) else \
            self.get_list(api_endpoint=settings.GITHUB_SETTINGS['GITHUB_USER_REPO_API'], **kwargs)
        
        self.repo_done = []

    def get_list(self, *args, **kwargs):
        """reusable helper to get list of information from Github API

            :user/:repo
            :user/:repo/commits
            :user/:repo/issues
            :user/:repo/pulls
        """
        print('{api_endpoint}'.format(**kwargs))
        response = requests.get('{api_endpoint}'.format(**kwargs),
            headers={'User-Agent':'Google-Bot'},
            params={
                'page':self.page,
                'per_page':self.per_page                
            }
        )        
        #if response.json:
        #    yield            
        return response.json

    def builder(self, *args, **kwargs):
        """this will build data-structure for the Github Class, will depend on the ff:
           
           user/org:
            repo:
                [commits, issues, pulls]        
            ...
        """
        for _ in self.repo_list:
            print(_)
            

    def read(self, *args, **kwargs):
        """will request data to github api"""     
        return 'OK'