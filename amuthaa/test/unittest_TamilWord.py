# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest

# import TamilLetter and TamilWord classes
from amuthaa.TamilLetter import TamilLetter
from amuthaa.TamilWord import TamilWord
    

class CholTest(unittest.TestCase):
    """ A test class for the TamilWord module """
    
    def setUp(self):
        #TODO: add setup
        pass
    
    def tearDown(self):
        #TODO: Add tear-down
        pass
    
    def testSomething(self):
        """docstring"""
        
        #TODO: implement this
        

    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CholTest))
    return suite
    
def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)
        

if __name__ == '__main__':
    main()