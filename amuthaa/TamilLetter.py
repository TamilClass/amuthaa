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
                            'அ': '',  # அ -> '' (empty string)
                            'ஆ': '\u0BBE',  # ஆ -> ா
                            'இ': '\u0BBF',  # இ -> ி
                            'ஈ': '\u0BC0',  # ஈ -> ீ
                            'உ': '\u0BC1',  # உ -> ு
                            'ஊ': '\u0BC2',  # ஊ -> ூ
                            'எ': '\u0BC6',  # எ -> ெ
                            'ஏ': '\u0BC7',  # ஏ -> ே
                            'ஐ': '\u0BC8',  # ஐ -> ை
                            'ஒ': '\u0BCA',  # ஒ -> ொ
                            'ஓ': '\u0BCB',  # ஓ -> ோ
                            'ஔ': '\u0BCC'  # ஔ -> ௌ
                            }

    # an inverse mapping of the above relationship, mapping  a grapheme that
    # represents the 'extension'/'marking' portion of a combination with its
    # respective vowel sound. E.g  'ா' should map to 'இ'
    ENDING_TO_VOWEL_MAP = dict((ending, vowel) for vowel, ending in
                            VOWEL_TO_ENDING_MAP.items() if ending != '')

    # create vowel ending list from the dictionary's keys and values
    COMBINATION_ENDINGS = list(ENDING_TO_VOWEL_MAP.keys())

    PULLI = '்'

    AYTHAM = 'ஃ'

    CONSONANT_TYPES = {
                  'VALLINAM': ('க்', 'ச்', 'ட்', 'த்', 'ப்', 'ற்'),
                  'MELLINAM': ('ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்'),
                  'IDAIYINAM': ('ய்', 'ர்', 'ல்', 'வ்', 'ழ்', 'ள்'),

                  # # Removing support for 'க்ஷ்' and 'ஶ்' temporarily
                  # TODO: Add support for 'க்ஷ்', 'ஶ்'
                  # 'GRANTHA'   : (u'ஶ்', u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்', u'க்ஷ்')
                  'GRANTHA': ('ஜ்', 'ஷ்', 'ஸ்', 'ஹ்')
                  }

    # construct a tuple of consonants from the sub-iterables of CONSONANT_TYPES
    CONSONANTS = tuple(consonant for consonant_group in
                       list(CONSONANT_TYPES.values())
                       for consonant in consonant_group)

    VOWEL_TYPES = {
              'KURIL': ('அ', 'இ', 'உ', 'எ', 'ஒ'),
              'NEDIL': ('ஆ', 'ஈ', 'ஊ', 'ஏ', 'ஐ', 'ஓ', 'ஔ')
              }

    # construct a tuple of VOWELS from keys of the VOWEL_TO_ENDING_MAP dict
    VOWELS = tuple(VOWEL_TO_ENDING_MAP.keys())

    @staticmethod
    def get_script_name(codepoint=''):
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

        if not codepoint or not isinstance(codepoint, str) or \
            not (1 <= len(codepoint) <= 2):
                raise TypeError("Expecting single unicode character")

        # TODO: Sanity check - ensure all characters are same language

        return unicodedata.name(codepoint[0]).split()[0]

    @staticmethod
    def assert_valid_letter(letter=''):
        """ Asserts that the given letter is a valid Tamil unicode grapheme

        Checks that the letter is of type unicode, is not equal to an empty
        string and is a Tamil letter (according to the Unicode consortium).

        Returns:
            True: If the letter is a valid Tamil unicode grapheme

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, or non-Tamil grapheme or codepoint
        """

        # Check for non-unicode objects
        if not isinstance(letter, str):
            raise TypeError("""Must be unicode string. Value \'%s\' of type
                %s received""" % (letter, type(letter)))

        # Check for empty strings
        if len(letter) == 0:
            raise ValueError("Expected Unicode character, not empty string.")

        # Check for non-Tamil, non-whitespace characters
        script_language = TamilLetter.get_script_name(letter).title()
        if  script_language != 'Tamil' and \
            not TamilLetter.is_whitespace(letter):

            raise ValueError("""Expected a Tamil character or whitespace.
                \'%s\' is from the %s script""" % (letter, script_language))

        # TODO: Make this work if more than one character is entered

        # TODO: Allow punctuation and digits

        # If we've gotten this far, everything seems to be alright
        return True

    # # Getter methods for aytham, vowels, consonants and combinations
    @staticmethod
    def get_aytham():
        """ Returns Aytham (ஃ)

        Returns a single unicode codepoint - the Aytham - a Tamil letter
        that is neither a vowel, a consonant, or a combination.

        Returns:
            u'ஃ' - the Tamil letter 'aytham'
        """

        return TamilLetter.AYTHAM

    @staticmethod
    def get_vowels():
        """ Returns a tuple of all the Tamil vowels

        Returns a single tuple containing all twelve Tamil vowels:
        (அ, ஆ, இ, ஈ, உ, ஊ, எ, ஏ, ஐ, ஒ, ஓ, ஔ).
        The vowels are not guaranteed to be in any particular order.

        Returns:
            A tuple containing all 12 Tamil vowels
        """

        # get keys from VOWEL_TO_ENDING_MAP and convert to tuple
        return TamilLetter.VOWELS

    @staticmethod
    def get_consonants():
        """ Returns a tuple of all the Tamil consonants

        Returns a single tuple containing all eighteen Tamil consonants:
        க், ச், ட், த், ப், ற், ங், ஞ், ண், ந், ம், ன், ய், ர், ல், வ், ழ், ள்
        and the four grantha consonants (ஜ், ஷ், ஸ், ஹ்) which occur most
        often.         The consonants are not guaranteed to be in any
        particular order.

         Returns:
            A 22-length tuple containing all 18 Tamil consonants and the
            4 most commonly-occuring grantha consonants.
        """

        return TamilLetter.CONSONANTS

    @staticmethod
    def get_letter_type(letter=''):
        """ Returns the type of letter: vowel, consonant, combination
        or aytham

        Given a valid Tamil unicode grapheme, returns a String indicating
        whether the grapheme is a Tamil vowel, consonant, combination
        or aytham.

        Args:
            letter: A valid Tamil unicode grapheme

        Returns:
            'VOWEL', 'CONSONANT', 'COMBINATION' or 'AYTHAM'

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        if TamilLetter.is_vowel(letter):
            return 'VOWEL'
        elif TamilLetter.is_consonant(letter):
            return 'CONSONANT'
        elif TamilLetter.is_combination(letter):
            return 'COMBINATION'
        elif TamilLetter.is_aytham(letter):
            return 'AYTHAM'
        else:
            raise Exception("""Unknown error. Letter \'%s\' is coming up as
                neither a vowel, consonant combination, or aytham""" % letter)

    @staticmethod
    def is_aytham(letter=''):
        """ Checks whether given unicode object is equal to Aytham (ஃ)

        Checks whether the given codepoint is equal to the the Tamil
        letter Aytham (ஃ)

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: if input is equal to the Aytham letter (ஃ)
            False: input is a valid Tamil unicode character other than Aytham

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """
        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        return letter == TamilLetter.get_aytham()

    # Boolean methods to check whether a given letter is aytham, a vowel,
    # a consonant or a combination

    @staticmethod
    def is_vowel(letter=''):
        """ Returns whether or not a given Tamil unicode grapheme is a vowel

        Return whether the given input is a Tamil vowel.
        A character is a vowel if it has a length of one and its codepoint has
        a decimal value between 2949 (அ) and 2964 (ஔ)

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: If input is a valid Tamil vowel
            False: input is a valid Tamil unicode grapheme but not a vowel

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        return len(letter) == 1 and (ord('அ') <= ord(letter) <= ord('ஔ'))

    @staticmethod
    def is_consonant(letter=''):
        """ Returns whether or not given Tamil unicode grapheme is a consonant

        Return whether the given input is a Tamil consonant.
        A character is a consonant if it has a length of two, its first
        codepoint is a letter from the அ ('a') combination column and its
        second codepoint is the pulli (்)

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: If input is a valid Tamil consonant
            False: input is a valid Tamil unicode grapheme but not a consonant

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """
        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        return (len(letter) == 2 and (letter[1] == '்')) and \
            (ord('க') <= ord(letter[0]) <= ord('ஹ'))

    @staticmethod
    def is_combination(letter=''):
        """ Returns whether given Tamil unicode grapheme is a combination

        Return whether the given input is a Tamil combination.
        A character is a combination if it has a length of two, its first
        codepoint is a letter from the அ ('a') combination column and its
        second codepoint is a valid combination ending (e.g. ே,  ி)

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: If input is a valid Tamil combination
            False: input is valid Tamil unicode grapheme but not a combination

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # a letter is a combination if it has exactly two characters:
        # a) the first of which is in the 'அ' column, and
        # b) the second of which is a combination ending ( ே,  ி, etc.)
        return ((ord('க') <= ord(letter[0]) <= ord('ஹ')) and
                len(letter) == 1) or (len(letter) == 2 and letter[1] in \
                                      TamilLetter.COMBINATION_ENDINGS)

    @staticmethod
    def is_kuril(letter=''):
        """ Returns whether given Tamil unicode grapheme is a kuril letter

        Return whether the given input is a Tamil kuril vowel or combination.
        A character is a kuril vowel (or a kuril combination if its vowel
        portion) is one of the five short vowels: அ, இ, உ, எ, ஒ

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: If input is a valid Tamil kuril vowel or combination
            False: input is valid Tamil unicode grapheme but not kuril

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # retrieve vowel component of letter and check if it's a kuril sound
        _, vowel = TamilLetter.split_combination(letter)
        return vowel in TamilLetter.VOWEL_TYPES['KURIL']

    @staticmethod
    def is_nedil(letter=''):
        """ Returns whether given Tamil unicode grapheme is a nedil letter

        Return whether the given input is a Tamil nedil vowel or combination.
        A character is a nedil vowel (or a nedil combination if its vowel
        portion) is one of the seven long vowels: ஆ, ஈ, ஊ, ஏ, ஐ, ஓ, ஔ

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            True: If input is a valid Tamil nedil vowel or combination
            False: input is valid Tamil unicode grapheme but not nedil

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # retrieve vowel component of letter and check if it's a nedil sound
        _, vowel = TamilLetter.split_combination(letter)
        return vowel in TamilLetter.VOWEL_TYPES['NEDIL']

    @staticmethod
    def get_vowel_type(letter=''):
        """ Returns the vowel type (i.e. 'KURIL' or 'NEDIL') of a given vowel

        Returns the vowel type of a given vowel: either 'KURIL' (short)
        or 'NEDIL' (long).

        Args:
            letter: A single Tamil unicode grapheme

        Returns:
            String: 'KURIL' if the letter is a valid Tamil unicode grapheme
                    and is short (i.e. either அ, இ, உ, எ, or ஒ).
                    'NEDIL' if the letter is a valid Tamil unicode grapheme
                    and is long (i.e. one of ஆ, ஈ, ஊ, ஏ, ஐ, ஓ, ஔ)

        Raises:
            TypeError: Input was not of type unicode
            ValueError: Empty string, a non-Tamil grapheme or codepoint
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # ensure that the letter is a vowel or combination
        if (not TamilLetter.is_vowel(letter) and
            not TamilLetter.is_combination(letter)):

            raise ValueError("""Vowel or combination expected, but \'%s\'
                is a %s""" % (letter,
                              TamilLetter.get_letter_type(letter).title()))

        # if letter is a combination, split out the vowel part
        _, vowel = TamilLetter.split_combination(letter)

        # retrieve and return the vowel type
        for vowel_type in TamilLetter.VOWEL_TYPES:
            if vowel in TamilLetter.VOWEL_TYPES[vowel_type]:
                return vowel_type

        # if we got this far, an unknown error occurred
        raise Exception("""Unknown error. Letter \'%s\' is coming up as
            neither kuril nor nedil""" % letter)

    @staticmethod
    def is_vallinam(letter=''):
        """
        Checks whether or not a given letter is vallinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # if not consonant, it is not a vallinam consonant
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve consonant component of the letter (ignore vowel component)
        consonant, _ = TamilLetter.split_combination(letter)

        # and check if it's a soft consonant
        return consonant in TamilLetter.CONSONANT_TYPES['VALLINAM']

    @staticmethod
    def is_mellinam(letter=''):
        """
        Checks whether or not a given letter is mellinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve consonant component of the letter (ignore vowel component)
        consonant, _ = TamilLetter.split_combination(letter)

        # and check if it's a soft consonant
        return consonant in TamilLetter.CONSONANT_TYPES['MELLINAM']

    @staticmethod
    def is_idaiyinam(letter=''):
        """
        Checks whether or not a given letter is idaiyinam
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # if not consonant, it is not an idaiyinam consonant
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve consonant component of the letter
        consonant, _ = TamilLetter.split_combination(letter)
        # and check if it's a medium consonant
        return consonant in TamilLetter.CONSONANT_TYPES['IDAIYINAM']

    @staticmethod
    def is_grantha(letter=''):
        """
        Checks whether or not a given letter is grantha
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # if not a consonant, it is not a grantha consonant
        if not TamilLetter.is_consonant(letter):
            return False

        # retrieve the consonant component of the letter
        consonant, _ = TamilLetter.split_combination(letter)
        # and check if it's a medium consonant
        return consonant in TamilLetter.CONSONANT_TYPES['GRANTHA']

    @staticmethod
    def is_whitespace(letter=''):
        """ Checks whether or not a given letter is whitespace (e.g. a space, tab, etc.) """

        # TODO: write test cases for this
        return len(letter) > 0 and (letter.isspace() or
                                    unicodedata.category(letter)[0].upper() \
                                    == 'Z')

    @staticmethod
    def is_punctuation(letter=''):
        """ Checks whether or not a given letter is punctuation """

        # TODO: write test cases for this

        # TODO: string.punctuation contains some symbols, so the condition
        #        below will return false positives
        return letter in string.punctuation or unicodedata.category(letter)[0].upper() in ('P')

    @staticmethod
    def is_digit(letter=''):
        """ Checks whether or not a given letter is a digit """

        # TODO: write test cases for this
        return letter.isnumeric() or letter.isdecimal() or \
                unicodedata.category(letter[0]).upper() in ('N')

    @staticmethod
    def is_symbol(letter=''):
        """ Checks whether or not a given letter is a symbol """

        # TODO: write test cases for this
        # TODO: See if python string function has anything for handling this
        return unicodedata.category(letter)[0].upper() in ('S')

    @staticmethod
    def get_consonant_type(letter=''):
        """
        Returns the consonant type (i.e. 'VALLINAM', 'MELLINAM', 'IDAIYINAM' or 'GRANTHA')
        """

        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # ensure that the letter is a vowel
        if not TamilLetter.is_consonant(letter):
            raise ValueError("Consonant expected but \'%s\' is a %s"
                             % (letter,
                                TamilLetter.get_letter_type(letter).title()))

        # retrieve and return the vowel type
        for consonant_type in TamilLetter.CONSONANT_TYPES:
            if letter in TamilLetter.CONSONANT_TYPES[consonant_type]:
                return consonant_type

        # if we got this far, an unknown error occurred
        raise Exception("""Unknown error. \'%s\' is coming up as neither
                        kuril nor nedil""" % letter)

    @staticmethod
    def get_combination(consonant='', vowel=''):
        """
        Returns a combination given a vowel and a consonant
        """

        # ensure that consonant and vowel are valid
        # single Tamil unicode graphemes
        TamilLetter.assert_valid_letter(consonant)
        TamilLetter.assert_valid_letter(vowel)

        if not TamilLetter.is_consonant(consonant):
            raise ValueError("Consonant expected. \'%s\' is not a consonant"
                             % consonant)

        if not TamilLetter.is_vowel(vowel):
            raise ValueError("Vowel expected. \'%s\' is not a vowel" % (vowel))

        # store combination initially as an array
        combination = []

        # combination = first part of consonant
        # (i.e. the அ-column, plus the extension)
        combination.append(consonant[0])
        combination.append(TamilLetter.VOWEL_TO_ENDING_MAP[vowel])

        return ''.join(combination)

    @staticmethod
    def split_combination(letter=''):
        """
        Returns a consonant, vowel tuple when given a combination
        """
        # ensure that the letter is a valid single Tamil unicode grapheme
        TamilLetter.assert_valid_letter(letter)

        # if consonant, no vowel in the tuple
        if TamilLetter.is_consonant(letter):
            return letter, ''

        # if vowel, no consonant in the tuple
        elif TamilLetter.is_vowel(letter):
            return  '', letter

        # if combination ending with -அ, return அ
        elif len(letter) == 1 and (ord('க') <= ord(letter) <= ord('ஹ')):
            return letter + TamilLetter.get_pulli(), 'அ'

        # if non-அ combination, separate vowel from extension and return it
        elif len(letter) == 2 and TamilLetter.is_combination(letter):

            # the consonant is the first part, plus the pulli
            consonant = []
            consonant.append(letter[0])
            consonant.append(TamilLetter.PULLI)
            consonant = ''.join(consonant)  # convert to string

            # get vowel using the extension
            vowel = TamilLetter.ENDING_TO_VOWEL_MAP[letter[1]]

            # return the (consonant, vowel) tuple
            return consonant, vowel

        # if aytham, return empty unicode strings for both vowel and consonant
        elif TamilLetter.is_aytham(letter):
            return '', ''

        else:
            raise Exception("An unknown exception occurred for letter %s." % letter)

    @staticmethod
    def get_combination_column(vowel=''):
        """
        Returns a dictionary of combinations for a particular vowel, mapped by consonant
        """
        # # Ensure that letter is a valid Tamil unicode character and a vowel
        TamilLetter.assert_valid_letter(vowel)

        if not TamilLetter.is_vowel(vowel):
            raise ValueError("Vowel required. \'%s\' is a %s" % (vowel, TamilLetter.get_letter_type(vowel).title()))


        # Declare empty dictionary
        combination_col = {}

        # For each vowel, determine the respective consonant-vowel combination and add it to the dictionary object
        for consonant in TamilLetter.get_consonants():

            # The first letter of the combination is the அ combination for the consonant
            # The second is an extension, which is obtained from the VOWEL_TO_ENDING_MAP
            combination = consonant[0] + TamilLetter.VOWEL_TO_ENDING_MAP[vowel]
            combination_col.update({consonant : combination})

        return combination_col

    @staticmethod
    def get_combination_row(consonant=''):
        """
        Returns a dictionary of combinations for a particular consonant, mapped by vowel
        """

        # # Ensure that letter is a valid Tamil unicode character and a consonant
        TamilLetter.assert_valid_letter(consonant)

        if not TamilLetter.is_consonant(consonant):
            raise ValueError("Consonant required. \'%s\' is a %s" % (consonant, TamilLetter.get_letter_type(consonant).title()))

        # Declare empty dictionary
        combination_row = {}

        # For each vowel, determine the respective consonant-vowel combination and add it to the dictionary object
        for vowel in TamilLetter.get_vowels():

            # The first letter of the combination is the அ combination for the consonant
            # The second is an extension, which is obtained from the VOWEL_TO_ENDING_MAP
            combination = consonant[0] + TamilLetter.VOWEL_TO_ENDING_MAP[vowel]
            combination_row.update({vowel : combination})

        return combination_row

    @staticmethod
    def get_combination_endings():
        """ Returns a tuple of vowel combination endings (ி ,ீ , ே, etc.) """

        # TODO: create a test case for this

        # get the list of combination endings, remove the empty unicode string and convert to a tuple
        return tuple(TamilLetter.COMBINATION_ENDINGS)

    @staticmethod
    def get_pulli():
        """ Returns the pulli codepoint ('்') """

        # TODO: Create a test case for this

        return TamilLetter.PULLI
