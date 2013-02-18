# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest
import logging

from amuthaa.TamilLetter import TamilLetter
from amuthaa.TamilNoun import TamilNoun


logging.basicConfig(level=logging.DEBUG)


class TamilNounTest(unittest.TestCase):
    """
    A test class for the TamilNoun module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TamilNounTest))
    return suite


def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)


if __name__ == '__main__':
    main()
