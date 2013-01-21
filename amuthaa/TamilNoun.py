# -*- coding: utf-8 -*-
#!/usr/bin/python

from TamilLetter import TamilLetter
from TamilWord import TamilWord

# Suffix dictionary: maps suffix to வேற்றுமை type
SUFFIX_VETTRUMAI = {
                    u'ஐ' : 2,
                    u'ஆல்' : 3,
                    u'ஓடு' : 3,
                    u'உடன்' : 3,
                    u'கு' : 4,
                    u'இல்' : 5,
                    u'இன்' : 5,
                    u'ஐ விட' : 5,
                    # u' இனின்று' : 5,  - commented this out. Never heard of it
                    u'இலிருந்து' : 5,
                    u'அது' : 6,
                    u'ஆது' : 6,
                    u'அ' : 6,
                    u'உடைய' : 6,
                    u'இனுடைய' : 6,
                    u'இல்' : 7,
                    u'இடத்தில்' : 7,
                    u'மேல்' : 7,
                    u'இன்மேல்' : 7,
                    u'கீழ்' : 7,
                    u'இன்கீழ்' : 7,
                    u'உள்' : 7,
                    u'கு உள்' : 7,
                    u'உம்' : 0,
                    u'ஆ' : 0,
                    u'ஏ' : 0,
                    u'ஓ' : 0
                    }


class TamilNoun(TamilWord):
    

    @staticmethod
    def validate_class(noun_class = 0):
        """ docstring """

        #TODO: implement method
    
    @staticmethod
    def get_class(word = u''):
        """ Returns the noun class for a given word """
        
        ### See flowchart in docs/material/sendhil/noun_classes.png for more details
        # TODO: Upload the flowchart to the github wiki and Update the above comment
        
        word = TamilWord(word)
        
        ## For noun classes ending in a consonant:
        ## Ending in ம் -> class 1
        ## Ending in ல், ன், ய், ள், ண் AND has exactly two graphemes AND first letter is kuril: class 2
        ## All other consonant-ending nouns -> class 3
        
        if TamilLetter.is_consonant(word[-1]):
            
            if word[-1] == u'ம்':
                return 1
            
            elif word[-1] in (u'ல்', u'ன்', u'ய்', u'ள்', u'ண்') and len(word)==2 and TamilLetter.is_kuril(word[0]):
                return 2
            
            else:
                return 3
            
        ## For noun classes not ending in a combination:
        ## TODO: What if a noun ends in Aytham?
        ## TODO: Has thiTamilLettertested on one-letter long all-vowel nouns (e.g. ஈ)?
        ## Ends in இ, ஈ or ஐ -> class 4
        ## Ends in ஆ, ஏ, ஊ or ஓ -> class 5
        ## Has exactly two graphemes AND first letter is kuril -> class 6
        ## Ends in று and penultimate grapheme is not a consonant -> class 7
        ## Ends in டு and penultimate grapheme is not a consonant -> class 8
        ## TODO: The above two rules assume the word is at least two graphemes long. Valid assumption?
        ## All other cases: class 9
        
        else:
            
            _, ending_vowel = TamilLetter.split_combination(word[-1])
            
            if ending_vowel in (u'இ', u'ஈ', u'ஐ'):
                return 4
            
            elif ending_vowel in (u'ஆ', u'ஏ', u'ஊ', u'ஓ'):
                return 5
            
            elif len(word)==2 and TamilLetter.is_kuril(TamilWord[0]):
                return 6
            
            elif word[-1]==u'று' and not TamilLetter.is_consonant(word[-2]):
                return 7
            
            elif word[-1]==u'டு' and not TamilLetter.is_consonant(word[-2]):
                return 8
            
            else:
                return 9
        
    @staticmethod
    def add_suffix(word = u'', suffix = u''):
        """ Adds a given suffix to a given noun and returns the result """

        # validate word and get noun class
        TamilWord.validate(word)
        noun_class = TamilNoun.get_class(word)
        word = TamilWord(word)
        
        #TODO: validate the suffix
        
        # Class 1: Word ends in ம்
        # a) Remove ம், and add த்த்
        # b) Simple combination
        if noun_class == 1:
            
            # change ம்->த் if we're dealing with a vettRumai 
            if SUFFIX_VETTRUMAI[suffix]:
            
                word[-1] = u'த்'
                
            # in either case, add the suffix through a simple combination
            word.add_ending(suffix)
            
        # Class 2: _______________________
        # a) Double the last consonant
        # b) Double the last consonant
        elif noun_class == 2:
            
            # double the last letter then add the suffix, whether it's a veTTrumai urubu or not
            word += word[-1]
            word.add_ending(suffix)
        
        
        # Class 3: Ends in consonant, not in class 1 or 2
        # a) Simple combination
        # b) Simple combination
        elif noun_class == 3:
            
            # simple combination
            word.add_ending(suffix)
            
        
        # Class 4: Ends in இ, ஈ, ஐ, எ
        # a) Add ய்
        # b) Add ய்
        elif noun_class == 4:
            # add ய் first, then simple combination
            word += u'ய்'
            word.add_ending(suffix)
        
        # Class 5, 6: Ends in ஆ, ஓ, ஊ or _______________________
        # a) Add வ்
        # b) Add வ்
        elif noun_class in (5, 6):
        
            # add வ் first, then simple combination
            word += 'வ்'
            word.add_ending(suffix)
        
        # Class 7, 8: Ends in டு or று
        # a) Split combination, remove vowel, double consonant
        elif noun_class in (7, 8) and SUFFIX_VETTRUMAI[suffix]:
        
            # Remove the 'உ' component of the last letter, double the last letter, then simple combination
            consonant, _ = TamilLetter.split_combination(word[-1])
            word[-1] = consonant
            word += consonant
            word.add_ending(suffix)
        
        # Class 7, 8: Ends in டு or று
        # b) Split combination, remove vowel, simple combination
        # Class 9: Ends in உ, not in class 6, 7 or 8
        # a) Split combination, remove vowel, simple combination
        # b) Split combination, remove vowel, simple combination
        elif (noun_class in (7, 8) and not SUFFIX_VETTRUMAI[suffix]) or noun_class == 9:

            # Remove the 'உ' component of the last letter, then simple combination
            consonant, _ = TamilLetter.split_combination(word[-1])
            word[-1] = consonant
            word.add_ending(suffix)

    
    @staticmethod
    def get_plural(word = u''):
        """ docstring """

        
        #TODO: Implement method
        
    
          
    
    @staticmethod
    def get_root(word):
            """ docstring """

        
        #TODO: Implement method
        
