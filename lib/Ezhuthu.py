# -*- coding: utf-8 -*-
#!/usr/bin/python

class Ezhuthu:
    
    ## Declare static variables
    
    vowel_ending_map  = {u'\u0BBE': u'ஆ', # ா -> ஆ 
                         u'\u0BBF': u'இ', # ி -> இ
                         u'\u0BC0': u'ஈ', # ீ -> ஈ
                         u'\u0BC1': u'உ', # ு -> உ
                         u'\u0BC2': u'ஊ',  # ூ -> ஊ
                         u'\u0BC6': u'எ', # ெ -> எ
                         u'\u0BC7': u'ஏ', # ே -> ஏ
                         u'\u0BC8': u'ஐ', # ை -> ஐ
                         u'\u0BCA': u'ஒ', # ொ -> ஒ
                         u'\u0BCB': u'ஓ', # ோ -> ஓ
                         u'\u0BCC': u'ஔ'} # ௌ -> ஔ
    
    vowel_endings = vowel_ending_map.keys()
    vowels = vowel_ending_map.values()
    
    aytham  = [u'ஃ']
    consonants = [u'க்', u'ங்', u'ச்', u'ஞ்', u'ட்', u'ண்', 
                  u'த்', u'ந்', u'ப்', u'ம்', u'ய்', u'ர்', 
                  u'ல்', u'வ்', u'ழ்', u'ள்', u'ற்', u'ன்', 
                  u'ஶ்', u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்', u'க்ஷ்']
    
         
    kuril_vowels = [u'அ', u'இ', u'உ', u'எ', u'ஐ', u'ஒ', u'ஔ']
    nedil_vowels = [u'ஆ', u'ஈ', u'ஊ', u'ஏ', u'ஓ']
    
    hard_consonants = [u'க்', u'ச்', u'ட்', u'த்', u'ப்', u'ற்']
    soft_consonants = [u'ங்', u'ஞ்', u'ண்', u'ந்', u'ம்', u'ன்']
    medium_consonants = [u'ய்',u'ர்', u'ல்', u'வ்', u'ழ்', u'ள்']
    grantha_consonants = [u'ஶ்', u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்', u'க்ஷ்']    
    
    
            
    @staticmethod
    def final_vowel(self, final_letter=u''):
        """ 
        Returns the final vowel that the letter ends in, if it is a combination.
        """
        # if consonant - no final vowel, so return an empty string
        if Ezhuthu.is_consonant(final_letter):
            return u''
        
        # if vowel - return the vowel
        elif Ezhuthu.is_vowel(final_letter):
            return final_letter
        
        # if combination ending with -அ, return அ 
        elif len(final_letter)==1 and (ord(u'க') <= ord(final_letter) <= ord(u'ஹ')):
            return u'அ' 
        
        # otherwise, separate the vowel from the extension and return it
        else:
            return self.vowel_ending_map[final_letter]
        
    
    @staticmethod
    def is_vowel(letter = u''):
        """ 
        a character is a vowel if it has a length of one and if its value is between
        1249 (அ) and 1263 (ஔ)
        """ 
        return len(letter)==1 and (ord(u'அ') <= ord(letter) <= ord(u'ஔ'))

    @staticmethod
    def is_consonant(letter = u''):
        """ 
        a character is a consonant if it has a length of two and its
        second (and last) character is the pulli (்) 
        """
        return len(letter)==2 and (letter[1] == u'்')
    
    @staticmethod
    def is_combination(self, letter = u''):
        """ 
        a character is a combination if its not a vowel or a consonant
        """
        # This will work if the letters are assumed to be Tamil and not aytham
        # TODO: Come up with a better solution
        return not (Ezhuthu.is_vowel(letter) or Ezhuthu.is_consonant(letter)) 
        

    @staticmethod
    def is_kuril(self, letter = u''):
        """ 
        A character is 'kuril' if it is a vowel or combination with a short sound.
        Raise a TypeError if the letter is a consonant.
        """      
        
        if Ezhuthu.is_consonant(letter):
            raise TypeError
        
        return letter in self.kuril_letters
    
    
    @staticmethod
    def is_nedil(self, letter = u''):
        """ a character is 'nedil' if it is a vowel or combination with a short sound
            Raise a TypeError if the letter is a consonant.
        """
        if Ezhuthu.is_consonant(letter):
            raise TypeError

        # a character is nedil if it's not kuril
        return letter in self.nedil_letters


print "Testing vowels..."
print Ezhuthu.is_vowel(u'அ')
print Ezhuthu.is_vowel(u'ஆ')
print Ezhuthu.is_vowel(u'க்')
print Ezhuthu.is_vowel(u'ங்')
print Ezhuthu.is_vowel(u'ய்')
print Ezhuthu.is_vowel(u'ஃ')
print Ezhuthu.is_vowel(u'க')
print Ezhuthu.is_vowel(u'k')

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