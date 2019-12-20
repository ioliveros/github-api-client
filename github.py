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
        
        self.page = kwargs.get('page', settings.DEFAULT_PAGE)
        self.per_page = kwargs.get('per_page', settings.DEFAULT_PER_PAGE)        

        self.repo_list = self.get_list(user=kwargs['owner'], 
            api_endpoint=settings.GITHUB_SETTINGS['GITHUB_USER_REPO_API']) /
            if not kwargs.get('repositories', None) else kwargs['repositories'])
        
        self.repo_done = []

    def get_list(self, *args, **kwargs):
        """reusable helper to get list of information from Github API

            :user/:repo
            :user/:repo/commits
            :user/:repo/issues
            :user/:repo/pulls
        """
        response = requests.get('{api_endpoint}'.format(**kwargs),
            headers={'User-Agent':'Google-Bot'},
            params={
                'page':self.current_page,
                'per_page':self.page_limit                
            }
        )
        if response.json:
            yield            

    def builder(self, *args, **kwargs):
        """this will build data-structure for the Github Class, will depend on the ff:
           
           user/org:
            repo:
                [commits, issues, pulls]        
            ...
        """
        for _ in self.repo_list:


    def read(self, *args, **kwargs):
        """will request data to github api"""     
        return 'OK'