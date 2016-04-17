# -*- coding: utf-8 -*-
#!/usr/bin/python

# import amuthaa directory from ..

import sys
sys.path.append("..")
sys.path


import unittest
import logging

# import TamilLetter class

from amuthaa.TamilLetter import TamilLetter

logging.basicConfig(level=logging.DEBUG)

# a tuple dictionary that matches a consonant, vowel tuple to its combination
COMBINATIONS = {
                ('க்', 'அ'): 'க', ('க்', 'ஆ'): 'கா', ('க்', 'இ'): 'கி',
                ('க்', 'ஈ'): 'கீ', ('க்', 'உ'): 'கு', ('க்', 'ஊ'): 'கூ',
                ('க்', 'எ'): 'கெ', ('க்', 'ஏ'): 'கே', ('க்', 'ஐ'): 'கை',
                ('க்', 'ஒ'): 'கொ', ('க்', 'ஓ'): 'கோ', ('க்', 'ஔ'): 'கௌ',

                ('ங்', 'அ'): 'ங', ('ங்', 'ஆ'): 'ஙா', ('ங்', 'இ'): 'ஙி',
                ('ங்', 'ஈ'): 'ஙீ', ('ங்', 'உ'): 'ஙு', ('ங்', 'ஊ'): 'ஙூ',
                ('ங்', 'எ'): 'ஙெ', ('ங்', 'ஏ'): 'ஙே', ('ங்', 'ஐ'): 'ஙை',
                ('ங்', 'ஒ'): 'ஙொ', ('ங்', 'ஓ'): 'ஙோ', ('ங்', 'ஔ'): 'ஙௌ',

                ('ச்', 'அ'): 'ச', ('ச்', 'ஆ'): 'சா', ('ச்', 'இ'): 'சி',
                ('ச்', 'ஈ'): 'சீ', ('ச்', 'உ'): 'சு', ('ச்', 'ஊ'): 'சூ',
                ('ச்', 'எ'): 'செ', ('ச்', 'ஏ'): 'சே', ('ச்', 'ஐ'): 'சை',
                ('ச்', 'ஒ'): 'சொ', ('ச்', 'ஓ'): 'சோ', ('ச்', 'ஔ'): 'சௌ',

                ('ஞ்', 'அ'): 'ஞ', ('ஞ்', 'ஆ'): 'ஞா', ('ஞ்', 'இ'): 'ஞி',
                ('ஞ்', 'ஈ'): 'ஞீ', ('ஞ்', 'உ'): 'ஞு', ('ஞ்', 'ஊ'): 'ஞூ',
                ('ஞ்', 'எ'): 'ஞெ', ('ஞ்', 'ஏ'): 'ஞே', ('ஞ்', 'ஐ'): 'ஞை',
                ('ஞ்', 'ஒ'): 'ஞொ', ('ஞ்', 'ஓ'): 'ஞோ', ('ஞ்', 'ஔ'): 'ஞௌ',

                ('ட்', 'அ'): 'ட', ('ட்', 'ஆ'): 'டா', ('ட்', 'இ'): 'டி',
                ('ட்', 'ஈ'): 'டீ', ('ட்', 'உ'): 'டு', ('ட்', 'ஊ'): 'டூ',
                ('ட்', 'எ'): 'டெ', ('ட்', 'ஏ'): 'டே', ('ட்', 'ஐ'): 'டை',
                ('ட்', 'ஒ'): 'டொ', ('ட்', 'ஓ'): 'டோ', ('ட்', 'ஔ'): 'டௌ',

                ('ண்', 'அ'): 'ண', ('ண்', 'ஆ'): 'ணா', ('ண்', 'இ'): 'ணி',
                ('ண்', 'ஈ'): 'ணீ', ('ண்', 'உ'): 'ணு', ('ண்', 'ஊ'): 'ணூ',
                ('ண்', 'எ'): 'ணெ', ('ண்', 'ஏ'): 'ணே', ('ண்', 'ஐ'): 'ணை',
                ('ண்', 'ஒ'): 'ணொ', ('ண்', 'ஓ'): 'ணோ', ('ண்', 'ஔ'): 'ணௌ',

                ('த்', 'அ'): 'த', ('த்', 'ஆ'): 'தா', ('த்', 'இ'): 'தி',
                ('த்', 'ஈ'): 'தீ', ('த்', 'உ'): 'து', ('த்', 'ஊ'): 'தூ',
                ('த்', 'எ'): 'தெ', ('த்', 'ஏ'): 'தே', ('த்', 'ஐ'): 'தை',
                ('த்', 'ஒ'): 'தொ', ('த்', 'ஓ'): 'தோ', ('த்', 'ஔ'): 'தௌ',

                ('ந்', 'அ'): 'ந', ('ந்', 'ஆ'): 'நா', ('ந்', 'இ'): 'நி',
                ('ந்', 'ஈ'): 'நீ', ('ந்', 'உ'): 'நு', ('ந்', 'ஊ'): 'நூ',
                ('ந்', 'எ'): 'நெ', ('ந்', 'ஏ'): 'நே', ('ந்', 'ஐ'): 'நை',
                ('ந்', 'ஒ'): 'நொ', ('ந்', 'ஓ'): 'நோ', ('ந்', 'ஔ'): 'நௌ',

                ('ப்', 'அ'): 'ப', ('ப்', 'ஆ'): 'பா', ('ப்', 'இ'): 'பி',
                ('ப்', 'ஈ'): 'பீ', ('ப்', 'உ'): 'பு', ('ப்', 'ஊ'): 'பூ',
                ('ப்', 'எ'): 'பெ', ('ப்', 'ஏ'): 'பே', ('ப்', 'ஐ'): 'பை',
                ('ப்', 'ஒ'): 'பொ', ('ப்', 'ஓ'): 'போ', ('ப்', 'ஔ'): 'பௌ',

                ('ம்', 'அ'): 'ம', ('ம்', 'ஆ'): 'மா', ('ம்', 'இ'): 'மி',
                ('ம்', 'ஈ'): 'மீ', ('ம்', 'உ'): 'மு', ('ம்', 'ஊ'): 'மூ',
                ('ம்', 'எ'): 'மெ', ('ம்', 'ஏ'): 'மே', ('ம்', 'ஐ'): 'மை',
                ('ம்', 'ஒ'): 'மொ', ('ம்', 'ஓ'): 'மோ', ('ம்', 'ஔ'): 'மௌ',

                ('ய்', 'அ'): 'ய', ('ய்', 'ஆ'): 'யா', ('ய்', 'இ'): 'யி',
                ('ய்', 'ஈ'): 'யீ', ('ய்', 'உ'): 'யு', ('ய்', 'ஊ'): 'யூ',
                ('ய்', 'எ'): 'யெ', ('ய்', 'ஏ'): 'யே', ('ய்', 'ஐ'): 'யை',
                ('ய்', 'ஒ'): 'யொ', ('ய்', 'ஓ'): 'யோ', ('ய்', 'ஔ'): 'யௌ',

                ('ர்', 'அ'): 'ர', ('ர்', 'ஆ'): 'ரா', ('ர்', 'இ'): 'ரி',
                ('ர்', 'ஈ'): 'ரீ', ('ர்', 'உ'): 'ரு', ('ர்', 'ஊ'): 'ரூ',
                ('ர்', 'எ'): 'ரெ', ('ர்', 'ஏ'): 'ரே', ('ர்', 'ஐ'): 'ரை',
                ('ர்', 'ஒ'): 'ரொ', ('ர்', 'ஓ'): 'ரோ', ('ர்', 'ஔ'): 'ரௌ',

                ('ல்', 'அ'): 'ல', ('ல்', 'ஆ'): 'லா', ('ல்', 'இ'): 'லி',
                ('ல்', 'ஈ'): 'லீ', ('ல்', 'உ'): 'லு', ('ல்', 'ஊ'): 'லூ',
                ('ல்', 'எ'): 'லெ', ('ல்', 'ஏ'): 'லே', ('ல்', 'ஐ'): 'லை',
                ('ல்', 'ஒ'): 'லொ', ('ல்', 'ஓ'): 'லோ', ('ல்', 'ஔ'): 'லௌ',

                ('வ்', 'அ'): 'வ', ('வ்', 'ஆ'): 'வா', ('வ்', 'இ'): 'வி',
                ('வ்', 'ஈ'): 'வீ', ('வ்', 'உ'): 'வு', ('வ்', 'ஊ'): 'வூ',
                ('வ்', 'எ'): 'வெ', ('வ்', 'ஏ'): 'வே', ('வ்', 'ஐ'): 'வை',
                ('வ்', 'ஒ'): 'வொ', ('வ்', 'ஓ'): 'வோ', ('வ்', 'ஔ'): 'வௌ',

                ('ழ்', 'அ'): 'ழ', ('ழ்', 'ஆ'): 'ழா', ('ழ்', 'இ'): 'ழி',
                ('ழ்', 'ஈ'): 'ழீ', ('ழ்', 'உ'): 'ழு', ('ழ்', 'ஊ'): 'ழூ',
                ('ழ்', 'எ'): 'ழெ', ('ழ்', 'ஏ'): 'ழே', ('ழ்', 'ஐ'): 'ழை',
                ('ழ்', 'ஒ'): 'ழொ', ('ழ்', 'ஓ'): 'ழோ', ('ழ்', 'ஔ'): 'ழௌ',

                ('ள்', 'அ'): 'ள', ('ள்', 'ஆ'): 'ளா', ('ள்', 'இ'): 'ளி',
                ('ள்', 'ஈ'): 'ளீ', ('ள்', 'உ'): 'ளு', ('ள்', 'ஊ'): 'ளூ',
                ('ள்', 'எ'): 'ளெ', ('ள்', 'ஏ'): 'ளே', ('ள்', 'ஐ'): 'ளை',
                ('ள்', 'ஒ'): 'ளொ', ('ள்', 'ஓ'): 'ளோ', ('ள்', 'ஔ'): 'ளௌ',

                ('ற்', 'அ'): 'ற', ('ற்', 'ஆ'): 'றா', ('ற்', 'இ'): 'றி',
                ('ற்', 'ஈ'): 'றீ', ('ற்', 'உ'): 'று', ('ற்', 'ஊ'): 'றூ',
                ('ற்', 'எ'): 'றெ', ('ற்', 'ஏ'): 'றே', ('ற்', 'ஐ'): 'றை',
                ('ற்', 'ஒ'): 'றொ', ('ற்', 'ஓ'): 'றோ', ('ற்', 'ஔ'): 'றௌ',

                ('ன்', 'அ'): 'ன', ('ன்', 'ஆ'): 'னா', ('ன்', 'இ'): 'னி',
                ('ன்', 'ஈ'): 'னீ', ('ன்', 'உ'): 'னு', ('ன்', 'ஊ'): 'னூ',
                ('ன்', 'எ'): 'னெ', ('ன்', 'ஏ'): 'னே', ('ன்', 'ஐ'): 'னை',
                ('ன்', 'ஒ'): 'னொ', ('ன்', 'ஓ'): 'னோ', ('ன்', 'ஔ'): 'னௌ',

                ('ஜ்', 'அ'): 'ஜ', ('ஜ்', 'ஆ'): 'ஜா', ('ஜ்', 'இ'): 'ஜி',
                ('ஜ்', 'ஈ'): 'ஜீ', ('ஜ்', 'உ'): 'ஜு', ('ஜ்', 'ஊ'): 'ஜூ',
                ('ஜ்', 'எ'): 'ஜெ', ('ஜ்', 'ஏ'): 'ஜே', ('ஜ்', 'ஐ'): 'ஜை',
                ('ஜ்', 'ஒ'): 'ஜொ', ('ஜ்', 'ஓ'): 'ஜோ', ('ஜ்', 'ஔ'): 'ஜௌ',

                ('ஷ்', 'அ'): 'ஷ', ('ஷ்', 'ஆ'): 'ஷா', ('ஷ்', 'இ'): 'ஷி',
                ('ஷ்', 'ஈ'): 'ஷீ', ('ஷ்', 'உ'): 'ஷு', ('ஷ்', 'ஊ'): 'ஷூ',
                ('ஷ்', 'எ'): 'ஷெ', ('ஷ்', 'ஏ'): 'ஷே', ('ஷ்', 'ஐ'): 'ஷை',
                ('ஷ்', 'ஒ'): 'ஷொ', ('ஷ்', 'ஓ'): 'ஷோ', ('ஷ்', 'ஔ'): 'ஷௌ',

                ('ஸ்', 'அ'): 'ஸ', ('ஸ்', 'ஆ'): 'ஸா', ('ஸ்', 'இ'): 'ஸி',
                ('ஸ்', 'ஈ'): 'ஸீ', ('ஸ்', 'உ'): 'ஸு', ('ஸ்', 'ஊ'): 'ஸூ',
                ('ஸ்', 'எ'): 'ஸெ', ('ஸ்', 'ஏ'): 'ஸே', ('ஸ்', 'ஐ'): 'ஸை',
                ('ஸ்', 'ஒ'): 'ஸொ', ('ஸ்', 'ஓ'): 'ஸோ', ('ஸ்', 'ஔ'): 'ஸௌ',

                ('ஹ்', 'அ'): 'ஹ', ('ஹ்', 'ஆ'): 'ஹா', ('ஹ்', 'இ'): 'ஹி',
                ('ஹ்', 'ஈ'): 'ஹீ', ('ஹ்', 'உ'): 'ஹு', ('ஹ்', 'ஊ'): 'ஹூ',
                ('ஹ்', 'எ'): 'ஹெ', ('ஹ்', 'ஏ'): 'ஹே', ('ஹ்', 'ஐ'): 'ஹை',
                ('ஹ்', 'ஒ'): 'ஹொ', ('ஹ்', 'ஓ'): 'ஹோ', ('ஹ்', 'ஔ'): 'ஹௌ',
                }

