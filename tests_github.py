import unittest

from github import Github

class TestGithub(unittest.TestCase):
    
    def test_get_repo_001(self):
        """test get all repo list"""
        gh = Github(owner='ioliveros')        
        for a in gh.repo_list:            
            self.assertIsNotNone(a)

    def test_get_repo_002(self):
        """test gosuapi repo if equal"""
        gh = Github(owner='ioliveros', repositories=['gosuapi'])        
        for a in gh.repo_list:       
            self.assertEqual(a, 'gosuapi')     
            
    def test_get_commits_003(self):
        """test gosuapi repo get commits"""
        gh = Github(owner='ioliveros', repositories=['gosuapi'], resources=['commits'])        
        r = gh.read()                
        self.assertIsNotNone(r['resource']['commits'])
    
    def test_get_pulls_004(self):
        """test ejabberd repo get pulls"""
        gh = Github(owner='processone', repositories=['ejabberd'], resources=['pulls'])        
        r = gh.read()        
        self.assertIsNotNone(r['resource']['pulls'])

    def test_get_issues_005(self):
        """test ejabberd repo get issues"""
        gh = Github(owner='processone', repositories=['ejabberd'], resources=['issues'])        
        r = gh.read()        
        self.assertIsNotNone(r['resource']['issues'])        

    def test_get_issues_006(self):
        """test ejabberd repo get commits, pulls, issues,"""
        gh = Github(owner='processone', repositories=['ejabberd'], resources=['commits', 'pulls', 'issues'])        
        r = gh.read()        
        self.assertIsNotNone(r['resource']['commits'])        
        self.assertIsNotNone(r['resource']['pulls'])        
        self.assertIsNotNone(r['resource']['issues'])       

    def test_get_issues_007(self):
        """test ejabberd repo get default resources"""
        gh = Github(owner='processone', repositories=['ejabberd'])        
        r = gh.read()        
        self.assertIsNotNone(r['resource']['commits'])        
        self.assertIsNotNone(r['resource']['pulls'])        
        self.assertIsNotNone(r['resource']['issues'])   


if __name__ == '__main__':
    unittest.main()