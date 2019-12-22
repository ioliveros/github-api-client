""" 
    settings
    ~~~~~~~~

    ref: https://developer.github.com/v3/

"""
import os

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10


GITHUB_BASE_API = 'https://api.github.com'
GITHUB_SETTINGS = {
    'GITHUB_SUPPORTED_RESOURCES': (
        'issues', 'commits', 'pull_requests'
    ),    
    'GITHUB_USER_API':'{base}/users'.format(
        base=GITHUB_BASE_API
    ),
    'GITHUB_USER_REPO_API': '{base}/{{user}}/repos'.format(
        base=GITHUB_BASE_API
    ),
    'GITHUB_USER_REPO_COMMITS_API': '{base}/{{user}}/{{repo}}/commits'.format(
        base=GITHUB_BASE_API
    ),
    'GITHUB_USER_REPO_ISSUES_API': '{base}/{{user}}/{{repo}}/issues'.format(
        base=GITHUB_BASE_API
    ),
    'GITHUB_USER_REPO_PULL_REQUESTS_API': '{base}/{{user}}/{{repo}}/pulls'.format(
        base=GITHUB_BASE_API
    )
}