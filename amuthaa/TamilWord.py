# -*- coding: utf-8 -*-
#!/usr/bin/python

import string

# import TamilLetter class
from amuthaa import TamilLetter


class TamilWord(object):
    """ Module to handle the processing of Tamil words """

    def __init__(self, word=u''):
        """ Constructor for TamilWord class. Takes a unicode string
        composed of Tamil characters as an optional input.
        """

        self._word = u''
        self._syllables = []
        self._letters = []

        # if word is entered, call the word property's setter
        # (which generates the syllables and letters lists)
        if word:
            self.word = word

    def __getitem__(self, index):
        """ Read the letter at the given position in the letters list """

        return self._letters[index]

    def __setitem__(self, index, value):
        """ Modify a member at the given position in the letters list """

        self._letters[index] = value

        # re-calculate word and syllables
        self.word = ''.join(self._letters)

    def __delitem__(self, index):
        """ Delete the letter at the given position in the letters list """

        del self._letters[index]

        # re-calculate word and syllables
        self.word = ''.join(self._letters)

    def __len__(self):
        """ Overload length operator. Returns length of the 'letters' list """

        return len(self.letters)

    # TODO: overload __iter__(self)

    # TODO: overload __reversed__(self)

    # TODO: overload __contains__(self, item)

    def __add__(self, other):
        """ Overload the + operator by appending the word string in the other
        object to the end of the self object """

        other_word = u''

        if isinstance(other, TamilWord):
            other_word = other.word

        elif isinstance(str(other), string) or isinstance(other, unicode):
            other_word = other

        else:
            raise TypeError("Object must be a TamilWord, String, or unicode \
                object. Object is of type %s" % type(other))

        self.word += other_word

    def __iadd__(self, other):
        """ Overload the += operator """

        other_word = u''

        if isinstance(other, TamilWord):
            other_word = other.word

        elif isinstance(str(other), string) or isinstance(other, unicode):
            other_word = other

        self.word += other_word

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, word):

        # if valid word is entered, calculate syllables and letters

        if self.validate(word):
            self._word = word

            self._letters = self.split_letters(word)
            #self._syllables = self.split_syllables(self._letters)
            # TODO: Fix split_syllables. It is not working at the moment

        # if invalid word is entered, initialize to empty string
        else:
            self._word = u''

    @property
    def syllables(self):
        """ Returns a list containing the word's syllables """

        return self._syllables

    @property
    def letters(self):
        """ Returns a list containing the word's letters (split by grapheme)"""

        return self._letters

    def add_ending(self, ending=u''):
        """ Add an ending to the word, combining vowel-consonant
        pairs if necessary """

        # If ending begins with a vowel, the word must end with a consonant
        # and this consonant-vowel pair should be combined
        # If the word doesn't end with a consonant, raise a value error
        if TamilLetter.is_vowel(ending[0]):

            if TamilLetter.is_consonant(self.word[-1]):

                # replace the last letter of the word with the consonant-vowel
                # combination, then copy over the rest of the ending
                self.word[-1] = TamilLetter.get_combination(self.word[-1], \
                                                            ending[0])
                self.word += ending[1:]

            # Unless word ends with a consonant, ending cannot start with a vowel
            else:
                raise ValueError("""Invalid word-ending pair - ending
                    can only start with a vowel if word ends with consonant""")

        # In all other cases, simply add the ending to the word
        self.word += ending

    @staticmethod
    def validate(word=u''):
        """ Asserts that a given word is valid """

        # if input was a TamilWord object, extract out the word portion
        if isinstance(word, TamilWord):
            word = word.word

        # simple test: every element of string must be valid Tamil character

        for codepoint in word:
            TamilLetter.assert_valid_letter(codepoint)

        # TODO: implement method this more thoroughly
        # TODO: check for pulli or combination_ending at beginning of word

        return True

    @staticmethod
    def split_letters(word=u''):
        """ Returns the graphemes (i.e. the Tamil characters)
        in a given word as a list """

        # ensure that the word is a valid word
        TamilWord.validate(word)

        # list (which will be returned to user)
        letters = []

        # a tuple of all combination endings and of all அ combinations
        combination_endings = TamilLetter.get_combination_endings()
        a_combinations = TamilLetter.get_combination_column(u'அ').values()

        # loop through
        for codepoint in word:

            # if codepoint is an அ combination, a vowel, aytham or a space,
            # add it to the list
            if codepoint in a_combinations or \
                TamilLetter.is_whitespace(codepoint) or \
                TamilLetter.is_vowel(codepoint) or \
                TamilLetter.is_aytham(codepoint):

                letters.append(codepoint)

            # if codepoint is a combination ending or a pulli ('்'), add it
            # to the end of the previously-added codepoint
            elif codepoint in combination_endings or \
                codepoint == TamilLetter.get_pulli():

                # ensure that at least one character already exists
                if len(letters) > 0:
                    letters[-1] = letters[-1] + codepoint

                # otherwise raise an Error. However, validate_word()
                # should catch this
                else:
                    raise ValueError("""Unknown error: Combination ending %s
                    cannot be first character of a word""" % (codepoint))

            # if codepoint was neither a vowel, aytham, a pulli or a
            # combination ending, an unexpected error has occurred
            else:
                raise ValueError("""Unknown error: Codepoint \'%s\' in word %s
                    is neither a vowel, consonant, combination or aytham"""
                    % (codepoint, word))

        # TODO: Write extensive test cases for this

        return letters

    @staticmethod
    def print_letters(word=u'', delimiter="-"):
        """ Prints all the graphemes in a word, separated by a
        delimiter (default: "-") """

        for letter in TamilWord.get_letters(word):
            print letter, delimiter,

        # go to new line
        print

    @staticmethod
    def split_syllables(letters=[]):
        """ Returns the syllables in a given word as a list """

        # Generic algorithm:
        # Each vowel and combination is its own syllable. Consonants and
        # aytham get added to the end of the previous syllable

        # ensure that the word is a valid word
        TamilWord.validate(''.join(letters))

        # initialize empty list
        syllables = []

        # loop through letters in the word
        for letter in letters:

            # if letter is a vowel or combination, it gets its own syllable
            if TamilLetter.is_combination(letter) or \
                TamilLetter.is_vowel(letter):
                syllables.append(letter)

            # if codepoint is a consonant or aytham, add it to the end
            # of the previously-added codepoint
            elif TamilLetter.is_consonant(letter) or \
                TamilLetter.is_aytham(letter):

                # ensure that at least one character already exists
                if len(syllables) > 0:
                    syllables[-1] = syllables[-1] + letter

                # if the first letter is a consonant (probably b/c it' s a
                # loanword), add it to the beginning of the string
                else:
                    syllables.append(letter)

            # if codepoint was neither a vowel, aytham, a pulli or a
            # combination ending, an unexpected error has occurred
            else:
                raise Exception("""Unknown error: \'%s\' in word %s is neither
                 a vowel, consonant, combination or aytham"""
                 % (letter, ''.join(letters)))


        # TODO: Write extensive test cases for this
