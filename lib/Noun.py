# -*- coding: utf-8 -*-
#!/usr/bin/python

from Ezhuthu import Ezhuthu
from Chol import Chol


class Noun(Chol):

        
    @staticmethod
    def validate_class(noun_class = 0):
        """ docstring """

        
        #TODO: implement method
    
    @staticmethod
    def get_class(word = u''):
        """ Returns the noun class for a given word """
        
        ### See flowchart in docs/material/sendhil/noun_classes.png for more details
        
        Chol.validate_word(word)
        word = Chol.split_letters(word)
        
        ## For noun classes ending in a consonant:
        ## Ending in ம் -> class 1
        ## Ending in ல், ன், ய், ள், ண் AND has exactly two graphemes AND first letter is kuril: class 2
        ## All other consonant-ending nouns -> class 3
        
        if Ezhuthu.is_consonant(word[-1]):
            
            if word[-1] == u'ம்':
                return 1
            
            elif word[-1] in (u'ல்', u'ன்', u'ய்', u'ள்', u'ண்') and len(word)==2 and Ezhuthu.is_kuril(word[0]):
                return 2
            
            else:
                return 3
            
        ## For noun classes not ending in a combination:
        ## TODO: What if a noun ends in Aytham?
        ## TODO: Has this been tested on one-letter long all-vowel nouns (e.g. ஈ)?
        ## Ends in இ, ஈ or ஐ -> class 4
        ## Ends in ஆ, ஏ, ஊ or ஓ -> class 5
        ## Has exactly two graphemes AND first letter is kuril -> class 6
        ## Ends in று and penultimate grapheme is not a consonant -> class 7
        ## Ends in டு and penultimate grapheme is not a consonant -> class 8
        ## TODO: The above two rules assume the word is at least two graphemes long. Valid assumption?
        ## All other cases: class 9
        
        else:
            
            _, ending_vowel = Ezhuthu.split_combination(word[-1])
            
            if ending_vowel in (u'இ', u'ஈ', u'ஐ'):
                return 4
            
            elif ending_vowel in (u'ஆ', u'ஏ', u'ஊ', u'ஓ'):
                return 5
            
            elif len(word)==2 and Ezhuthu.is_kuril(Chol[0]):
                return 6
            
            elif word[-1]==u'று' and not Ezhuthu.is_consonant(word[-2]):
                return 7
            
            elif word[-1]==u'டு' and not Ezhuthu.is_consonant(word[-2]):
                return 8
            
            else:
                return 9
        
    @staticmethod
    def add_suffix(word = u'', word_class=0, suffix = ''):
        """ docstring """

        
        #TODO: Implement method
             
             
    
    @staticmethod
    def get_plural(word = u''):
        """ docstring """

        
        #TODO: Implement method
        
    
          
    
    @staticmethod
    def get_root(word):
            """ docstring """

        
        #TODO: Implement method
        
