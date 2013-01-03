# -*- coding: utf-8 -*-
#!/usr/bin/python

import unicodedata

class Ezhuthu:
    """
    Module to handle Tamil letter processing 
    """
    
    ## Declare static variables

    
    VOWEL_TO_ENDING_MAP  = {
                            u'அ' : u'',     # அ -> '' (empty string)
                            u'ஆ' : u'\u0BBE', # ஆ -> ா 
                            u'இ' : u'\u0BBF', # இ -> ி 
                            u'ஈ' : u'\u0BC0', # ஈ -> ீ 
                            u'உ' : u'\u0BC1', # உ -> ு 
                            u'ஊ' : u'\u0BC2',  # ஊ -> ூ
                            u'எ': u'\u0BC6', # எ -> ெ 
                            u'ஏ' : u'\u0BC7', # ஏ -> ே 
                            u'ஐ' : u'\u0BC8', # ஐ -> ை 
                            u'ஒ' : u'\u0BCA', # ஒ -> ொ  
                            u'ஓ' : u'\u0BCB', # ஓ -> ோ 
                            u'ஔ' : u'\u0BCC' # ஔ -> ௌ 
                            } 
    
    # create an inverse map as well
    ENDING_TO_VOWEL_MAP = dict((ending, vowel) for vowel, ending in VOWEL_TO_ENDING_MAP.iteritems())
    
    # create vowel ending list from the dictionary's keys and values
    COMBINATION_ENDINGS = VOWEL_TO_ENDING_MAP.values()
    
    PULLI =  u'்'
    
    AYTHAM  = u'ஃ'
    
    CONSONANTS = {
                  'VALLINAM'  : (u'க்', u'ச்', u'ட்', u'த்', u'ப்', u'ற்'),
                  'MELLINAM'  : (u'ங்', u'ஞ்', u'ண்', u'ந்', u'ம்', u'ன்'),
                  'IDAIYINAM' : (u'ய்',u'ர்', u'ல்', u'வ்', u'ழ்', u'ள்'),
                  'GRANTHA'   : (u'ஶ்', u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்', u'க்ஷ்')
                  }
    
    VOWELS = {
              'KURIL' : (u'அ', u'இ', u'உ', u'எ', u'ஒ'),
              'NEDIL' : (u'ஆ', u'ஈ', u'ஊ', u'ஏ', u'ஐ', u'ஓ', u'ஔ')
              }
    

    

    @staticmethod
    def get_script_name(letter = u''):
        """ Returns the name of the script that the unicode character is encoded in """
        
        return unicodedata.name(letter).split()[0]

    
    @staticmethod
    def validate_letter(letter = u''):
        """
        Ensures that letter is of type unicode, is not equal to an empty string and is a Tamil letter (according to the Unicode consortium).
        If one of these conditions is not met, an Exception is raised. If all of them are met, True is returned
        """
        
        # Check for non-unicode objects
        if not isinstance(letter, unicode):
            raise TypeError("Must be. Value %s of type %s received" %(letter, type(letter)))

        # Check for empty strings
        if len(letter)==0:
            raise ValueError("Expected a Unicode character. Empty string received.")
        
        # Check for non-Tamil characters
        script_language = Ezhuthu.get_script_name(letter).title()
        if  script_language != 'Tamil':
            raise ValueError("Expected a Tamil character. %s is from the %s script" %(letter, script_language))
        
        # Check for more than one character
        # TODO: Implement this
        
        # If we've gotten this far, everything seems to be alright
        return True

    @staticmethod
    def is_aytham(letter = u''):
        """
        Checks whether the given letter is the Aytha Ezhuthu (ஃ)
        """                
        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        return letter == Ezhuthu.AYTHAM
    
    
    @staticmethod
    def is_vowel(letter = u''):
        """ 
        a character is a vowel if it has a length of one and if its value is between
        1249 (அ) and 1263 (ஔ)
        """ 
        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        return len(letter)==1 and (ord(u'அ') <= ord(letter) <= ord(u'ஔ'))

    @staticmethod
    def is_consonant(letter = u''):
        """ 
        a character is a consonant if it has a length of two and its
        second (and last) character is the pulli (்) 
        """
        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        return len(letter)==2 and (letter[1] == u'்')
    
    @staticmethod
    def is_combination(letter = u''):
        """ 
        Check whether a letter is a combination or not
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        # a letter is a combination if it has exactly two characters, the first of which is in the 'அ' column, 
        # and the second of which is a combination ending ( ே,  ி, etc.)
        return len(letter)==2 and (ord(u'க') <= ord(letter[0]) <= ord(u'ஹ')) and letter[1] in Ezhuthu.COMBINATION_ENDINGS

    
    @staticmethod
    def get_letter_type(letter = u''):
        """ Returns the letter type: Vowel, Consonant or Combination """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        if Ezhuthu.is_vowel(letter):
            return 'VOWEL'
        elif Ezhuthu.is_consonant(letter):
            return 'CONSONANT'
        elif Ezhuthu.is_combination(letter):
            return 'COMBINATION'
        else:
            raise Exception("Unknown error. Letter %s is coming up as neither a vowel, consonant or combination" %letter)


    @staticmethod
    def is_kuril(letter = u''):
        """ 
        A character is 'kuril' if it is a vowel or combination with a short sound.
        Raise a TypeError if the letter is a consonant.
        """      
        
        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        ## This was commented out so that function is more forgiving, raising less exceptions
        # consonants cannot be kuril or nedil
        #if Ezhuthu.is_consonant(letter):
            #raise TypeError("The kuril/nedil (long vowel / short vowel) distinction only applies to vowels and to combinations. %s is a consonant." %letter)
        
        # retrieve the vowel component of the letter and check if it's a kuril sound
        _, vowel = Ezhuthu.split_combination(letter)        
        return vowel in Ezhuthu.VOWELS['KURIL']
    
    
    @staticmethod
    def is_nedil(letter = u''):
        """ a character is 'nedil' if it is a vowel or combination with a short sound
            Raise a TypeError if the letter is a consonant.
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        ## This was commented out so that function is more forgiving, raising less exceptions
        # consonants cannot be kuril or nedil
        # if Ezhuthu.is_consonant(letter):
            # raise TypeError("The kuril/nedil (long vowel / short vowel) distinction only applies to vowels and to combinations. %s is a consonant." %letter)

        # retrieve the vowel component of the letter and check if it's a kuril sound
        _, vowel = Ezhuthu.split_combination(letter)        
        return vowel in Ezhuthu.VOWELS['NEDIL']
    
    
    @staticmethod
    def get_vowel_type(letter = u''):
        """
        Returns the vowel type (i.e. 'KURIL' or 'NEDIL')
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        # ensure that the letter is a vowel
        if not Ezhuthu.is_vowel(letter) and not Ezhuthu.is_combination(letter):
            raise ValueError("Vowel or combination expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))
        
        # retrieve and return the vowel type 
        for vowel_type in Ezhuthu.VOWELS:
            if letter in Ezhuthu.VOWELS[vowel_type]:
                return vowel_type
        
        # if we got this far, an unknown error occurred
        raise Exception("Unknown error. Letter %s is coming up as neither kuril nor nedil" %letter)        


    @staticmethod
    def is_vallinam(letter = u''):
        """
        Checks whether or not a given letter is vallinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        if not Ezhuthu.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))        
        
        # retrieve the consonant component of the letter and check if it's a hard consonant
        consonant, _ = Ezhuthu.split_combination(letter)        
        return consonant in Ezhuthu.CONSONANTS['VALLINAM']

    @staticmethod
    def is_mellinam(letter = u''):
        """
        Checks whether or not a given letter is mellinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        if not Ezhuthu.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))        
        
        # retrieve the consonant component of the letter and check if it's a soft consonant
        consonant, _ = Ezhuthu.split_combination(letter)        
        return consonant in Ezhuthu.CONSONANTS['MELLINAM']
    
    @staticmethod
    def is_idaiyinam(letter = u''):
        """
        Checks whether or not a given letter is idaiyinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        if not Ezhuthu.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))        
        
        # retrieve the consonant component of the letter and check if it's a medium consonant
        consonant, _ = Ezhuthu.split_combination(letter)        
        return consonant in Ezhuthu.CONSONANTS['IDAIYINAM']
    
    @staticmethod
    def is_grantha(letter = u''):
        """
        Checks whether or not a given letter is grantha
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        if not Ezhuthu.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))        
        
        # retrieve the consonant component of the letter and check if it's a grantha consonant
        consonant, _ = Ezhuthu.split_combination(letter)        
        return consonant in Ezhuthu.CONSONANTS['GRANTHA']
    
                
    @staticmethod
    def get_consonant_type(letter = u''):
        """
        Returns the consonant type (i.e. 'VALLINAM', 'MELLINAM', 'IDAIYINAM' or 'GRANTHA')
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        # ensure that the letter is a vowel
        if not Ezhuthu.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter %s is a %s" %(letter, Ezhuthu.get_letter_type(letter).title()))
        
        # retrieve and return the vowel type 
        for consonant_type in Ezhuthu.CONSONANTS:
            if letter in Ezhuthu.CONSONANTS[consonant_type]:
                return consonant_type
        
        # if we got this far, an unknown error occurred
        raise Exception("Unknown error. Letter %s is coming up as neither kuril nor nedil" %letter)    
    

    @staticmethod
    def get_combination(consonant=u'', vowel=u''):
        """ 
        Returns a combination given a vowel and a consonant
        """
        
        # ensure that the consonant and vowel are valid single Tamil unicode graphemes 
        Ezhuthu.validate_letter(consonant)
        Ezhuthu.validate_letter(vowel)
        
        if not Ezhuthu.is_consonant(consonant):
            raise ValueError("Consonant expected. %s is not a consonant" %consonant)

        if not Ezhuthu.is_vowel(vowel):
            raise ValueError("Vowel expected. %s is not a vowel" %(vowel))
        
        # store combination initially as an array
        combination = []
        
        # combination = first part of consonant (i.e. the அ-column, plus the extension)
        combination.append(consonant[0])
        combination.append(Ezhuthu.VOWEL_TO_ENDING_MAP[vowel])
        
        return ''.join(combination)


            
    @staticmethod
    def split_combination(letter=u''):
        """ 
        Returns a consonant, vowel tuple when given a combination
        """
        # ensure that the letter is a valid single Tamil unicode grapheme 
        Ezhuthu.validate_letter(letter)
        
        # if consonant, no vowel in the tuple
        if Ezhuthu.is_consonant(letter):
            return letter,  u''
        
        # if vowel or Aytham, no consonant in the tuple 
        elif Ezhuthu.is_vowel(letter) or Ezhuthu.is_aytham(letter):
            return  u'', letter
        
        # if combination ending with -அ, return அ 
        elif len(letter)==1 and (ord(u'க') <= ord(letter) <= ord(u'ஹ')):
            return letter, u'அ' 
        
        # otherwise, separate the vowel from the extension and return it
        elif len(letter)==2 and Ezhuthu.is_combination(letter):
            
            # the consonant is the first part, plus the pulli
            consonant = []
            consonant.append(letter[0])
            consonant.append(Ezhuthu.PULLI)
            consonant = ''.join(consonant)      # convert to string
            
            # get vowel using the extension
            vowel =  Ezhuthu.ENDING_TO_VOWEL_MAP[letter[1]]
            
            # return the (consonant, vowel) tuple           
            return consonant, vowel
        

    @staticmethod
    def get_column(vowel = u''):
        """
        Returns a dictionary of combinations for a particular vowel, mapped by consonant
        """
        #TODO: Implement thi
        
        
    @staticmethod
    def get_row(consonant = u''):
        """
        Returns a dictionary of combinations for a particular consonant, mapped by vowel
        """
        for vowel in Ezhuthu.VOWELS:
            #TODO: make this work
            pass
    

    

