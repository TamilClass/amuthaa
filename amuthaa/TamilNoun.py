# -*- coding: utf-8 -*-
#!/usr/bin/python

from TamilLetter import TamilLetter
from TamilWord import TamilWord

# Suffix dictionary: maps suffix to வேற்றுமை type
SUFFIX = {
            u'ஐ': 1,
            u'ஆல்': 2,
            u'ஓடு': 2,
            u'உடன்': 2,
            u'கு': 4,
            u'இல்': 5,
            u'இன்': 5,
            u'ஐ விட': 5,
            # u' இனின்று': 5,  - commented this out. Never heard of it
            u'இலிருந்து': 5,
            u'அது': 6,
            u'ஆது': 6,
            u'அ': 6,
            u'உடைய': 6,
            u'இனுடைய': 6,
            u'இல்': 7,
            u'இடத்தில்': 7,
            u'மேல்': 7,
            u'இன்மேல்': 7,
            u'கீழ்': 7,
            u'இன்கீழ்': 7,
            u'உள்': 7,
            u'கு உள்': 7,
            u'உம்': 0,
            u'ஆ': 0,
            u'ஏ': 0,
            u'ஓ': 0
            }


class TamilNoun(TamilWord):

    def __init__(self, word=u''):

        TamilWord.__init__(self, word)

        self._noun_class = None

    @staticmethod
    def validate_class(noun_class=0):
        """ docstring """

        #TODO: implement method

    @staticmethod
    def get_class(word=u''):
        """ Returns the noun class for a given noun """

        ### See flowchart (docs/material/sendhil/noun_classes.png) for details

        # Convert 'word' from a unicode object to a TamilWord object
        word = TamilWord(word)

        ## For noun classes ending in a consonant:
        ## Ending in ம் -> class 1
        ## Ending in ல், ன், ய், ள், ண் AND has exactly two graphemes AND
        ##    first letter is kuril: class 2
        ## All other consonant-ending nouns -> class 3

        if TamilLetter.is_consonant(word[-1]):

            if word[-1] == u'ம்':
                return 1

            elif (word[-1] in (u'ல்', u'ன்', u'ய்', u'ள்', u'ண்') and
                len(word) == 2 and TamilLetter.is_kuril(word[0])):
                return 2

            else:
                return 3

        ## For noun classes not ending in a combination:
        ## TODO: What if a noun ends in Aytham? Is this possible?
        ## TODO: Ensure this is tested on single letter nouns (e.g. ஈ)
        ## Ends in இ, ஈ or ஐ -> class 4
        ## Ends in ஆ, ஏ, ஊ or ஓ -> class 5
        ## Has exactly two graphemes AND first letter is kuril -> class 6
        ## Ends in று and penultimate grapheme is not a consonant -> class 7
        ## Ends in டு and penultimate grapheme is not a consonant -> class 8
        ## TODO: Is it ok that rules assume the word is >= two graphemes long?
        ## All other cases: class 9

        else:

            _, ending_vowel = TamilLetter.split_combination(word[-1])

            if ending_vowel in (u'இ', u'ஈ', u'ஐ'):
                return 4

            elif ending_vowel in (u'ஆ', u'ஏ', u'ஊ', u'ஓ'):
                return 5

            elif len(word) == 2 and TamilLetter.is_kuril(word[0]):
                return 6

            elif word[-1] == u'று' and not TamilLetter.is_consonant(word[-2]):
                return 7

            elif word[-1] == u'டு' and not TamilLetter.is_consonant(word[-2]):
                return 8

            else:
                return 9

    @property
    def direct_object(self):
        """Returns the direct object of a given noun."""

        direct_object = TamilNoun(self.word)

        suffix = u"ஐ"

        ENDING_BY_CLASS = {1: u"த்த்",
                           2: self.word[-1],
                           3: self.word[-1],
                           4: u"ய்",
                           5: u"வ்",
                           6: u"வ்",
                           7: u"ட்ட்",
                           8: u"ற்ற்",
                           9: TamilLetter.get_combination(self.word[-1])[0]
                  }

        noun_class = TamilNoun.get_class(self.word)
        ending = TamilWord(ENDING_BY_CLASS[noun_class])

        if noun_class == 1:

            del direct_object[-1]

            direct_object.word += \
                (ending[0] + TamilLetter.get_combination(ending[-1], suffix))

        elif noun_class == 2:

            direct_object.word += \
                (TamilLetter.get_combination(ending[0], suffix))

        elif noun_class == 3:

            del direct_object[-1]

            direct_object.word += \
                (TamilLetter.get_combination(ending[0], suffix))

        elif noun_class == 4:

            direct_object.word += \
                (TamilLetter.get_combination(ending[0], suffix))

        elif noun_class == 5:

            direct_object.word += \
                (TamilLetter.get_combination(ending[0], suffix))

        elif noun_class == 6:

            direct_object.word += \
                (TamilLetter.get_combination(ending[0], suffix))

        elif noun_class == 7:

            del direct_object[-1]

            direct_object.word += \
                (ending[0] + TamilLetter.get_combination(ending[-1], suffix))

        elif noun_class == 8:

            del direct_object[-1]

            direct_object.word += \
                (ending[0] + TamilLetter.get_combination(ending[-1], suffix))

        elif noun_class == 9:

            del direct_object[-1]

            direct_object.word += \
                (TamilLetter.get_combination(ending[-1], suffix))



    @staticmethod
    def add_suffix(suffix=u''):
        """ docstring """
        pass
        #TODO: Implement method

    @staticmethod
    def get_plural(word=u''):
        """ docstring """

        #TODO: Implement method

    @staticmethod
    def get_root(word):
            """ docstring """

        #TODO: Implement method
