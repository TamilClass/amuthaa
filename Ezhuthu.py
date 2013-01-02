# -*- coding: utf-8 -*-
#!/usr/bin/python

vowel_endings = {u'\u0BBE': u'ஆ', 
                 u'\u0BBF': u'இ', 
                 u'\u0BC0': u'ஈ',
                 u'\u0BC1': u'உ',
                 u'\u0BC2': u'ஊ', 
                 u'\u0BC6': u'எ', 
                 u'\u0BC7': u'ஏ', 
                 u'\u0BC8': u'ஐ',
                 u'\u0BCA': u'ஒ', 
                 u'\u0BCB': u'ஓ', 
                 u'\u0BCC': u'ஔ'}


class Ezhuthu:
    
    def __init__(self, letter=""):
        self.letter = letter
        
    def final_letter(self):
        """ Returns the final letter in the word
        """
        return Ezhuthu(self.letter[-1])
    
    def final_vowel(self):
        """ Returns the final vowel that the letter ends in.
            Return None if the final letter is a consonant  
        """
        final_letter = Ezhuthu(self.letter[-1])        
        
        # if consonant - no final vowel
        if final_letter.is_consonant():
            return None
        
        # if vowel - return the vowel
        elif self.is_vowel():
            return final_letter
        
        # if combination ending with -அ, return அ 
        elif len(self.letter)==1 and (ord(u'க') <= ord(final_letter.letter) <= ord(u'ஹ')):
            return Ezhuthu(u'அ') 
        
        # otherwise, separate the vowel from the extension and return it
        else:
            return Ezhuthu(vowel_endings(final_letter.letter))
        
            pass
        
    def is_vowel(self):
        """ a character is a vowel if it has a length of one and if its value is between
            1249 (அ) and 1263 (ஔ)
            """ 
        return len(self.letter)==1 and (ord(u'அ') <= ord(self.letter) <= ord(u'ஔ'))

    def is_consonant(self):
        """ a character is a consonant if it has a length of two and its
            second (and last) character is the pulli (்) 
            """
        return len(self.letter)==2 and (self.letter[1] == u'்')
    
    def is_combination(self):
        not (self.is_vowel() or self.is_consonant()) 



a = Ezhuthu(u"")
print a.is_consonant()