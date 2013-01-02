# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest

# import Ezhuthu class
try:
    from learntamil.apps.amuthaa.lib.Ezhuthu import Ezhuthu
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    from Ezhuthu import Ezhuthu

vowels        = [u'அ', u'ஆ', u'இ', u'ஈ', 
                 u'உ', u'ஊ', u'எ', u'ஏ', 
                 u'ஐ',u'ஒ', u'ஓ', u'ஔ']

consonants    = [u'க்', u'ங்', u'ச்', u'ஞ்', 
                 u'த்', u'ந்', u'ப்', u'ம்', 
                 u'ய்',u'ர்', u'ல்', u'வ்',
                 u'ழ்', u'ள்', u'ற்', u'ன்']



class EzhuthuTest(unittest.TestCase):
    """
    A test class for the Ezhuthu module
    """
    
    def setUp(self):
        self.letter = Ezhuthu()
    
    def tearDown(self):
        self.letter.dispose()
        self.letter = None
    
    def test_is_vowel(self):
        self.letter = Ezhuthu(u'அ')
        self.failIf(self.letter.is_vowel())
        
        self.letter = Ezhuthu(u'ஆ')
        self.failUnless(self.letter.is_vowel())
        

    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(EzhuthuTest))
    return suite
    
def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)
        

if __name__ == '__main__':
    main()
