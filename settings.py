""" 
    settings
    ~~~~~~~~

    ref: https://developer.github.com/v3/

    eg.
        https://api.github.com/repos/processone/ejabberd/issues

"""

DEFAULT_PAGE = 1
DEFAULT_PER_PAGE = 10


GITHUB_BASE_API = 'https://api.github.com'
GITHUB_SETTINGS = {
    'GITHUB_SUPPORTED_RESOURCES': (
        'issues', 'commits', 'pulls'
    ),        
    'GITHUB_USER_REPO_API': '{base}/users/{{owner}}/repos'.format(
        base=GITHUB_BASE_API
    ),
    'GITHUB_RESOURCE_API': '{base}/repos/{{owner}}/{{repo}}/{{resource}}'.format(
        base=GITHUB_BASE_API
    )
}