COMBINATIONS_BY_CONSONANT = {
                             'க்': { 'அ': 'க', 'ஆ': 'கா', 'இ': 'கி', 'ஈ': 'கீ',
                                      'உ': 'கு', 'ஊ': 'கூ', 'எ': 'கெ', 'ஏ': 'கே',
                                      'ஐ': 'கை', 'ஒ': 'கொ', 'ஓ': 'கோ', 'ஔ': 'கௌ'
                                      },
                             'ங்': {'அ': 'ங', 'ஆ': 'ஙா', 'இ': 'ஙி', 'ஈ':
                                      'ஙீ', 'உ': 'ஙு', 'ஊ': 'ஙூ', 'எ': 'ஙெ', 'ஏ': 'ஙே',
                                      'ஐ': 'ஙை', 'ஒ': 'ஙொ', 'ஓ': 'ஙோ', 'ஔ': 'ஙௌ'
                                      },
                             'ச்': { 'அ': 'ச', 'ஆ': 'சா', 'இ': 'சி', 'ஈ': 'சீ',
                                      'உ': 'சு', 'ஊ': 'சூ', 'எ': 'செ', 'ஏ': 'சே',
                                      'ஐ': 'சை', 'ஒ': 'சொ', 'ஓ': 'சோ', 'ஔ': 'சௌ'
                                      },
                             'ஞ்': { 'அ': 'ஞ', 'ஆ': 'ஞா', 'இ': 'ஞி', 'ஈ': 'ஞீ',
                                      'உ': 'ஞு', 'ஊ': 'ஞூ', 'எ': 'ஞெ', 'ஏ': 'ஞே',
                                      'ஐ': 'ஞை', 'ஒ': 'ஞொ', 'ஓ': 'ஞோ', 'ஔ': 'ஞௌ'
                                      },
                             'ட்': { 'அ': 'ட', 'ஆ': 'டா', 'இ': 'டி', 'ஈ': 'டீ',
                                      'உ': 'டு', 'ஊ': 'டூ', 'எ': 'டெ', 'ஏ': 'டே',
                                      'ஐ': 'டை', 'ஒ': 'டொ', 'ஓ': 'டோ', 'ஔ': 'டௌ'
                                      },
                             'ண்': { 'அ': 'ண', 'ஆ': 'ணா', 'இ': 'ணி', 'ஈ': 'ணீ',
                                      'உ': 'ணு', 'ஊ': 'ணூ', 'எ': 'ணெ', 'ஏ': 'ணே',
                                      'ஐ': 'ணை', 'ஒ': 'ணொ', 'ஓ': 'ணோ', 'ஔ': 'ணௌ'
                                      },
                             'த்': { 'அ': 'த', 'ஆ': 'தா', 'இ': 'தி', 'ஈ': 'தீ',
                                      'உ': 'து', 'ஊ': 'தூ', 'எ': 'தெ', 'ஏ': 'தே',
                                      'ஐ': 'தை', 'ஒ': 'தொ', 'ஓ': 'தோ', 'ஔ': 'தௌ'
                                      },
                             'ந்': { 'அ': 'ந', 'ஆ': 'நா', 'இ': 'நி', 'ஈ': 'நீ',
                                      'உ': 'நு', 'ஊ': 'நூ', 'எ': 'நெ', 'ஏ': 'நே',
                                      'ஐ': 'நை', 'ஒ': 'நொ', 'ஓ': 'நோ', 'ஔ': 'நௌ'
                                      },
                             'ப்': { 'அ': 'ப', 'ஆ': 'பா', 'இ': 'பி', 'ஈ': 'பீ',
                                      'உ': 'பு', 'ஊ': 'பூ', 'எ': 'பெ', 'ஏ': 'பே',
                                      'ஐ': 'பை', 'ஒ': 'பொ', 'ஓ': 'போ', 'ஔ': 'பௌ'
                                      },
                             'ம்': { 'அ': 'ம', 'ஆ': 'மா', 'இ': 'மி', 'ஈ': 'மீ',
                                      'உ': 'மு', 'ஊ': 'மூ', 'எ': 'மெ', 'ஏ': 'மே',
                                      'ஐ': 'மை', 'ஒ': 'மொ', 'ஓ': 'மோ', 'ஔ': 'மௌ'
                                      },
                             'ய்': { 'அ': 'ய', 'ஆ': 'யா', 'இ': 'யி', 'ஈ': 'யீ',
                                      'உ': 'யு', 'ஊ': 'யூ', 'எ': 'யெ', 'ஏ': 'யே',
                                      'ஐ': 'யை', 'ஒ': 'யொ', 'ஓ': 'யோ', 'ஔ': 'யௌ'
                                      },
                             'ர்': { 'அ': 'ர', 'ஆ': 'ரா', 'இ': 'ரி', 'ஈ': 'ரீ',
                                      'உ': 'ரு', 'ஊ': 'ரூ', 'எ': 'ரெ', 'ஏ': 'ரே',
                                      'ஐ': 'ரை', 'ஒ': 'ரொ', 'ஓ': 'ரோ', 'ஔ': 'ரௌ'
                                      },
                             'ல்': { 'அ': 'ல', 'ஆ': 'லா', 'இ': 'லி', 'ஈ': 'லீ',
                                      'உ': 'லு', 'ஊ': 'லூ', 'எ': 'லெ', 'ஏ': 'லே',
                                      'ஐ': 'லை', 'ஒ': 'லொ', 'ஓ': 'லோ', 'ஔ': 'லௌ'
                                      },
                             'வ்': { 'அ': 'வ', 'ஆ': 'வா', 'இ': 'வி', 'ஈ': 'வீ',
                                      'உ': 'வு', 'ஊ': 'வூ', 'எ': 'வெ', 'ஏ': 'வே',
                                      'ஐ': 'வை', 'ஒ': 'வொ', 'ஓ': 'வோ', 'ஔ': 'வௌ'
                                      },
                             'ழ்': { 'அ': 'ழ', 'ஆ': 'ழா', 'இ': 'ழி', 'ஈ': 'ழீ',
                                      'உ': 'ழு', 'ஊ': 'ழூ', 'எ': 'ழெ', 'ஏ': 'ழே',
                                      'ஐ': 'ழை', 'ஒ': 'ழொ', 'ஓ': 'ழோ', 'ஔ': 'ழௌ'
                                      },
                             'ள்': { 'அ': 'ள', 'ஆ': 'ளா', 'இ': 'ளி', 'ஈ': 'ளீ',
                                      'உ': 'ளு', 'ஊ': 'ளூ', 'எ': 'ளெ', 'ஏ': 'ளே',
                                      'ஐ': 'ளை', 'ஒ': 'ளொ', 'ஓ': 'ளோ', 'ஔ': 'ளௌ'
                                      },
                             'ற்': { 'அ': 'ற', 'ஆ': 'றா', 'இ': 'றி', 'ஈ': 'றீ',
                                      'உ': 'று', 'ஊ': 'றூ', 'எ': 'றெ', 'ஏ': 'றே',
                                      'ஐ': 'றை', 'ஒ': 'றொ', 'ஓ': 'றோ', 'ஔ': 'றௌ'
                                      },
                             'ன்': { 'அ': 'ன', 'ஆ': 'னா', 'இ': 'னி', 'ஈ': 'னீ',
                                      'உ': 'னு', 'ஊ': 'னூ', 'எ': 'னெ', 'ஏ': 'னே',
                                      'ஐ': 'னை', 'ஒ': 'னொ', 'ஓ': 'னோ', 'ஔ': 'னௌ'
                                      },
                             'ஜ்': { 'அ': 'ஜ', 'ஆ': 'ஜா', 'இ': 'ஜி', 'ஈ': 'ஜீ',
                                      'உ': 'ஜு', 'ஊ': 'ஜூ', 'எ': 'ஜெ', 'ஏ': 'ஜே',
                                      'ஐ': 'ஜை', 'ஒ': 'ஜொ', 'ஓ': 'ஜோ', 'ஔ': 'ஜௌ'
                                      },
                             'ஸ்': { 'அ': 'ஸ', 'ஆ': 'ஸா', 'இ': 'ஸி', 'ஈ': 'ஸீ',
                                      'உ': 'ஸு', 'ஊ': 'ஸூ', 'எ': 'ஸெ', 'ஏ': 'ஸே',
                                      'ஐ': 'ஸை', 'ஒ': 'ஸொ', 'ஓ': 'ஸோ', 'ஔ': 'ஸௌ'
                                      },
                             'ஷ்': { 'அ': 'ஷ', 'ஆ': 'ஷா', 'இ': 'ஷி', 'ஈ': 'ஷீ',
                                      'உ': 'ஷு', 'ஊ': 'ஷூ', 'எ': 'ஷெ', 'ஏ': 'ஷே',
                                      'ஐ': 'ஷை', 'ஒ': 'ஷொ', 'ஓ': 'ஷோ', 'ஔ': 'ஷௌ'
                                      },
                             'ஹ்': { 'அ': 'ஹ', 'ஆ': 'ஹா', 'இ': 'ஹி', 'ஈ': 'ஹீ',
                                      'உ': 'ஹு', 'ஊ': 'ஹூ', 'எ': 'ஹெ', 'ஏ': 'ஹே',
                                      'ஐ': 'ஹை', 'ஒ': 'ஹொ', 'ஓ': 'ஹோ', 'ஔ': 'ஹௌ'
                                      }
                             }


