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

# a tuple dictionary that matches a consonant, vowel tuple to its combination
COMBINATIONS = {
                (u'க்', u'அ') : u'க', (u'க்', u'ஆ') : u'கா', (u'க்', u'இ') : u'கி', 
                (u'க்', u'ஈ') : u'கீ', (u'க்', u'உ') : u'கு', (u'க்', u'ஊ') : u'கூ', 
                (u'க்', u'எ') : u'கெ', (u'க்', u'ஏ') : u'கே', (u'க்', u'ஐ') : u'கை', 
                (u'க்', u'ஒ') : u'கொ', (u'க்', u'ஓ') : u'கோ', (u'க்', u'ஔ') : u'கௌ', 
                
                (u'ங்', u'அ') : u'ங', (u'ங்', u'ஆ') : u'ஙா', (u'ங்', u'இ') : u'ஙி', 
                (u'ங்', u'ஈ') : u'ஙீ', (u'ங்', u'உ') : u'ஙு', (u'ங்', u'ஊ') : u'ஙூ', 
                (u'ங்', u'எ') : u'ஙெ', (u'ங்', u'ஏ') : u'ஙே', (u'ங்', u'ஐ') : u'ஙை', 
                (u'ங்', u'ஒ') : u'ஙொ', (u'ங்', u'ஓ') : u'ஙோ', (u'ங்', u'ஔ') : u'ஙௌ', 
                
                (u'ச்', u'அ') : u'ச', (u'ச்', u'ஆ') : u'சா', (u'ச்', u'இ') : u'சி', 
                (u'ச்', u'ஈ') : u'சீ', (u'ச்', u'உ') : u'சு', (u'ச்', u'ஊ') : u'சூ', 
                (u'ச்', u'எ') : u'செ', (u'ச்', u'ஏ') : u'சே', (u'ச்', u'ஐ') : u'சை', 
                (u'ச்', u'ஒ') : u'சொ', (u'ச்', u'ஓ') : u'சோ', (u'ஞ்', u'ஔ') : u'சௌ', 
                
                (u'ஞ்', u'அ') : u'ஞ', (u'ஞ்', u'ஆ') : u'ஞா', (u'ஞ்', u'இ') : u'ஞி', 
                (u'ஞ்', u'ஈ') : u'ஞீ', (u'ஞ்', u'உ') : u'ஞு', (u'ஞ்', u'ஊ') : u'ஞூ', 
                (u'ஞ்', u'எ') : u'ஞெ', (u'ஞ்', u'ஏ') : u'ஞே', (u'ஞ்', u'ஐ') : u'ஞை', 
                (u'ஞ்', u'ஒ') : u'ஞொ', (u'ஞ்', u'ஓ') : u'ஞோ', (u'ட்', u'ஔ') : u'ஞௌ', 
                
                (u'ட்', u'அ') : u'ட', (u'ட்', u'ஆ') : u'டா', (u'ட்', u'இ') : u'டி', 
                (u'ட்', u'ஈ') : u'டீ', (u'ட்', u'உ') : u'டு', (u'ட்', u'ஊ') : u'டூ', 
                (u'ட்', u'எ') : u'டெ', (u'ட்', u'ஏ') : u'டே', (u'ட்', u'ஐ') : u'டை', 
                (u'ட்', u'ஒ') : u'டொ', (u'ட்', u'ஓ') : u'டோ', (u'ண்', u'ஔ') : u'டௌ', 
                
                (u'ண்', u'அ') : u'ண', (u'ண்', u'ஆ') : u'ணா', (u'ண்', u'இ') : u'ணி', 
                (u'ண்', u'ஈ') : u'ணீ', (u'ண்', u'உ') : u'ணு', (u'ண்', u'ஊ') : u'ணூ', 
                (u'ண்', u'எ') : u'ணெ', (u'ண்', u'ஏ') : u'ணே', (u'ண்', u'ஐ') : u'ணை', 
                (u'ண்', u'ஒ') : u'ணொ', (u'ண்', u'ஓ') : u'ணோ', (u'ண்', u'ஔ') : u'ணௌ', 
                
                (u'த்', u'அ') : u'த', (u'த்', u'ஆ') : u'தா', (u'த்', u'இ') : u'தி', 
                (u'த்', u'ஈ') : u'தீ', (u'த்', u'உ') : u'து', (u'த்', u'ஊ') : u'தூ', 
                (u'த்', u'எ') : u'தெ', (u'த்', u'ஏ') : u'தே', (u'த்', u'ஐ') : u'தை', 
                (u'த்', u'ஒ') : u'தொ', (u'த்', u'ஓ') : u'தோ', (u'த்', u'ஔ') : u'தௌ', 
                
                (u'ந்', u'அ') : u'ந', (u'ந்', u'ஆ') : u'நா', (u'ந்', u'இ') : u'நி', 
                (u'ந்', u'ஈ') : u'நீ', (u'ந்', u'உ') : u'நு', (u'ந்', u'ஊ') : u'நூ', 
                (u'ந்', u'எ') : u'நெ', (u'ந்', u'ஏ') : u'நே', (u'ந்', u'ஐ') : u'நை', 
                (u'ந்', u'ஒ') : u'நொ', (u'ந்', u'ஓ') : u'நோ', (u'ந்', u'ஔ') : u'நௌ', 
                
                (u'ப்', u'அ') : u'ப', (u'ப்', u'ஆ') : u'பா', (u'ப்', u'இ') : u'பி', 
                (u'ப்', u'ஈ') : u'பீ', (u'ப்', u'உ') : u'பு', (u'ப்', u'ஊ') : u'பூ', 
                (u'ப்', u'எ') : u'பெ', (u'ப்', u'ஏ') : u'பே', (u'ப்', u'ஐ') : u'பை', 
                (u'ப்', u'ஒ') : u'பொ', (u'ப்', u'ஓ') : u'போ', (u'ப்', u'ஔ') : u'பௌ', 
                
                (u'ம்', u'அ') : u'ம', (u'ம்', u'ஆ') : u'மா', (u'ம்', u'இ') : u'மி', 
                (u'ம்', u'ஈ') : u'மீ', (u'ம்', u'உ') : u'மு', (u'ம்', u'ஊ') : u'மூ', 
                (u'ம்', u'எ') : u'மெ', (u'ம்', u'ஏ') : u'மே', (u'ம்', u'ஐ') : u'மை', 
                (u'ம்', u'ஒ') : u'மொ', (u'ம்', u'ஓ') : u'மோ', (u'ம்', u'ஔ') : u'மௌ', 
                
                (u'ய்', u'அ') : u'ய', (u'ய்', u'ஆ') : u'யா', (u'ய்', u'இ') : u'யி', 
                (u'ய்', u'ஈ') : u'யீ', (u'ய்', u'உ') : u'யு', (u'ய்', u'ஊ') : u'யூ', 
                (u'ய்', u'எ') : u'யெ', (u'ய்', u'ஏ') : u'யே', (u'ய்', u'ஐ') : u'யை', 
                (u'ய்', u'ஒ') : u'யொ', (u'ய்', u'ஓ') : u'யோ', (u'ய்', u'ஔ') : u'யௌ', 
                
                (u'ர்', u'அ') : u'ர', (u'ர்', u'ஆ') : u'ரா', (u'ர்', u'இ') : u'ரி', 
                (u'ர்', u'ஈ') : u'ரீ', (u'ர்', u'உ') : u'ரு', (u'ர்', u'ஊ') : u'ரூ', 
                (u'ர்', u'எ') : u'ரெ', (u'ர்', u'ஏ') : u'ரே', (u'ர்', u'ஐ') : u'ரை', 
                (u'ர்', u'ஒ') : u'ரொ', (u'ர்', u'ஓ') : u'ரோ', (u'ர்', u'ஔ') : u'ரௌ', 
                
                (u'ல்', u'அ') : u'ல', (u'ல்', u'ஆ') : u'லா', (u'ல்', u'இ') : u'லி', 
                (u'ல்', u'ஈ') : u'லீ', (u'ல்', u'உ') : u'லு', (u'ல்', u'ஊ') : u'லூ', 
                (u'ல்', u'எ') : u'லெ', (u'ல்', u'ஏ') : u'லே', (u'ல்', u'ஐ') : u'லை', 
                (u'ல்', u'ஒ') : u'லொ', (u'ல்', u'ஓ') : u'லோ', (u'ல்', u'ஔ') : u'லௌ', 
                
                (u'வ்', u'அ') : u'வ', (u'வ்', u'ஆ') : u'வா', (u'வ்', u'இ') : u'வி', 
                (u'வ்', u'ஈ') : u'வீ', (u'வ்', u'உ') : u'வு', (u'வ்', u'ஊ') : u'வூ', 
                (u'வ்', u'எ') : u'வெ', (u'வ்', u'ஏ') : u'வே', (u'வ்', u'ஐ') : u'வை', 
                (u'வ்', u'ஒ') : u'வொ', (u'வ்', u'ஓ') : u'வோ', (u'வ்', u'ஔ') : u'வௌ', 
                
                (u'ழ்', u'அ') : u'ழ', (u'ழ்', u'ஆ') : u'ழா', (u'ழ்', u'இ') : u'ழி', 
                (u'ழ்', u'ஈ') : u'ழீ', (u'ழ்', u'உ') : u'ழு', (u'ழ்', u'ஊ') : u'ழூ', 
                (u'ழ்', u'எ') : u'ழெ', (u'ழ்', u'ஏ') : u'ழே', (u'ழ்', u'ஐ') : u'ழை', 
                (u'ழ்', u'ஒ') : u'ழொ', (u'ழ்', u'ஓ') : u'ழோ', (u'ழ்', u'ஔ') : u'ழௌ', 
                
                (u'ள்', u'அ') : u'ள', (u'ள்', u'ஆ') : u'ளா', (u'ள்', u'இ') : u'ளி', 
                (u'ள்', u'ஈ') : u'ளீ', (u'ள்', u'உ') : u'ளு', (u'ள்', u'ஊ') : u'ளூ', 
                (u'ள்', u'எ') : u'ளெ', (u'ள்', u'ஏ') : u'ளே', (u'ள்', u'ஐ') : u'ளை', 
                (u'ள்', u'ஒ') : u'ளொ', (u'ள்', u'ஓ') : u'ளோ', (u'ள்', u'ஔ') : u'ளௌ', 
                
                (u'ற்', u'அ') : u'ற', (u'ற்', u'ஆ') : u'றா', (u'ற்', u'இ') : u'றி', 
                (u'ற்', u'ஈ') : u'றீ', (u'ற்', u'உ') : u'று', (u'ற்', u'ஊ') : u'றூ', 
                (u'ற்', u'எ') : u'றெ', (u'ற்', u'ஏ') : u'றே', (u'ற்', u'ஐ') : u'றை', 
                (u'ற்', u'ஒ') : u'றொ', (u'ற்', u'ஓ') : u'றோ', (u'ற்', u'ஔ') : u'றௌ', 
                
                (u'ன்', u'அ') : u'ன', (u'ன்', u'ஆ') : u'னா', (u'ன்', u'இ') : u'னி', 
                (u'ன்', u'ஈ') : u'னீ', (u'ன்', u'உ') : u'னு', (u'ன்', u'ஊ') : u'னூ', 
                (u'ன்', u'எ') : u'னெ', (u'ன்', u'ஏ') : u'னே', (u'ன்', u'ஐ') : u'னை', 
                (u'ன்', u'ஒ') : u'னொ', (u'ன்', u'ஓ') : u'னோ', (u'ஶ்', u'ஔ') : u'னௌ', 
                
                (u'ஜ்', u'அ') : u'ஜ', (u'ஜ்', u'ஆ') : u'ஜா', (u'ஜ்', u'இ') : u'ஜி', 
                (u'ஜ்', u'ஈ') : u'ஜீ', (u'ஜ்', u'உ') : u'ஜு', (u'ஜ்', u'ஊ') : u'ஜூ', 
                (u'ஜ்', u'எ') : u'ஜெ', (u'ஜ்', u'ஏ') : u'ஜே', (u'ஜ்', u'ஐ') : u'ஜை', 
                (u'ஜ்', u'ஒ') : u'ஜொ', (u'ஜ்', u'ஓ') : u'ஜோ', (u'ஜ்', u'ஔ') : u'ஜௌ', 
                
                (u'ஷ்', u'அ') : u'ஷ', (u'ஷ்', u'ஆ') : u'ஷா', (u'ஷ்', u'இ') : u'ஷி', 
                (u'ஷ்', u'ஈ') : u'ஷீ', (u'ஷ்', u'உ') : u'ஷு', (u'ஷ்', u'ஊ') : u'ஷூ', 
                (u'ஷ்', u'எ') : u'ஷெ', (u'ஷ்', u'ஏ') : u'ஷே', (u'ஷ்', u'ஐ') : u'ஷை', 
                (u'ஷ்', u'ஒ') : u'ஷொ', (u'ஷ்', u'ஓ') : u'ஷோ', (u'ஷ்', u'ஔ') : u'ஷௌ', 
                
                (u'ஸ்', u'அ') : u'ஸ', (u'ஸ்', u'ஆ') : u'ஸா', (u'ஸ்', u'இ') : u'ஸி', 
                (u'ஸ்', u'ஈ') : u'ஸீ', (u'ஸ்', u'உ') : u'ஸு', (u'ஸ்', u'ஊ') : u'ஸூ', 
                (u'ஸ்', u'எ') : u'ஸெ', (u'ஸ்', u'ஏ') : u'ஸே', (u'ஸ்', u'ஐ') : u'ஸை', 
                (u'ஸ்', u'ஒ') : u'ஸொ', (u'ஸ்', u'ஓ') : u'ஸோ', (u'ஸ்', u'ஔ') : u'ஸௌ', 
                
                (u'ஹ்', u'அ') : u'ஹ', (u'ஹ்', u'ஆ') : u'ஹா', (u'ஹ்', u'இ') : u'ஹி', 
                (u'ஹ்', u'ஈ') : u'ஹீ', (u'ஹ்', u'உ') : u'ஹு', (u'ஹ்', u'ஊ') : u'ஹூ', 
                (u'ஹ்', u'எ') : u'ஹெ', (u'ஹ்', u'ஏ') : u'ஹே', (u'ஹ்', u'ஐ') : u'ஹை', 
                (u'ஹ்', u'ஒ') : u'ஹொ', (u'ஹ்', u'ஓ') : u'ஹோ', (u'ஹ்', u'ஔ') : u'ஹௌ', 
                }


