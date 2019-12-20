import unittest

from .github import Github

class TestGetRepo(unittest.TestCase):
    def test_get_repo_001(self):

        gh = Github(owner='ioliveros')
        print(gh.repo_list)



if __name__ == '__main__':
    unittest.main()