COMBINATIONS_BY_VOWEL = {
                         'அ': {
                                 'க்': 'க', 'ங்': 'ங', 'ச்': 'ச', 'ஞ்': 'ஞ', 'ட்': 'ட', 'ண்': 'ண',
                                 'த்': 'த', 'ந்': 'ந', 'ப்': 'ப', 'ம்': 'ம', 'ய்': 'ய', 'ர்': 'ர',
                                 'ல்': 'ல', 'வ்': 'வ', 'ழ்': 'ழ', 'ள்': 'ள', 'ற்': 'ற', 'ன்': 'ன',
                                 'ஜ்': 'ஜ', 'ஷ்': 'ஷ', 'ஸ்': 'ஸ', 'ஹ்': 'ஹ'
                                 },
                         'ஆ': {
                                 'க்': 'கா', 'ங்': 'ஙா', 'ச்': 'சா', 'ஞ்': 'ஞா', 'ட்': 'டா', 'ண்': 'ணா',
                                 'த்': 'தா', 'ந்': 'நா', 'ப்': 'பா', 'ம்': 'மா', 'ய்': 'யா', 'ர்': 'ரா',
                                 'ல்': 'லா', 'வ்': 'வா', 'ழ்': 'ழா', 'ள்': 'ளா', 'ற்': 'றா', 'ன்': 'னா',
                                 'ஜ்': 'ஜா', 'ஷ்': 'ஷா', 'ஸ்': 'ஸா', 'ஹ்': 'ஹா'
                                 },
                         'இ': {
                                 'க்': 'கி', 'ங்': 'ஙி', 'ச்': 'சி', 'ஞ்': 'ஞி', 'ட்': 'டி', 'ண்': 'ணி',
                                 'த்': 'தி', 'ந்': 'நி', 'ப்': 'பி', 'ம்': 'மி', 'ய்': 'யி', 'ர்': 'ரி',
                                 'ல்': 'லி', 'வ்': 'வி', 'ழ்': 'ழி', 'ள்': 'ளி', 'ற்': 'றி', 'ன்': 'னி',
                                 'ஜ்': 'ஜி', 'ஷ்': 'ஷி', 'ஸ்': 'ஸி', 'ஹ்': 'ஹி'
                                 },
                         'ஈ': {
                                 'க்': 'கீ', 'ங்': 'ஙீ', 'ச்': 'சீ', 'ஞ்': 'ஞீ', 'ட்': 'டீ', 'ண்': 'ணீ',
                                 'த்': 'தீ', 'ந்': 'நீ', 'ப்': 'பீ', 'ம்': 'மீ', 'ய்': 'யீ', 'ர்': 'ரீ',
                                 'ல்': 'லீ', 'வ்': 'வீ', 'ழ்': 'ழீ', 'ள்': 'ளீ', 'ற்': 'றீ', 'ன்': 'னீ',
                                 'ஜ்': 'ஜீ', 'ஷ்': 'ஷீ', 'ஸ்': 'ஸீ', 'ஹ்': 'ஹீ'
                                 },
                         'உ': {
                                 'க்': 'கு', 'ங்': 'ஙு', 'ச்': 'சு', 'ஞ்': 'ஞு', 'ட்': 'டு', 'ண்': 'ணு',
                                 'த்': 'து', 'ந்': 'நு', 'ப்': 'பு', 'ம்': 'மு', 'ய்': 'யு', 'ர்': 'ரு',
                                 'ல்': 'லு', 'வ்': 'வு', 'ழ்': 'ழு', 'ள்': 'ளு', 'ற்': 'று', 'ன்': 'னு',
                                 'ஜ்': 'ஜு', 'ஷ்': 'ஷு', 'ஸ்': 'ஸு', 'ஹ்': 'ஹு'
                                 },
                         'ஊ': {
                                 'க்': 'கூ', 'ங்': 'ஙூ', 'ச்': 'சூ', 'ஞ்': 'ஞூ', 'ட்': 'டூ', 'ண்': 'ணூ',
                                 'த்': 'தூ', 'ந்': 'நூ', 'ப்': 'பூ', 'ம்': 'மூ', 'ய்': 'யூ', 'ர்': 'ரூ',
                                 'ல்': 'லூ', 'வ்': 'வூ', 'ழ்': 'ழூ', 'ள்': 'ளூ', 'ற்': 'றூ', 'ன்': 'னூ',
                                 'ஜ்': 'ஜூ', 'ஷ்': 'ஷூ', 'ஸ்': 'ஸூ', 'ஹ்': 'ஹூ'
                                 },
                         'எ': {
                                 'க்': 'கெ', 'ங்': 'ஙெ', 'ச்': 'செ', 'ஞ்': 'ஞெ', 'ட்': 'டெ', 'ண்': 'ணெ',
                                 'த்': 'தெ', 'ந்': 'நெ', 'ப்': 'பெ', 'ம்': 'மெ', 'ய்': 'யெ', 'ர்': 'ரெ',
                                 'ல்': 'லெ', 'வ்': 'வெ', 'ழ்': 'ழெ', 'ள்': 'ளெ', 'ற்': 'றெ', 'ன்': 'னெ',
                                 'ஜ்': 'ஜெ', 'ஷ்': 'ஷெ', 'ஸ்': 'ஸெ', 'ஹ்': 'ஹெ'
                                 },
                         'ஏ': {
                                 'க்': 'கே', 'ங்': 'ஙே', 'ச்': 'சே', 'ஞ்': 'ஞே', 'ட்': 'டே', 'ண்': 'ணே',
                                 'த்': 'தே', 'ந்': 'நே', 'ப்': 'பே', 'ம்': 'மே', 'ய்': 'யே', 'ர்': 'ரே',
                                 'ல்': 'லே', 'வ்': 'வே', 'ழ்': 'ழே', 'ள்': 'ளே', 'ற்': 'றே', 'ன்': 'னே',
                                 'ஜ்': 'ஜே', 'ஷ்': 'ஷே', 'ஸ்': 'ஸே', 'ஹ்': 'ஹே'
                                 },
                         'ஐ': {
                                 'க்': 'கை', 'ங்': 'ஙை', 'ச்': 'சை', 'ஞ்': 'ஞை', 'ட்': 'டை', 'ண்': 'ணை',
                                 'த்': 'தை', 'ந்': 'நை', 'ப்': 'பை', 'ம்': 'மை', 'ய்': 'யை', 'ர்': 'ரை',
                                 'ல்': 'லை', 'வ்': 'வை', 'ழ்': 'ழை', 'ள்': 'ளை', 'ற்': 'றை', 'ன்': 'னை',
                                 'ஜ்': 'ஜை', 'ஷ்': 'ஷை', 'ஸ்': 'ஸை', 'ஹ்': 'ஹை'
                                 },
                         'ஒ': {
                                 'க்': 'கொ', 'ங்': 'ஙொ', 'ச்': 'சொ', 'ஞ்': 'ஞொ', 'ட்': 'டொ', 'ண்': 'ணொ',
                                 'த்': 'தொ', 'ந்': 'நொ', 'ப்': 'பொ', 'ம்': 'மொ', 'ய்': 'யொ', 'ர்': 'ரொ',
                                 'ல்': 'லொ', 'வ்': 'வொ', 'ழ்': 'ழொ', 'ள்': 'ளொ', 'ற்': 'றொ', 'ன்': 'னொ',
                                 'ஜ்': 'ஜொ', 'ஷ்': 'ஷொ', 'ஸ்': 'ஸொ', 'ஹ்': 'ஹொ'
                                 },
                         'ஓ': {
                                 'க்': 'கோ', 'ங்': 'ஙோ', 'ச்': 'சோ', 'ஞ்': 'ஞோ', 'ட்': 'டோ', 'ண்': 'ணோ',
                                 'த்': 'தோ', 'ந்': 'நோ', 'ப்': 'போ', 'ம்': 'மோ', 'ய்': 'யோ', 'ர்': 'ரோ',
                                 'ல்': 'லோ', 'வ்': 'வோ', 'ழ்': 'ழோ', 'ள்': 'ளோ', 'ற்': 'றோ', 'ன்': 'னோ',
                                 'ஜ்': 'ஜோ', 'ஷ்': 'ஷோ', 'ஸ்': 'ஸோ', 'ஹ்': 'ஹோ'
                                 },
                         'ஔ': {
                                 'க்': 'கௌ', 'ங்': 'ஙௌ', 'ச்': 'சௌ', 'ஞ்': 'ஞௌ', 'ட்': 'டௌ', 'ண்': 'ணௌ',
                                 'த்': 'தௌ', 'ந்': 'நௌ', 'ப்': 'பௌ', 'ம்': 'மௌ', 'ய்': 'யௌ', 'ர்': 'ரௌ',
                                 'ல்': 'லௌ', 'வ்': 'வௌ', 'ழ்': 'ழௌ', 'ள்': 'ளௌ', 'ற்': 'றௌ', 'ன்': 'னௌ',
                                 'ஜ்': 'ஜௌ', 'ஷ்': 'ஷௌ', 'ஸ்': 'ஸௌ', 'ஹ்': 'ஹௌ'
                                 }
                         }


