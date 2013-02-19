# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest
import logging

from amuthaa.TamilNoun import TamilNoun

import xlrd

logging.basicConfig(level=logging.DEBUG)


class TamilNounTest(unittest.TestCase):
    """
    A test class for the TamilNoun module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_class(self):
        """ Tests the get_class() method of the TamilNoun class

        Loops through words in Excel spreadsheet and ensures that the
        get_class() method returns the expected class number for each noun
        in the Excel file
        """

        # Load excel workbook and sheet
        filename = "TamilNounsByClass.xls"

        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)

        for rownum in range(1, sh.nrows):

            row = sh.row_values(rownum)

            noun = row[0]

            expected_class = int(row[1])
            received_class = int(TamilNoun.get_class(noun))

            print("Testing %s. Expecting class %s..."
                  % (noun, expected_class)),

            self.assertEquals(expected_class, received_class,
                              """For noun %s expected noun class %s.
                              Received noun class %s."""
                              % (noun, expected_class, received_class))

            print("pass")

    def test_split_letters(self):
        """ Tests the split_letters() method of the TamilNoun class

        Loops through words in Excel spreadsheet and ensures that the
        split_letters() method returns the expected list of letters_str
        for each noun in the Excel file
        """

        # Load excel workbook and sheet
        filename = "TamilNounsByClass.xls"

        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)

        for rownum in range(1, sh.nrows):

            row = sh.row_values(rownum)

            noun = row[0]

            letters_str = row[3]
            letters_str = letters_str.replace(" ", "")
            expected_letters = letters_str.split(",")
            received_letters = TamilNoun.split_letters(noun)

            print("Testing %s. Expecting letters %s..."
                  % (noun, letters_str)),

            self.assertEquals(expected_letters, received_letters,
                              """For noun %s expected %s.
                              Received %s."""
                              % (noun, expected_letters, received_letters))

            print("pass")

    def test_direct_object(self):
        """ Tests the direct_object property's getter method of the
        TamilNoun class.

        Loops through words in Excel spreadsheet and ensures that the
        method returns the expected direct object for each noun in
        the Excel file
        """

        # Load excel workbook and sheet
        filename = "TamilNounsByClass.xls"

        wb = xlrd.open_workbook(filename)
        sh = wb.sheet_by_index(0)

        for rownum in range(1, sh.nrows):

            row = sh.row_values(rownum)

            noun = TamilNoun(row[0])

            expected = row[2]
            received = noun.direct_object

            print("Testing %s. Expecting %s..."
                  % (noun.word, expected)),

            self.assertEquals(expected, received,
                              """For noun %s expected %s.
                              Received %s."""
                              % (noun.word, expected, received))

            print("pass")


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
