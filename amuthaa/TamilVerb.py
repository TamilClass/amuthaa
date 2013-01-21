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

    @staticmethod
    def validate_class(noun_class=0):
        """ docstring """

        # TODO: implement method

    @staticmethod
    def conjugate(verb=u'', verbclass=0, tense='PRESENT'):
            """ docstring """

        # TODO: Implement method