## Other tuples used for testing

COMBINATION_ENDINGS_TUPLE  = ('\u0BBE', # ஆ -> ா
                             '\u0BBF', # இ -> ி
                            '\u0BC0', # ஈ -> ீ
                            '\u0BC1', # உ -> ு
                            '\u0BC2',  # ஊ -> ூ
                            '\u0BC6', # எ -> ெ
                            '\u0BC7', # ஏ -> ே
                            '\u0BC8', # ஐ -> ை
                            '\u0BCA', # ஒ -> ொ
                            '\u0BCB', # ஓ -> ோ
                            '\u0BCC' # ஔ -> ௌ
                            )
PULLI =  '்'
AYTHAM  = 'ஃ'

VALLINAM_CONSONANTS = ('க்', 'ச்', 'ட்', 'த்', 'ப்', 'ற்')
MELLINAM_CONSONANTS = ('ங்', 'ஞ்', 'ண்', 'ந்', 'ம்', 'ன்')
IDAIYINAM_CONSONANTS = ('ய்','ர்', 'ல்', 'வ்', 'ழ்', 'ள்')
GRANTHA_CONSONANTS = ('ஜ்', 'ஷ்', 'ஸ்', 'ஹ்') # removed support for 'க்ஷ்' temporarily and ஶ் permanently

KURIL_VOWELS = ('அ', 'இ', 'உ', 'எ', 'ஒ')
NEDIL_VOWELS = ('ஆ', 'ஈ', 'ஊ', 'ஏ', 'ஐ', 'ஓ', 'ஔ')

A_COMBINATIONS = ('அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ',  'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ')