print "Testing consonants..."
print Ezhuthu.is_consonant(u'அ')
print Ezhuthu.is_consonant(u'ஆ')
print Ezhuthu.is_consonant(u'க்')
print Ezhuthu.is_consonant(u'ங்')
print Ezhuthu.is_consonant(u'ய்')
print Ezhuthu.is_consonant(u'ஃ')
print Ezhuthu.is_consonant(u'க')
print Ezhuthu.is_consonant(u'k')

print "Testing nedils..."
print Ezhuthu.is_nedil(u'அ')
print Ezhuthu.is_nedil(u'ஆ')
print Ezhuthu.is_nedil(u'க்')
print Ezhuthu.is_nedil(u'ங்')
print Ezhuthu.is_nedil(u'ய்')
print Ezhuthu.is_nedil(u'ஃ')
print Ezhuthu.is_nedil(u'க')
print Ezhuthu.is_nedil(u'k')

class EzhuthuTest(unittest.TestCase):
    """
    A test class for the Ezhuthu module
    """
    
    def setUp(self):
        self.letter = Ezhuthu()
    
    def tearDown(self):
        self.letter.dispose()
        self.letter = None
    
    def testIsVowelWithVowels(self):
        """is_vowel should return True for all vowels"""
        
        for vowel in Ezhuthu.VOWELS:
            
            self.failUnless(Ezhuthu.is_vowel(vowel))

    def testIsVowelWithConsonants(self):
        """is_vowel should return False on all consonants"""
        
        for consonant in Ezhuthu.CONSONANTS:
            
            self.failIf(Ezhuthu.is_vowel(consonant))

            
        
        
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
