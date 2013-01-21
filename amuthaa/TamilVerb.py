# -*- coding: utf-8 -*-
#!/usr/bin/python

from TamilLetter import TamilLetter
from TamilWord import TamilWord


class TamilVerb(TamilWord):

    def __init__(self, root=u'', infinitive=u'', conjunctive=u''):
        _classnum = None
        _root = root
        _infinitive = infinitive
        _conjunctive = conjunctive

    # Dictionary to map a pronoun with its respective suffix
    PROUNOUN_SUFFIXES = {
                         u'நான்': u'ஏன்',
                         u'நீ': u'ஆய்',
                         u'நீர்': u'ஈர்',
                         u'நீங்கள்': u'ஈர்கள்',
                         u'அவன்': u'ஆன்',
                         u'அவள்': u'ஆள்',
                         u'அவர்': u'ஆர்',
                         u'நாங்கள்': u'ஓம்',
                         u'நாம்': u'ஓம்',
                         u'அவர்கள்': u'ஆர்கள்',
                         u'அது': u'அது',
                         u'அவை': u'அன',
                         }

    @staticmethod
    def validate_class(noun_class=0):
        """ docstring """

        # TODO: implement method

        # TODO: implement method

    @staticmethod
    def conjugate(verb=u'', verbclass=0, tense='PRESENT'):
            """ docstring """

        # TODO: Implement method

        # TODO: Implement method
