# -*- coding: utf-8 -*-
#!/usr/bin/python

from .TamilLetter import TamilLetter
from .TamilWord import TamilWord


class TamilVerb(TamilWord):

    def __init__(self, root='', infinitive='', conjunctive=''):
        _classnum = None
        _root = root
        _infinitive = infinitive
        _conjunctive = conjunctive

    # Dictionary to map a pronoun with its respective suffix
    PROUNOUN_SUFFIXES = {
                         'நான்': 'ஏன்',
                         'நீ': 'ஆய்',
                         'நீர்': 'ஈர்',
                         'நீங்கள்': 'ஈர்கள்',
                         'அவன்': 'ஆன்',
                         'அவள்': 'ஆள்',
                         'அவர்': 'ஆர்',
                         'நாங்கள்': 'ஓம்',
                         'நாம்': 'ஓம்',
                         'அவர்கள்': 'ஆர்கள்',
                         'அது': 'அது',
                         'அவை': 'அன',
                         }

    @staticmethod
    def validate_class(noun_class=0):
        """ docstring """

        # TODO: implement method

        # TODO: implement method

    @staticmethod
    def conjugate(verb='', verbclass=0, tense='PRESENT'):
            """ docstring """

        # TODO: Implement method

        # TODO: Implement method
