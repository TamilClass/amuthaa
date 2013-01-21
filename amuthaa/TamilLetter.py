# -*- coding: utf-8 -*-
#!/usr/bin/python

import unicodedata
import string


class TamilLetter:
    """ Class to handle Tamil letter processing

    The TamilLetter class has a number of different static functions that help
    with the processing of Tamil letters.
    """

    # A mapping between Tamil vowels and the grapheme that provides that
    # particular vowel sound if it were the 'extension'/'marking' of a
    # combination. E.g. 'ஆ' should map to 'ா'

    VOWEL_TO_ENDING_MAP = {
                            u'அ': u'',          # அ -> '' (empty string)
                            u'ஆ': u'\u0BBE',    # ஆ -> ா
                            u'இ': u'\u0BBF',    # இ -> ி
                            u'ஈ': u'\u0BC0',     # ஈ -> ீ
                            u'உ': u'\u0BC1',    # உ -> ு
                            u'ஊ': u'\u0BC2',    # ஊ -> ூ
                            u'எ': u'\u0BC6',     # எ -> ெ
                            u'ஏ': u'\u0BC7',     # ஏ -> ே
                            u'ஐ': u'\u0BC8',     # ஐ -> ை
                            u'ஒ': u'\u0BCA',     # ஒ -> ொ
                            u'ஓ': u'\u0BCB',     # ஓ -> ோ
                            u'ஔ': u'\u0BCC'     # ஔ -> ௌ
                            }

    # an inverse mapping of the above relationship, mapping  a grapheme that
    # represents the 'extension'/'marking' portion of a combination with its
    # respective vowel sound. E.g  'ா' should map to 'இ'
    ENDING_TO_VOWEL_MAP = dict((ending, vowel) for vowel, ending in
                            VOWEL_TO_ENDING_MAP.iteritems() if ending != u'')

    # create vowel ending list from the dictionary's keys and values
    COMBINATION_ENDINGS = ENDING_TO_VOWEL_MAP.keys()

    PULLI = u'்'

    AYTHAM = u'ஃ'

    CONSONANTS = {
                  'VALLINAM': (u'க்', u'ச்', u'ட்', u'த்', u'ப்', u'ற்'),
                  'MELLINAM': (u'ங்', u'ஞ்', u'ண்', u'ந்', u'ம்', u'ன்'),
                  'IDAIYINAM': (u'ய்', u'ர்', u'ல்', u'வ்', u'ழ்', u'ள்'),

                  ## Removing support for 'க்ஷ்' and 'ஶ்' temporarily
                  #TODO: Add support for 'க்ஷ்', 'ஶ்'
                  #'GRANTHA'   : (u'ஶ்', u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்', u'க்ஷ்')
                  'GRANTHA': (u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்')
                  }

    VOWELS = {
              'KURIL': (u'அ', u'இ', u'உ', u'எ', u'ஒ'),
              'NEDIL': (u'ஆ', u'ஈ', u'ஊ', u'ஏ', u'ஐ', u'ஓ', u'ஔ')
              }

    @staticmethod
    def get_script_name(codepoint=u''):
        """ Returns name of character's script

        Returns the name of the script in which the unicode codepoint is
        encoded.

        Args:
            codepoint: A single unicode codepoint

        Returns:
            A string containing the name of the script that the unicode
            codepoint is encoded in. For example:
            for a Tamil codepoint, it would return 'Tamil', for a Western
            European codepoint it would return 'Latin', for a Russian codepoint
            it would return 'Cyrillic'

        Raises:
            TypeError: A single unicode codepoint was not entered

        """

        if (not codepoint or
            len(codepoint) != 1 or not isinstance(codepoint, unicode)):
                raise TypeError("Expecting single unicode character")

        return unicodedata.name(codepoint[0]).split()[0]

    @staticmethod
    def validate_letter(letter=u''):
        """
        Ensures that letter is of type unicode, is not equal to an empty string and is a Tamil letter (according to the Unicode consortium).
        If one of these conditions is not met, an Exception is raised. If all of them are met, True is returned
        """

        # Check for non-unicode objects
        if not isinstance(letter, unicode):
            raise TypeError("Must be unicode string. Value \'%s\' of type %s received" %(letter, type(letter)))

        # Check for empty strings
        if len(letter) == 0:
            raise ValueError("Expected a Unicode character. Empty string received.")

        # Check for non-Tamil, non-whitespace characters
        script_language = TamilLetter.get_script_name(letter).title()
        if  script_language != 'Tamil' and not TamilLetter.is_whitespace(letter):
            raise ValueError("Expected a Tamil character or whitespace. \'%s\' is from the %s script" %(letter, script_language))

        # TODO: for more than one character

        # TODO: Allow punctuation and digits 

        # If we've gotten this far, everything seems to be alright
        return True

    ## Getter methods for aytham, vowels, consonants and combinations

    @staticmethod
    def get_aytham():
        """ Returns a single unicode letter - aytham """

        return TamilLetter.AYTHAM

    @staticmethod
    def get_vowels():
        """ Returns a tuple of all the vowels """

        # get keys from VOWEL_TO_ENDING_MAP and convert to tuple
        return tuple(TamilLetter.VOWEL_TO_ENDING_MAP.keys())

    @staticmethod
    def get_consonants():
        """ Returns a tuple of all the consonants """

        # merge all sub-iterables in CONSONANTS into one tuple 
        return  tuple(consonant for consonant_group in TamilLetter.CONSONANTS.values() for consonant in consonant_group)

    @staticmethod
    def get_letter_type(letter=u''):
        """ Returns the letter type: Vowel, Consonant or Combination """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        if TamilLetter.is_vowel(letter):
            return 'VOWEL'
        elif TamilLetter.is_consonant(letter):
            return 'CONSONANT'
        elif TamilLetter.is_combination(letter):
            return 'COMBINATION'
        elif TamilLetter.is_aytham(letter):
            return 'AYTHAM'
        else:
            raise Exception("Unknown error. Letter \'%s\' is coming up as neither a vowel, consonant combination, or aytham" %letter)

    @staticmethod
    def is_aytham(letter=u''):
        """
        Checks whether the given letter is the Aytha TamilLetter (ஃ)
        """
        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        return letter == TamilLetter.get_aytham()


    ## Boolean methods to check whether a given letter is aytham, a vowel, a consonant or a combination

    @staticmethod
    def is_vowel(letter=u''):
        """ 
        a character is a vowel if it has a length of one and if its value is between
        2949 (அ) and 2964 (ஔ)
        """ 
        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        return len(letter)==1 and (ord(u'அ') <= ord(letter) <= ord(u'ஔ'))

    @staticmethod
    def is_consonant(letter=u''):
        """ 
        a character is a consonant if it has a length of two and its
        second (and last) character is the pulli (்) 
        """
        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        return (len(letter)==2 and (letter[1] == u'்')) and (ord(u'க') <= ord(letter[0]) <= ord(u'ஹ'))

    @staticmethod
    def is_combination(letter=u''):
        """ 
        Check whether a letter is a combination or not
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # a letter is a combination if it has exactly two characters, the first of which is in the 'அ' column, 
        # and the second of which is a combination ending ( ே,  ி, etc.)
        return (ord(u'க') <= ord(letter[0]) <= ord(u'ஹ')) and (len(letter)==1 or (len(letter)==2 and letter[1] in TamilLetter.COMBINATION_ENDINGS))


    @staticmethod
    def is_kuril(letter=u''):
        """ 
        A character is 'kuril' if it is a vowel or combination with a short sound.
        """  

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # retrieve the vowel component of the letter and check if it's a kuril sound
        _, vowel = TamilLetter.split_combination(letter)
        return vowel in TamilLetter.VOWELS['KURIL']


    @staticmethod
    def is_nedil(letter=u''):
        """ a character is 'nedil' if it is a vowel or combination with a long sound.
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # retrieve the vowel component of the letter and check if it's a nedil sound
        _, vowel = TamilLetter.split_combination(letter)
        return vowel in TamilLetter.VOWELS['NEDIL']


    @staticmethod
    def get_vowel_type(letter=u''):
        """
        Returns the vowel type (i.e. 'KURIL' or 'NEDIL')
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # ensure that the letter is a vowel or combination
        if not TamilLetter.is_vowel(letter) and not TamilLetter.is_combination(letter):
            raise ValueError("Vowel or combination expected, but the letter \'%s\' is a %s" %(letter, TamilLetter.get_letter_type(letter).title()))

        # if letter is a combination, split out the vowel part
        _, vowel = TamilLetter.split_combination(letter)

        # retrieve and return the vowel type 
        for vowel_type in TamilLetter.VOWELS:
            if vowel in TamilLetter.VOWELS[vowel_type]:
                return vowel_type

        # if we got this far, an unknown error occurred
        raise Exception("Unknown error. Letter \'%s\' is coming up as neither kuril nor nedil" %letter)


    @staticmethod
    def is_vallinam(letter=u''):
        """
        Checks whether or not a given letter is vallinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # if not consonant, it is not a vallinam consonant
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve the consonant component of the letter and check if it's a hard consonant
        consonant, _ = TamilLetter.split_combination(letter)
        return consonant in TamilLetter.CONSONANTS['VALLINAM']

    @staticmethod
    def is_mellinam(letter=u''):
        """
        Checks whether or not a given letter is mellinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve the consonant component of the letter and check if it's a soft consonant
        consonant, _ = TamilLetter.split_combination(letter)
        return consonant in TamilLetter.CONSONANTS['MELLINAM']

    @staticmethod
    def is_idaiyinam(letter=u''):
        """
        Checks whether or not a given letter is idaiyinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # if not consonant, it is not an idaiyinam consonant
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve the consonant component of the letter and check if it's a medium consonant
        consonant, _ = TamilLetter.split_combination(letter)
        return consonant in TamilLetter.CONSONANTS['IDAIYINAM']

    @staticmethod
    def is_grantha(letter=u''):
        """
        Checks whether or not a given letter is grantha
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # if not a consonant, it is not a grantha consonant 
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve the consonant component of the letter and check if it's a grantha consonant
        consonant, _ = TamilLetter.split_combination(letter)
        return consonant in TamilLetter.CONSONANTS['GRANTHA']


    @staticmethod
    def is_whitespace(letter=u''):
        """ Checks whether or not a given letter is whitespace (e.g. a space, tab, etc.) """

        #TODO: write test cases for this
        return len(letter)>0 and (letter.isspace() or unicodedata.category(letter)[0].upper()==u'Z')


    @staticmethod
    def is_punctuation(letter=u''):
        """ Checks whether or not a given letter is punctuation """

        #TODO: write test cases for this
        #TODO: string.punctuation contains some symbols, so the condition below will return false positives
        return letter in string.punctuation or unicodedata.category(letter)[0].upper() in ('P')


    @staticmethod
    def is_digit(letter=u''):
        """ Checks whether or not a given letter is a digit """

        #TODO: write test cases for this
        return letter.isnumeric() or letter.isdecimal() or unicodedata.category(letter[0]).upper() in ('N')


    @staticmethod
    def is_symbol(letter=u''):
        """ Checks whether or not a given letter is a symbol """

        #TODO: write test cases for this
        #TODO: See if the python string function has anything for handling this
        return unicodedata.category(letter)[0].upper() in ('S')


    @staticmethod
    def get_consonant_type(letter=u''):
        """
        Returns the consonant type (i.e. 'VALLINAM', 'MELLINAM', 'IDAIYINAM' or 'GRANTHA')
        """

        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # ensure that the letter is a vowel
        if not TamilLetter.is_consonant(letter):
            raise ValueError("Consonant expected, but the letter \'%s\' is a %s" %(letter, TamilLetter.get_letter_type(letter).title()))

        # retrieve and return the vowel type 
        for consonant_type in TamilLetter.CONSONANTS:
            if letter in TamilLetter.CONSONANTS[consonant_type]:
                return consonant_type

        # if we got this far, an unknown error occurred
        raise Exception("Unknown error. Letter \'%s\' is coming up as neither kuril nor nedil" %letter)


    @staticmethod
    def get_combination(consonant=u'', vowel=u''):
        """ 
        Returns a combination given a vowel and a consonant
        """

        # ensure that the consonant and vowel are valid single Tamil unicode graphemes 
        TamilLetter.validate_letter(consonant)
        TamilLetter.validate_letter(vowel)

        if not TamilLetter.is_consonant(consonant):
            raise ValueError("Consonant expected. \'%s\' is not a consonant" %consonant)

        if not TamilLetter.is_vowel(vowel):
            raise ValueError("Vowel expected. \'%s\' is not a vowel" %(vowel))

        # store combination initially as an array
        combination = []

        # combination = first part of consonant (i.e. the அ-column, plus the extension)
        combination.append(consonant[0])
        combination.append(TamilLetter.VOWEL_TO_ENDING_MAP[vowel])

        return ''.join(combination)



    @staticmethod
    def split_combination(letter=u''):
        """ 
        Returns a consonant, vowel tuple when given a combination
        """
        # ensure that the letter is a valid single Tamil unicode grapheme 
        TamilLetter.validate_letter(letter)

        # if consonant, no vowel in the tuple
        if TamilLetter.is_consonant(letter):
            return letter,  u''

        # if vowel, no consonant in the tuple 
        elif TamilLetter.is_vowel(letter):
            return  u'', letter

        # if combination ending with -அ, return அ 
        elif len(letter)==1 and (ord(u'க') <= ord(letter) <= ord(u'ஹ')):
            return letter+TamilLetter.get_pulli(), u'அ' 

        # if non-அ combination, separate the vowel from the extension and return it
        elif len(letter)==2 and TamilLetter.is_combination(letter):

            # the consonant is the first part, plus the pulli
            consonant = []
            consonant.append(letter[0])
            consonant.append(TamilLetter.PULLI)
            consonant = ''.join(consonant)      # convert to string

            # get vowel using the extension
            vowel =  TamilLetter.ENDING_TO_VOWEL_MAP[letter[1]]

            # return the (consonant, vowel) tuple   
            return consonant, vowel

        # if aytham, return empty unicode strings for both vowel and consonant
        elif TamilLetter.is_aytham(letter):
            return u'', u''

        else:
            raise Exception("An unknown exception occurred for letter %s." %letter)


    @staticmethod
    def get_combination_column(vowel = u''):
        """
        Returns a dictionary of combinations for a particular vowel, mapped by consonant
        """
        ## Ensure that letter is a valid Tamil unicode character and a vowel
        TamilLetter.validate_letter(vowel)

        if not TamilLetter.is_vowel(vowel):
            raise ValueError("Vowel required. \'%s\' is a %s" %(vowel, TamilLetter.get_letter_type(vowel).title()))


        # Declare empty dictionary
        combination_col = {}

        # For each vowel, determine the respective consonant-vowel combination and add it to the dictionary object
        for consonant in TamilLetter.get_consonants():

            # The first letter of the combination is the அ combination for the consonant
            # The second is an extension, which is obtained from the VOWEL_TO_ENDING_MAP
            combination = consonant[0]+TamilLetter.VOWEL_TO_ENDING_MAP[vowel]
            combination_col.update({consonant : combination})


        return combination_col


    @staticmethod
    def get_combination_row(consonant = u''):
        """
        Returns a dictionary of combinations for a particular consonant, mapped by vowel
        """

        ## Ensure that letter is a valid Tamil unicode character and a consonant
        TamilLetter.validate_letter(consonant)

        if not TamilLetter.is_consonant(consonant):
            raise ValueError("Consonant required. \'%s\' is a %s" %(consonant, TamilLetter.get_letter_type(consonant).title()))


        # Declare empty dictionary
        combination_row = {}

        # For each vowel, determine the respective consonant-vowel combination and add it to the dictionary object
        for vowel in TamilLetter.get_vowels():

            # The first letter of the combination is the அ combination for the consonant
            # The second is an extension, which is obtained from the VOWEL_TO_ENDING_MAP
            combination = consonant[0]+TamilLetter.VOWEL_TO_ENDING_MAP[vowel]
            combination_row.update({vowel : combination})

        return combination_row


    @staticmethod
    def get_combination_endings():
        """ Returns a tuple of vowel combination endings (ி ,ீ , ே, etc.) """

        #TODO: create a test case for this

        # get the list of combination endings, remove the empty unicode string and convert to a tuple
        return tuple(TamilLetter.COMBINATION_ENDINGS)


    @staticmethod
    def get_pulli():
        """ Returns the pulli codepoint ('்') """

        #TODO: Create a test case for this

        return TamilLetter.PULLI