class TamilLetterTest(unittest.TestCase):
    """
    A test class for the TamilLetter module
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass


    ## Test is_aytham() on aytham, vowels, consonants and combinations

    def testIsAytham_Aytham(self):
        """is_aytham should return True for aytham"""

        print("Testing TamilLetter.is_aytham() with aytham - expecting True", end=' ')

        self.assertTrue(TamilLetter.is_aytham('ஃ'))

        print(".... pass")

    def testIsAytham_Vowels(self):
        """is_aytham should return False for all vowels"""

        print("Testing TamilLetter.is_aytham() with vowels - expecting True", end=' ')

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_aytham(vowel))

        print(".... pass")

    def testIsAytham_Consonants(self):
        """is_aytham should return False for all consonants"""

        print("Testing TamilLetter.is_aytham() with consonants - expecting False", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_aytham(consonant))

        print(".... pass")

    def testIsAytham_Combinations(self):
        """is_aytham should return False for all combinations"""

        print("Testing TamilLetter.is_aytham() with combinations - expecting False", end=' ')

        for combination in list(COMBINATIONS.values()):

            self.assertFalse(TamilLetter.is_aytham(combination))

        print(".... pass")


    ## Test is_vowel() with aytham, vowels, consonants and combinations

    def testIsVowel_Aytham(self):
        """is_vowel should return True for aytham"""

        print("Testing TamilLetter.is_vowel() with aytham - expecting False", end=' ')

        self.assertFalse(TamilLetter.is_vowel(TamilLetter.get_aytham()))

        print(".... pass")

    def testIsVowel_Vowels(self):
        """is_vowel should return True for all vowels"""

        print("Testing TamilLetter.is_vowel() with vowels - expecting True", end=' ')

        for vowel in TamilLetter.get_vowels():

            self.assertTrue(TamilLetter.is_vowel(vowel))

        print(".... pass")

    def testIsVowel_Consonants(self):
        """is_vowel should return False for all consonants"""

        print("Testing TamilLetter.is_vowel() with consonants - expecting False", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_vowel(consonant))

        print(".... pass")

    def testIsVowel_Combinations(self):
        """is_vowel should return False for all combinations"""

        print("Testing TamilLetter.is_vowel() with combinations - expecting False", end=' ')

        for combination in list(COMBINATIONS.values()):

            self.assertFalse(TamilLetter.is_vowel(combination))

        print(".... pass")


    ## Test is_consonant() with aytham, vowels, consonants and combinations

    def testIsConsonant_Aytham(self):
        """is_consonant should return False for aytham"""

        print("Testing TamilLetter.is_consonant() with aytham - expecting False", end=' ')

        self.assertFalse(TamilLetter.is_consonant(TamilLetter.get_aytham()))

        print(".... pass")

    def testIsConsonant_Vowels(self):
        """is_consonant should return False for all vowels"""

        print("Testing TamilLetter.is_consonant() with vowels - expecting False", end=' ')

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_consonant(vowel))

        print(".... pass ")

    def testIsConsonant_Consonants(self):
        """is_consonant should return True for all consonants"""

        print("Testing TamilLetter.is_consonant() with consonants - expecting True", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertTrue(TamilLetter.is_consonant(consonant))

        print(".... pass")

    def testIsConsonant_Combinations(self):
        """is_consonant should return False for all combinations"""

        print("Testing TamilLetter.is_consonant() with combinations - expecting False", end=' ')

        for combination in list(COMBINATIONS.values()):

            self.assertFalse(TamilLetter.is_consonant(combination))

        print(".... pass")



    ## Test is_combination() with aytham, vowels, consonants and combinations

    def testIsCombination_Aytham(self):
        """is_combination should return True for aytham"""

        print("Testing TamilLetter.is_combination() with aytham - expecting False", end=' ')

        self.assertFalse(TamilLetter.is_combination(TamilLetter.get_aytham()))

        print(".... pass")

    def testIsCombination_Vowels(self):
        """is_combination should return False for all vowels"""

        print("Testing TamilLetter.is_combination() with vowels - expecting False", end=' ')

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_combination(vowel))

        print(".... pass ")

    def testIsCombination_Consonants(self):
        """is_combination should return False for all consonants"""

        print("Testing TamilLetter.is_combination() with consonants - expecting True", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_combination(consonant))

        print(".... pass")

    def testIsCombination_Combinations(self):
        """is_combination should return True for all combinations"""

        print("Testing TamilLetter.is_combination() with combinations - expecting False", end=' ')

        for combination in list(COMBINATIONS.values()):

            self.assertTrue(TamilLetter.is_combination(combination))

        print(".... pass")


## Test get_script_name()

    def testGetScriptName_Tamil(self):
        """ get_script_name() should return the name of the script that the unicode character is encoded in """

        print("Testing TamilLetter.get_script_name() with Tamil letters", end=' ')

        tamil_letters = tuple(TamilLetter.get_vowels())+tuple(TamilLetter.get_consonants())+tuple(COMBINATIONS.values())

        # Go through each Tamil letter
        for letter in tamil_letters:

            # format in title case
            result_script_name = TamilLetter.get_script_name(letter).title()
            script_name = 'TAMIL'.title()


            # check for equality
            self.assertEqual(script_name, result_script_name, "Error on letter \'%s\' from script \'%s\'. Function returned \'%s\'" %(letter, script_name, result_script_name))

        print(".... pass")


    def testGetScriptName_otherLanguages(self):
        """ get_script_name() should return the name of the script that the unicode character is encoded in """

        print("Testing TamilLetter.get_script_name() with letters from other scripts", end=' ')

        other_languages = {
                           'ඐ': 'SINHALA', 'එ': 'SINHALA', 'ඒ': 'SINHALA', 'ඓ': 'SINHALA',
                           'ඔ': 'SINHALA', 'ඕ': 'SINHALA', 'ඖ': 'SINHALA', 'ඳ': 'SINHALA',
                           'ප': 'SINHALA', 'ඵ': 'SINHALA', 'බ': 'SINHALA', 'භ': 'SINHALA',
                           'ම': 'SINHALA', 'ඹ': 'SINHALA', 'ය': 'SINHALA', 'ර': 'SINHALA',

                           'ഠ': 'MALAYALAM', 'ഡ': 'MALAYALAM', 'ഢ': 'MALAYALAM', 'ണ': 'MALAYALAM', 'ത': 'MALAYALAM',
                           'ഥ': 'MALAYALAM', 'ദ': 'MALAYALAM', 'ധ': 'MALAYALAM', 'ന': 'MALAYALAM',

                           'ಠ': 'KANNADA', 'ಡ': 'KANNADA', 'ಢ': 'KANNADA', 'ಣ': 'KANNADA', 'ತ': 'KANNADA',
                           'ಥ': 'KANNADA', 'ದ': 'KANNADA', 'ಧ': 'KANNADA', 'ನ': 'KANNADA',

                           'ఠ': 'TELUGU', 'డ': 'TELUGU', 'ఢ': 'TELUGU', 'ణ': 'TELUGU', 'త': 'TELUGU',
                           'థ': 'TELUGU', 'ద': 'TELUGU', 'ధ': 'TELUGU', 'న': 'TELUGU',

                           'ऐ': 'DEVANAGARI', 'ऑ': 'DEVANAGARI', 'ऒ': 'DEVANAGARI', 'ओ': 'DEVANAGARI',
                           'औ': 'DEVANAGARI', 'क': 'DEVANAGARI', 'ख': 'DEVANAGARI', 'ग': 'DEVANAGARI',
                           'घ': 'DEVANAGARI', 'ङ': 'DEVANAGARI', 'च': 'DEVANAGARI', 'छ': 'DEVANAGARI',
                           'ज': 'DEVANAGARI', 'झ': 'DEVANAGARI', 'ञ': 'DEVANAGARI', 'ट': 'DEVANAGARI',

                           'A': 'LATIN', 'B': 'LATIN', 'C': 'LATIN', 'D': 'LATIN', 'E': 'LATIN',
                           'F': 'LATIN', 'G': 'LATIN', 'H': 'LATIN', 'I': 'LATIN', 'J': 'LATIN',
                           'K': 'LATIN', 'L': 'LATIN', 'M': 'LATIN', 'N': 'LATIN', 'O': 'LATIN',

                           'ฐ': 'THAI', 'ฑ': 'THAI', 'ฒ': 'THAI', 'ณ': 'THAI', 'ด': 'THAI', 'ต': 'THAI',
                           'ถ': 'THAI', 'ท': 'THAI', 'ธ': 'THAI', 'น': 'THAI', 'บ': 'THAI',
                           'ป': 'THAI', 'ผ': 'THAI', 'ฝ': 'THAI', 'พ': 'THAI', 'ฟ': 'THAI',

                           '໐': 'LAO', '໑': 'LAO', '໒': 'LAO', '໓': 'LAO', '໔': 'LAO', '໕': 'LAO',
                           '໖': 'LAO', '໗': 'LAO', '໘': 'LAO', '໙': 'LAO', 'ດ': 'LAO', 'ຕ': 'LAO',
                           'ຖ': 'LAO', 'ທ': 'LAO', 'ນ': 'LAO', 'ບ': 'LAO', 'ປ': 'LAO', 'ຜ': 'LAO',
                           'ຝ': 'LAO', 'ພ': 'LAO', 'ຟ': 'LAO',

                           'ཐ': 'TIBETAN', 'ད': 'TIBETAN', 'དྷ': 'TIBETAN', 'ན': 'TIBETAN', 'པ': 'TIBETAN',
                           'ཕ': 'TIBETAN', 'བ': 'TIBETAN', 'བྷ': 'TIBETAN', 'མ': 'TIBETAN', 'ཙ': 'TIBETAN',
                           'ཚ': 'TIBETAN', 'ཛ': 'TIBETAN', 'ཛྷ': 'TIBETAN', 'ཝ': 'TIBETAN', 'ཞ': 'TIBETAN',
                           'ཟ': 'TIBETAN',

                           'ថ': 'KHMER', 'ទ': 'KHMER', 'ធ': 'KHMER', 'ន': 'KHMER', 'ប': 'KHMER',
                           'ផ': 'KHMER', 'ព': 'KHMER', 'ភ': 'KHMER', 'ម': 'KHMER', 'យ': 'KHMER',
                           'រ': 'KHMER', 'ល': 'KHMER', 'វ': 'KHMER', 'ឝ': 'KHMER', 'ឞ': 'KHMER',
                           'ស': 'KHMER',

                           'ᠠ': 'MONGOLIAN', 'ᠡ': 'MONGOLIAN', 'ᠢ': 'MONGOLIAN', 'ᠣ': 'MONGOLIAN',
                           'ᠤ': 'MONGOLIAN', 'ᠥ': 'MONGOLIAN', 'ᠦ': 'MONGOLIAN', 'ᠧ': 'MONGOLIAN',
                           'ᠨ': 'MONGOLIAN', 'ᠩ': 'MONGOLIAN', 'ᠪ': 'MONGOLIAN', 'ᠫ': 'MONGOLIAN',
                           'ᠬ': 'MONGOLIAN', 'ᠭ': 'MONGOLIAN', 'ᠮ': 'MONGOLIAN', 'ᠯ': 'MONGOLIAN'
        }

        # Go through each key, value pair from above
        for letter in other_languages:

            # format in title case
            result_script_name = TamilLetter.get_script_name(letter).title()
            script_name = other_languages[letter].title()

            # check for equality
            self.assertEqual(script_name, result_script_name, "Error on letter \'%s\' from script \'%s\'. Function returned \'%s\'" %(letter, script_name, result_script_name))

        print(".... pass")

    def testIsKuril_kuril(self):
        """ is_kuril() should return True for all kuril letters """

        print("Testing TamilLetter.is_kuril() with kuril letters", end=' ')

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return true
            self.assertTrue(TamilLetter.is_kuril(vowel), "Vowel \'%s\' returned False for is_kuril(). Should return True." %(vowel))

            # all combinations made from kuril vowels should also return true
            for combination in list(TamilLetter.get_combination_column(vowel).values()):
                self.assertTrue(TamilLetter.is_kuril(combination), "Combination \'%s\' returned False for is_kuril(). Should return True." %(combination))

        print(".... pass")

    def testIsKuril_nedil(self):
        """ is_kuril() should return False for all nedil letters """

        print("Testing TamilLetter.is_kuril() with nedil letters", end=' ')

        for vowel in NEDIL_VOWELS:

            # all the kuril vowels should return true
            self.assertFalse(TamilLetter.is_kuril(vowel), "Vowel \'%s\' returned True for is_kuril(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_kuril(combination), "Combination \'%s\' returned True for is_kuril(). Should return False." %(combination))

        print(".... pass")

    def testIsKuril_consonantsAndAytham(self):
        """ is_kuril() should return False for all consonants and for aytham """

        # first test consonants
        print("Testing TamilLetter.is_kuril() with consonants", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_kuril(consonant), "Consonant \'%s\' returned True for is_kuril(). Should return False.")

        print(".... pass")


        #now test aytham
        print("Testing TamilLetter.is_kuril() with aytham (ஃ)", end=' ')

        self.assertFalse(TamilLetter.is_kuril(AYTHAM), "Aytham (\'%s\') returned True for is_kuril(). Should return False." %AYTHAM)

        print(".... pass")


    def testIsNedil_kuril(self):
        """ is_nedil() should True for all kuril letters """

        print("Testing TamilLetter.is_nedil() with kuril letters", end=' ')

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return false
            self.assertFalse(TamilLetter.is_nedil(vowel), "Vowel \'%s\' returned True for is_nedil(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_nedil(combination), "Combination \'%s\' returned True for is_nedil(). Should return False." %(combination))

        print(".... pass")

    def testIsNedil_nedil(self):
        """ is_nedil() should True for all kuril letters """

        print("Testing TamilLetter.is_nedil() with kuril letters", end=' ')

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return false
            self.assertFalse(TamilLetter.is_nedil(vowel), "Vowel \'%s\' returned True for is_nedil(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_nedil(combination), "Combination \'%s\' returned True for is_nedil(). Should return False." %(combination))

        print(".... pass")

    def testIsNedil_consonantsAndAytham(self):
        """ is_nedil() should return False for all consonants and for aytham """

        # first test consonants
        print("Testing TamilLetter.is_nedil() with consonants", end=' ')

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_nedil(consonant), "Consonant \'%s\' returned True for is_nedil(). Should return False.")

        print(".... pass")


        #now test aytham
        print("Testing TamilLetter.is_nedil() with aytham (ஃ)", end=' ')

        self.assertFalse(TamilLetter.is_nedil(AYTHAM), "Aytham (\'%s\') returned True for is_nedil(). Should return False." %AYTHAM)

        print(".... pass")

    def testGetAytham(self):
        """ get_aytham() should return the Aytham (ஃ) character """

        print("Testing TamilLetter.get_aytham()", end=' ')

        expected = AYTHAM
        received = TamilLetter.get_aytham()

        self.assertEqual(expected, received, "Expected Aytham (\'%s\'), but received \'%s\' instead" %(expected, received))


        print(".... pass")

    def testGetVowels(self):
        """ get_vowels() should return a tuple of all the vowels """

        print("Testing TamilLetter.get_vowels()", end=' ')

        expected = KURIL_VOWELS + NEDIL_VOWELS
        received = TamilLetter.get_vowels()

        #ensure that both expected and received are tuples
        self.assertTrue(isinstance(expected,tuple), "\'%s\' should be a tuple, but is a %s" %(expected, type(expected)))
        self.assertTrue(isinstance(received,tuple), "\'%s\' should be a tuple, but is a %s" %(received, type(received)))

        #ensure that size of the two tuples is correct
        self.assertEqual(len(expected), len(received), "Vowel Tuple should have %s members" %len(expected))

        # compare as sets, to ignore order
        self.assertEqual(set(expected), set(received), "Expected tuple \'%s\' but received tuple \'%s\'" %(expected, received))

        print(".... pass")

    def testGetConsonants(self):
        """ get_consonants() should return a tuple of all the consonants """

        print("Testing TamilLetter.get_consonants()", end=' ')

        expected = VALLINAM_CONSONANTS + MELLINAM_CONSONANTS + IDAIYINAM_CONSONANTS + GRANTHA_CONSONANTS
        received = TamilLetter.get_consonants()

        #ensure that both expected and received are tuples
        self.assertTrue(isinstance(expected,tuple), "\'%s\' should be a tuple, but is a %s" %(expected, type(expected)))
        self.assertTrue(isinstance(received,tuple), "\'%s\' should be a tuple, but is a %s" %(received, type(received)))

        #ensure that size of the two tuples is correct
        self.assertEqual(len(expected), len(received), "Consonant tuple should have %s members" %len(received))

        # compare as sets, to ignore order
        self.assertEqual(set(expected), set(received), "Expected tuple \'%s\' but received tuple \'%s\'" %(expected, received))

        print(".... pass")

    def testGetCombination_validInput(self):
        """ get_combination() should return the result of combining a given consonant, vowel tuple """

        print("Testing TamilLetter.get_combination() with valid input (i.e. all possible with consonant, vowel) tuples", end=' ')

        # get tuple/list of consonants, vowels and combinations
        consonants = TamilLetter.get_consonants()
        vowels = TamilLetter.get_vowels()

        # loop through each consonant, vowel pair
        for consonant in consonants:

            for vowel in vowels:

                expected = COMBINATIONS[(consonant, vowel)]
                received = TamilLetter.get_combination(consonant, vowel)
                self.assertEqual(expected, received, "The combination \'%s\' should have resulted from consonant \'%s\' and vowel \'%s\'. \'%s\' was received" %(expected, vowel, consonant, received))


        print(".... pass")

    def testGetCombination_invalidInput(self):
        """ get_combination() should raise an exception if the input is not a consonant, vowel tuple """

        # get tuple/list of consonants, vowels and combinations
        consonants = TamilLetter.get_consonants()
        vowels = TamilLetter.get_vowels()
        combinations = list(COMBINATIONS.values())

        # Test every possible vowel, vowel tuple. Should raise a ValueError
        print("Testing TamilLetter.get_combination() with vowel, vowel tuples", end=' ')

        for vowel1 in vowels:

            for vowel2 in vowels:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(vowel1, vowel2)

        print(".... pass")


        # Test every possible consonant, consonant tuple. Should raise a ValueError
        print("Testing TamilLetter.get_combination() with consonant, consonant tuples", end=' ')

        for consonant1 in consonants:

            for consonant2 in consonants:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(consonant1, consonant2)

        print(".... pass")


        # Test every possible combination, combination tuple. Should raise a ValueError
        print("Testing TamilLetter.get_combination() with combination, combination tuples", end=' ')

        for combination1 in combinations:

            for combination2 in combinations:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(combination1, combination2)

        print(".... pass")


        # Test every possible vowel, consonant combination (get_combination) expects consonant, vowel input
        print("Testing TamilLetter.get_combination() with vowel, consonant tuples (get_combination() expects the consonant first, then the vowel)", end=' ')

        for vowel in vowels:

            for consonant in consonants:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(vowel, consonant)

        print(".... pass")


    def testSplitCombination(self):
        """ split_combination() should return the correct consonant, vowel tuple when given a letter """

        # Test for all combinations
        print("Testing TamilLetter.split_combination() with all combinations", end=' ')

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEqual(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print(".... pass")

        # Test for all consonants
        print("Testing TamilLetter.split_combination() with all consonants", end=' ')

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:

            expected = (consonant, '')
            received = TamilLetter.split_combination(consonant)

            self.assertEqual(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], consonant, received[0], received[1]))

        print(".... pass")

        # Test for all vowels
        print("Testing TamilLetter.split_combination() with all combinations", end=' ')

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEqual(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print(".... pass")

        # Test for aytham
        print("Testing TamilLetter.split_combination() with all combinations", end=' ')

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEqual(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print(".... pass")


    def testGetLetterType(self):
        """ get_letter_type() should return the letter type for a given letter (e.g. vowel, consonant, combination, aytham) """

        # Test for Aytham
        print("Testing TamilLetter.get_letter_type() with Aytham (ஃ)", end=' ')
        letter = AYTHAM
        expected = 'AYTHAM'
        received = TamilLetter.get_letter_type(letter)

        self.assertEqual(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, letter, received))

        print(".... pass")


        # Test for vowels
        print("Testing TamilLetter.get_letter_type() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()

        for vowel in vowels:
            expected = 'VOWEL'
            received = TamilLetter.get_letter_type(vowel)

            self.assertEqual(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, vowel, received))

        print(".... pass")

        # Test for consonants
        print("Testing TamilLetter.get_letter_type() with consonants", end=' ')

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:
            expected = 'CONSONANT'
            received = TamilLetter.get_letter_type(consonant)

            self.assertEqual(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, consonant, received))

        print(".... pass")


        # Test for combinations
        print("Testing TamilLetter.get_letter_type() with combinations", end=' ')

        combinations = list(COMBINATIONS.values())

        for combination in combinations:
            expected = 'COMBINATION'
            received = TamilLetter.get_letter_type(combination)

            self.assertEqual(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, combination, received))

        print(".... pass")


    def testGetVowelType_validInput(self):
        """ get_vowel_type() should return the vowel type (kuril or nedil) for all vowels and combination """

        # Test with kuril vowels
        print("Testing TamilLetter.get_vowel_type() with kuril vowels and their combinations", end=' ')

        for vowel in KURIL_VOWELS:

            expected = 'KURIL'

            # Test the vowel itself
            received = TamilLetter.get_vowel_type(vowel)
            self.assertEqual(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

            # Test for each combination involving a kuril vowel
            combinations = list(TamilLetter.get_combination_column(vowel).values())
            for combination in combinations:

                received = TamilLetter.get_vowel_type(combination)
                self.assertEqual(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

        print(".... pass")


        # Test with nedil vowels
        print("Testing TamilLetter.get_vowel_type() with nedil vowels and their combinations", end=' ')

        for vowel in NEDIL_VOWELS:

            expected = 'NEDIL'

            # Test the vowel itself
            received = TamilLetter.get_vowel_type(vowel)
            self.assertEqual(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

            # Test for each combination involving a kuril vowel
            combinations = list(TamilLetter.get_combination_column(vowel).values())
            for combination in combinations:

                received = TamilLetter.get_vowel_type(combination)
                self.assertEqual(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

        print(".... pass")


    def testGetVowelType_invalidInput(self):
        """ get_vowel_type() should raise a ValueError for Aytham and consonants """

        # Test with aytham
        print("Testing TamilLetter.get_vowel_type() with aytham", end=' ')

        letter = TamilLetter.get_aytham()
        with self.assertRaises(ValueError):
            _ = TamilLetter.get_vowel_type(letter)

        print(".... pass")


        # Test with all consonants
        print("Testing TamilLetter.get_vowel_type() with consonants", end=' ')

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_vowel_type(consonant)

        print(".... pass")


    def testIsVallinam_TrueCases(self):
        """ is_vallinam() should return True for all vallinam consonants """

        print("Testing TamilLetter.is_vallinam() with vallinam consonants", end=' ')

        for consonant in VALLINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_vallinam(consonant), "\'%s\' is a vallinam consonant, but is_vallinam() returned False" %consonant)

        print(".... pass")


    def testIsVallinam_FalseCases(self):
        """ is_vallinam() should return False for aytham and for all vowels, combinations and mellinam, idaiyinam and grantha consonants """

        # Test with aytham
        print("Testing TamilLetter.is_vallinam() with aytham", end=' ')

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_vallinam(letter), "\'%s\' is Aytham, but is_vallinam() returned True" %letter)

        print(".... pass")


        # Test with vowels
        print("Testing TamilLetter.is_vallinam() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_vallinam(vowel), "\'%s\' is a vowel, but is_vallinam() returned True" %vowel)

        print(".... pass")


        # Test with combinations
        print("Testing TamilLetter.is_vallinam() with combinations", end=' ')

        combinations = list(COMBINATIONS.values())
        for combination in combinations:

            self.assertFalse(TamilLetter.is_vallinam(combination), "\'%s\' is a combination, but is_vallinam() returned True" %combination)

        print(".... pass")


        # Test with mellinam consonants
        print("Testing TamilLetter.is_vallinam() with mellinam consonant", end=' ')

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_vallinam(consonant), "\'%s\' is a mellinam consonant, but is_vallinam() returned True" %consonant)

        print(".... pass")


        # Test with idaiyinam consonants
        print("Testing TamilLetter.is_vallinam() with idaiyinam consonant", end=' ')

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_vallinam(consonant), "\'%s\' is an idaiyinam consonant, but is_vallinam() returned True" %consonant)

        print(".... pass")


    def testIsMellinam_TrueCases(self):
        """ is_mellinam() should return True for all mellinam consonants """

        print("Testing TamilLetter.is_mellinam() with mellinam consonants", end=' ')

        for consonant in MELLINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_mellinam(consonant), "\'%s\' is a mellinam consonant, but is_mellinam() returned False" %consonant)

        print(".... pass")


    def testIsMellinam_FalseCases(self):
        """ is_mellinam() should return False for aytham and for all vowels, combinations and vallinam, idaiyinam and grantha consonants """

        # Test with aytham
        print("Testing TamilLetter.is_mellinam() with aytham", end=' ')

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_mellinam(letter), "\'%s\' is Aytham, but is_mellinam() returned True" %letter)

        print(".... pass")


        # Test with vowels
        print("Testing TamilLetter.is_mellinam() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_mellinam(vowel), "\'%s\' is a vowel, but is_mellinam() returned True" %vowel)

        print(".... pass")


        # Test with combinations
        print("Testing TamilLetter.is_mellinam() with combinations", end=' ')

        combinations = list(COMBINATIONS.values())
        for combination in combinations:

            self.assertFalse(TamilLetter.is_mellinam(combination), "\'%s\' is a combination, but is_mellinam() returned True" %combination)

        print(".... pass")


        # Test with mellinam consonants
        print("Testing TamilLetter.is_mellinam() with vallinam consonant", end=' ')

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is a vallinam consonant, but is_mellinam() returned True" %consonant)

        print(".... pass")


        # Test with idaiyinam consonants
        print("Testing TamilLetter.is_mellinam() with idaiyinam consonant", end=' ')

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is an idaiyinam consonant, but is_mellinam() returned True" %consonant)

        print(".... pass")

        # Test with grantha consonants
        print("Testing TamilLetter.is_mellinam() with grantha consonant", end=' ')

        for consonant in GRANTHA_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is a grantha consonant, but is_mellinam() returned True" %consonant)

        print(".... pass")


    def testIdaiyinam_TrueCases(self):
        """ is_GRANTHA() should return True for all idaiyinam consonants """

        print("Testing TamilLetter.is_idaiyinam() with idaiyinam consonants", end=' ')

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_idaiyinam(consonant), "\'%s\' is a idaiyinam consonant, but is_idaiyinam() returned False" %consonant)

        print(".... pass")


    def testIdaiyinam_FalseCases(self):
        """ is_idaiyinam() should return False for aytham and for all vowels, combinations and vallinam, mellinam and grantha consonants """

        # Test with aytham
        print("Testing TamilLetter.is_idaiyinam() with aytham", end=' ')

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_idaiyinam(letter), "\'%s\' is Aytham, but is_idaiyinam() returned True" %letter)

        print(".... pass")


        # Test with vowels
        print("Testing TamilLetter.is_idaiyinam() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_idaiyinam(vowel), "\'%s\' is a vowel, but is_idaiyinam() returned True" %vowel)

        print(".... pass")


        # Test with combinations
        print("Testing TamilLetter.is_idaiyinam() with combinations", end=' ')

        combinations = list(COMBINATIONS.values())
        for combination in combinations:

            self.assertFalse(TamilLetter.is_idaiyinam(combination), "\'%s\' is a combination, but is_idaiyinam() returned True" %combination)

        print(".... pass")


        # Test with idaiyinam consonants
        print("Testing TamilLetter.is_idaiyinam() with vallinam consonant", end=' ')

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is a vallinam consonant, but is_idaiyinam() returned True" %consonant)

        print(".... pass")


        # Test with idaiyinam consonants
        print("Testing TamilLetter.is_idaiyinam() with mellinam consonant", end=' ')

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is an mellinam consonant, but is_idaiyinam() returned True" %consonant)

        print(".... pass")

        # Test with grantha consonants
        print("Testing TamilLetter.is_idaiyinam() with grantha consonant", end=' ')

        for consonant in GRANTHA_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is an grantha consonant, but is_idaiyinam() returned True" %consonant)

        print(".... pass")


    def testIsGrantha_TrueCases(self):
        """ is_grantha() should return True for all grantha consonants """

        print("Testing TamilLetter.is_grantha() with grantha consonants", end=' ')

        for consonant in GRANTHA_CONSONANTS:

            self.assertTrue(TamilLetter.is_grantha(consonant), "\'%s\' is a grantha consonant, but is_grantha() returned False" %consonant)

        print(".... pass")


    def testIsGrantha_FalseCases(self):
        """ is_grantha() should return False for aytham and for all vowels, combinations and vallinam, mellinam and idaiyinam consonants """

        # Test with aytham
        print("Testing TamilLetter.is_grantha() with aytham", end=' ')

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_grantha(letter), "\'%s\' is Aytham, but is_grantha() returned True" %letter)

        print(".... pass")


        # Test with vowels
        print("Testing TamilLetter.is_grantha() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_grantha(vowel), "\'%s\' is a vowel, but is_grantha() returned True" %vowel)

        print(".... pass")


        # Test with combinations
        print("Testing TamilLetter.is_grantha() with combinations", end=' ')

        combinations = list(COMBINATIONS.values())
        for combination in combinations:

            self.assertFalse(TamilLetter.is_grantha(combination), "\'%s\' is a combination, but is_grantha() returned True" %combination)

        print(".... pass")


        # Test with grantha consonants
        print("Testing TamilLetter.is_grantha() with vallinam consonant", end=' ')

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is a vallinam consonant, but is_grantha() returned True" %consonant)

        print(".... pass")


        # Test with grantha consonants
        print("Testing TamilLetter.is_grantha() with mellinam consonant", end=' ')

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is an mellinam consonant, but is_grantha() returned True" %consonant)

        print(".... pass")

        # Test with grantha consonants
        print("Testing TamilLetter.is_grantha() with idaiyinam consonant", end=' ')

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is an idaiyinam consonant, but is_grantha() returned True" %consonant)

        print(".... pass")

    def testGetCombinationColumn_validInput(self):
        """ get_combination_column() should return a dictionary mapping consonant -> combination for a given vowel """

        print("Testing TamilLetter.get_combination_column() with vowels", end=' ')

        vowels = TamilLetter.get_vowels()

        # ensure that the correct row is returned for each vowel
        for vowel in vowels:

            expected = COMBINATIONS_BY_VOWEL[vowel]
            received = TamilLetter.get_combination_column(vowel)

            self.assertEqual(expected, received, "Expected dictionary %s to be equal to dictionary %s" %(expected, received))


        print(".... pass")


    def testGetCombinationColumn_invalidInput(self):
        """ get_combination_column() should raise a ValueError for all consonants, combinations and aytham """

        # Test Aytham
        print("Testing TamilLetter.get_combination_column() with Aytham (ஃ) - expecting ValueError", end=' ')

        letter = AYTHAM

        with self.assertRaises(ValueError):
            _ = TamilLetter.get_combination_column(letter)

        print(".... pass")

        # Test consonants
        print("Testing TamilLetter.get_combination_column() with consonants - expecting ValueError", end=' ')

        consonants = TamilLetter.get_consonants()
        for consonant in consonants:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_column(consonant)

        print(".... pass")

        # Test Combinations
        print("Testing TamilLetter.get_combination_column() with combinations - expecting ValueError", end=' ')

        combinations = list(COMBINATIONS.values())

        for combination in combinations:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_column(combination)

        print(".... pass")


    def testGetCombinationRow_validInput(self):
        """ get_combination_row() should return a dictionary mapping vowel -> combination for a given consonant """

        print("Testing TamilLetter.get_combination_row() with consonants - Expecting a dictionary of vowel->combination mappings for the given consonant", end=' ')

        consonants = TamilLetter.get_consonants()

        # ensure that the correct row is returned for each consonant
        for consonant in consonants:

            expected = COMBINATIONS_BY_CONSONANT[consonant]
            received = TamilLetter.get_combination_row(consonant)

            self.assertEqual(expected, received, "Expected dictionary %s to be equal to dictionary %s" %(expected, received))


        print(".... pass")


    def testGetCombinationRow_invalidInput(self):
        """ get_combination_row() should raise a ValueError for all consonants, combinations and aytham """

        # Test Aytham
        print("Testing TamilLetter.get_combination_row() with Aytham (ஃ) - expecting ValueError", end=' ')

        letter = AYTHAM

        with self.assertRaises(ValueError):
            _ = TamilLetter.get_combination_row(letter)

        print(".... pass")

        # Test consonants
        print("Testing TamilLetter.get_combination_row() with vowels - expecting ValueError", end=' ')

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_row(vowel)

        print(".... pass")

        # Test Combinations
        print("Testing TamilLetter.get_combination_row() with combinations - expecting ValueError", end=' ')

        combinations = list(COMBINATIONS.values())

        for combination in combinations:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_row(combination)

        print(".... pass")


    def testGetCombinationEndings(self):
        """ get_combination_endings() should return a tuple of all the combination endings """

        print("Testing TamilLetter.get_combination_endings()", end=' ')

        expected_tuple = COMBINATION_ENDINGS_TUPLE
        received_tuple = TamilLetter.get_combination_endings()

        self.assertEqual(set(expected_tuple), set(received_tuple), "Expected tuple \'%s\' but received \'%s\'" %(expected_tuple, received_tuple) )

        print(".... pass")



'''def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TamilLetterTest))
    return suite

def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite) '''


if __name__ == '__main__':
    unittest.main()
