# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest
import logging

# import TamilLetter class

from amuthaa.TamilLetter import TamilLetter

logging.basicConfig(level=logging.DEBUG)

# a tuple dictionary that matches a consonant, vowel tuple to its combination
COMBINATIONS = {
                (u'க்', u'அ'): u'க', (u'க்', u'ஆ'): u'கா', (u'க்', u'இ'): u'கி',
                (u'க்', u'ஈ'): u'கீ', (u'க்', u'உ'): u'கு', (u'க்', u'ஊ'): u'கூ',
                (u'க்', u'எ'): u'கெ', (u'க்', u'ஏ'): u'கே', (u'க்', u'ஐ'): u'கை',
                (u'க்', u'ஒ'): u'கொ', (u'க்', u'ஓ'): u'கோ', (u'க்', u'ஔ'): u'கௌ',

                (u'ங்', u'அ'): u'ங', (u'ங்', u'ஆ'): u'ஙா', (u'ங்', u'இ'): u'ஙி',
                (u'ங்', u'ஈ'): u'ஙீ', (u'ங்', u'உ'): u'ஙு', (u'ங்', u'ஊ'): u'ஙூ',
                (u'ங்', u'எ'): u'ஙெ', (u'ங்', u'ஏ'): u'ஙே', (u'ங்', u'ஐ'): u'ஙை',
                (u'ங்', u'ஒ'): u'ஙொ', (u'ங்', u'ஓ'): u'ஙோ', (u'ங்', u'ஔ'): u'ஙௌ',

                (u'ச்', u'அ'): u'ச', (u'ச்', u'ஆ'): u'சா', (u'ச்', u'இ'): u'சி',
                (u'ச்', u'ஈ'): u'சீ', (u'ச்', u'உ'): u'சு', (u'ச்', u'ஊ'): u'சூ',
                (u'ச்', u'எ'): u'செ', (u'ச்', u'ஏ'): u'சே', (u'ச்', u'ஐ'): u'சை',
                (u'ச்', u'ஒ'): u'சொ', (u'ச்', u'ஓ'): u'சோ', (u'ச்', u'ஔ'): u'சௌ',

                (u'ஞ்', u'அ'): u'ஞ', (u'ஞ்', u'ஆ'): u'ஞா', (u'ஞ்', u'இ'): u'ஞி',
                (u'ஞ்', u'ஈ'): u'ஞீ', (u'ஞ்', u'உ'): u'ஞு', (u'ஞ்', u'ஊ'): u'ஞூ',
                (u'ஞ்', u'எ'): u'ஞெ', (u'ஞ்', u'ஏ'): u'ஞே', (u'ஞ்', u'ஐ'): u'ஞை',
                (u'ஞ்', u'ஒ'): u'ஞொ', (u'ஞ்', u'ஓ'): u'ஞோ', (u'ஞ்', u'ஔ'): u'ஞௌ',

                (u'ட்', u'அ'): u'ட', (u'ட்', u'ஆ'): u'டா', (u'ட்', u'இ'): u'டி',
                (u'ட்', u'ஈ'): u'டீ', (u'ட்', u'உ'): u'டு', (u'ட்', u'ஊ'): u'டூ',
                (u'ட்', u'எ'): u'டெ', (u'ட்', u'ஏ'): u'டே', (u'ட்', u'ஐ'): u'டை',
                (u'ட்', u'ஒ'): u'டொ', (u'ட்', u'ஓ'): u'டோ', (u'ட்', u'ஔ'): u'டௌ',

                (u'ண்', u'அ'): u'ண', (u'ண்', u'ஆ'): u'ணா', (u'ண்', u'இ'): u'ணி',
                (u'ண்', u'ஈ'): u'ணீ', (u'ண்', u'உ'): u'ணு', (u'ண்', u'ஊ'): u'ணூ',
                (u'ண்', u'எ'): u'ணெ', (u'ண்', u'ஏ'): u'ணே', (u'ண்', u'ஐ'): u'ணை',
                (u'ண்', u'ஒ'): u'ணொ', (u'ண்', u'ஓ'): u'ணோ', (u'ண்', u'ஔ'): u'ணௌ',

                (u'த்', u'அ'): u'த', (u'த்', u'ஆ'): u'தா', (u'த்', u'இ'): u'தி',
                (u'த்', u'ஈ'): u'தீ', (u'த்', u'உ'): u'து', (u'த்', u'ஊ'): u'தூ',
                (u'த்', u'எ'): u'தெ', (u'த்', u'ஏ'): u'தே', (u'த்', u'ஐ'): u'தை',
                (u'த்', u'ஒ'): u'தொ', (u'த்', u'ஓ'): u'தோ', (u'த்', u'ஔ'): u'தௌ',

                (u'ந்', u'அ'): u'ந', (u'ந்', u'ஆ'): u'நா', (u'ந்', u'இ'): u'நி',
                (u'ந்', u'ஈ'): u'நீ', (u'ந்', u'உ'): u'நு', (u'ந்', u'ஊ'): u'நூ',
                (u'ந்', u'எ'): u'நெ', (u'ந்', u'ஏ'): u'நே', (u'ந்', u'ஐ'): u'நை',
                (u'ந்', u'ஒ'): u'நொ', (u'ந்', u'ஓ'): u'நோ', (u'ந்', u'ஔ'): u'நௌ',

                (u'ப்', u'அ'): u'ப', (u'ப்', u'ஆ'): u'பா', (u'ப்', u'இ'): u'பி',
                (u'ப்', u'ஈ'): u'பீ', (u'ப்', u'உ'): u'பு', (u'ப்', u'ஊ'): u'பூ',
                (u'ப்', u'எ'): u'பெ', (u'ப்', u'ஏ'): u'பே', (u'ப்', u'ஐ'): u'பை',
                (u'ப்', u'ஒ'): u'பொ', (u'ப்', u'ஓ'): u'போ', (u'ப்', u'ஔ'): u'பௌ',

                (u'ம்', u'அ'): u'ம', (u'ம்', u'ஆ'): u'மா', (u'ம்', u'இ'): u'மி',
                (u'ம்', u'ஈ'): u'மீ', (u'ம்', u'உ'): u'மு', (u'ம்', u'ஊ'): u'மூ',
                (u'ம்', u'எ'): u'மெ', (u'ம்', u'ஏ'): u'மே', (u'ம்', u'ஐ'): u'மை',
                (u'ம்', u'ஒ'): u'மொ', (u'ம்', u'ஓ'): u'மோ', (u'ம்', u'ஔ'): u'மௌ',

                (u'ய்', u'அ'): u'ய', (u'ய்', u'ஆ'): u'யா', (u'ய்', u'இ'): u'யி',
                (u'ய்', u'ஈ'): u'யீ', (u'ய்', u'உ'): u'யு', (u'ய்', u'ஊ'): u'யூ',
                (u'ய்', u'எ'): u'யெ', (u'ய்', u'ஏ'): u'யே', (u'ய்', u'ஐ'): u'யை',
                (u'ய்', u'ஒ'): u'யொ', (u'ய்', u'ஓ'): u'யோ', (u'ய்', u'ஔ'): u'யௌ',

                (u'ர்', u'அ'): u'ர', (u'ர்', u'ஆ'): u'ரா', (u'ர்', u'இ'): u'ரி',
                (u'ர்', u'ஈ'): u'ரீ', (u'ர்', u'உ'): u'ரு', (u'ர்', u'ஊ'): u'ரூ',
                (u'ர்', u'எ'): u'ரெ', (u'ர்', u'ஏ'): u'ரே', (u'ர்', u'ஐ'): u'ரை',
                (u'ர்', u'ஒ'): u'ரொ', (u'ர்', u'ஓ'): u'ரோ', (u'ர்', u'ஔ'): u'ரௌ',

                (u'ல்', u'அ'): u'ல', (u'ல்', u'ஆ'): u'லா', (u'ல்', u'இ'): u'லி',
                (u'ல்', u'ஈ'): u'லீ', (u'ல்', u'உ'): u'லு', (u'ல்', u'ஊ'): u'லூ',
                (u'ல்', u'எ'): u'லெ', (u'ல்', u'ஏ'): u'லே', (u'ல்', u'ஐ'): u'லை',
                (u'ல்', u'ஒ'): u'லொ', (u'ல்', u'ஓ'): u'லோ', (u'ல்', u'ஔ'): u'லௌ',

                (u'வ்', u'அ'): u'வ', (u'வ்', u'ஆ'): u'வா', (u'வ்', u'இ'): u'வி',
                (u'வ்', u'ஈ'): u'வீ', (u'வ்', u'உ'): u'வு', (u'வ்', u'ஊ'): u'வூ',
                (u'வ்', u'எ'): u'வெ', (u'வ்', u'ஏ'): u'வே', (u'வ்', u'ஐ'): u'வை',
                (u'வ்', u'ஒ'): u'வொ', (u'வ்', u'ஓ'): u'வோ', (u'வ்', u'ஔ'): u'வௌ',

                (u'ழ்', u'அ'): u'ழ', (u'ழ்', u'ஆ'): u'ழா', (u'ழ்', u'இ'): u'ழி',
                (u'ழ்', u'ஈ'): u'ழீ', (u'ழ்', u'உ'): u'ழு', (u'ழ்', u'ஊ'): u'ழூ',
                (u'ழ்', u'எ'): u'ழெ', (u'ழ்', u'ஏ'): u'ழே', (u'ழ்', u'ஐ'): u'ழை',
                (u'ழ்', u'ஒ'): u'ழொ', (u'ழ்', u'ஓ'): u'ழோ', (u'ழ்', u'ஔ'): u'ழௌ',

                (u'ள்', u'அ'): u'ள', (u'ள்', u'ஆ'): u'ளா', (u'ள்', u'இ'): u'ளி',
                (u'ள்', u'ஈ'): u'ளீ', (u'ள்', u'உ'): u'ளு', (u'ள்', u'ஊ'): u'ளூ',
                (u'ள்', u'எ'): u'ளெ', (u'ள்', u'ஏ'): u'ளே', (u'ள்', u'ஐ'): u'ளை',
                (u'ள்', u'ஒ'): u'ளொ', (u'ள்', u'ஓ'): u'ளோ', (u'ள்', u'ஔ'): u'ளௌ',

                (u'ற்', u'அ'): u'ற', (u'ற்', u'ஆ'): u'றா', (u'ற்', u'இ'): u'றி',
                (u'ற்', u'ஈ'): u'றீ', (u'ற்', u'உ'): u'று', (u'ற்', u'ஊ'): u'றூ',
                (u'ற்', u'எ'): u'றெ', (u'ற்', u'ஏ'): u'றே', (u'ற்', u'ஐ'): u'றை',
                (u'ற்', u'ஒ'): u'றொ', (u'ற்', u'ஓ'): u'றோ', (u'ற்', u'ஔ'): u'றௌ',

                (u'ன்', u'அ'): u'ன', (u'ன்', u'ஆ'): u'னா', (u'ன்', u'இ'): u'னி',
                (u'ன்', u'ஈ'): u'னீ', (u'ன்', u'உ'): u'னு', (u'ன்', u'ஊ'): u'னூ',
                (u'ன்', u'எ'): u'னெ', (u'ன்', u'ஏ'): u'னே', (u'ன்', u'ஐ'): u'னை',
                (u'ன்', u'ஒ'): u'னொ', (u'ன்', u'ஓ'): u'னோ', (u'ன்', u'ஔ'): u'னௌ',

                (u'ஜ்', u'அ'): u'ஜ', (u'ஜ்', u'ஆ'): u'ஜா', (u'ஜ்', u'இ'): u'ஜி',
                (u'ஜ்', u'ஈ'): u'ஜீ', (u'ஜ்', u'உ'): u'ஜு', (u'ஜ்', u'ஊ'): u'ஜூ',
                (u'ஜ்', u'எ'): u'ஜெ', (u'ஜ்', u'ஏ'): u'ஜே', (u'ஜ்', u'ஐ'): u'ஜை',
                (u'ஜ்', u'ஒ'): u'ஜொ', (u'ஜ்', u'ஓ'): u'ஜோ', (u'ஜ்', u'ஔ'): u'ஜௌ',

                (u'ஷ்', u'அ'): u'ஷ', (u'ஷ்', u'ஆ'): u'ஷா', (u'ஷ்', u'இ'): u'ஷி',
                (u'ஷ்', u'ஈ'): u'ஷீ', (u'ஷ்', u'உ'): u'ஷு', (u'ஷ்', u'ஊ'): u'ஷூ',
                (u'ஷ்', u'எ'): u'ஷெ', (u'ஷ்', u'ஏ'): u'ஷே', (u'ஷ்', u'ஐ'): u'ஷை',
                (u'ஷ்', u'ஒ'): u'ஷொ', (u'ஷ்', u'ஓ'): u'ஷோ', (u'ஷ்', u'ஔ'): u'ஷௌ',

                (u'ஸ்', u'அ'): u'ஸ', (u'ஸ்', u'ஆ'): u'ஸா', (u'ஸ்', u'இ'): u'ஸி',
                (u'ஸ்', u'ஈ'): u'ஸீ', (u'ஸ்', u'உ'): u'ஸு', (u'ஸ்', u'ஊ'): u'ஸூ',
                (u'ஸ்', u'எ'): u'ஸெ', (u'ஸ்', u'ஏ'): u'ஸே', (u'ஸ்', u'ஐ'): u'ஸை',
                (u'ஸ்', u'ஒ'): u'ஸொ', (u'ஸ்', u'ஓ'): u'ஸோ', (u'ஸ்', u'ஔ'): u'ஸௌ',

                (u'ஹ்', u'அ'): u'ஹ', (u'ஹ்', u'ஆ'): u'ஹா', (u'ஹ்', u'இ'): u'ஹி',
                (u'ஹ்', u'ஈ'): u'ஹீ', (u'ஹ்', u'உ'): u'ஹு', (u'ஹ்', u'ஊ'): u'ஹூ',
                (u'ஹ்', u'எ'): u'ஹெ', (u'ஹ்', u'ஏ'): u'ஹே', (u'ஹ்', u'ஐ'): u'ஹை',
                (u'ஹ்', u'ஒ'): u'ஹொ', (u'ஹ்', u'ஓ'): u'ஹோ', (u'ஹ்', u'ஔ'): u'ஹௌ',
                }

COMBINATIONS_BY_CONSONANT = {
                             u'க்': { u'அ': u'க', u'ஆ': u'கா', u'இ': u'கி', u'ஈ': u'கீ',
                                      u'உ': u'கு', u'ஊ': u'கூ', u'எ': u'கெ', u'ஏ': u'கே',
                                      u'ஐ': u'கை', u'ஒ': u'கொ', u'ஓ': u'கோ', u'ஔ': u'கௌ'
                                      },
                             u'ங்': {u'அ': u'ங', u'ஆ': u'ஙா', u'இ': u'ஙி', u'ஈ':
                                      u'ஙீ', u'உ': u'ஙு', u'ஊ': u'ஙூ', u'எ': u'ஙெ', u'ஏ': u'ஙே',
                                      u'ஐ': u'ஙை', u'ஒ': u'ஙொ', u'ஓ': u'ஙோ', u'ஔ': u'ஙௌ'
                                      },
                             u'ச்': { u'அ': u'ச', u'ஆ': u'சா', u'இ': u'சி', u'ஈ': u'சீ',
                                      u'உ': u'சு', u'ஊ': u'சூ', u'எ': u'செ', u'ஏ': u'சே',
                                      u'ஐ': u'சை', u'ஒ': u'சொ', u'ஓ': u'சோ', u'ஔ': u'சௌ'
                                      },
                             u'ஞ்': { u'அ': u'ஞ', u'ஆ': u'ஞா', u'இ': u'ஞி', u'ஈ': u'ஞீ',
                                      u'உ': u'ஞு', u'ஊ': u'ஞூ', u'எ': u'ஞெ', u'ஏ': u'ஞே',
                                      u'ஐ': u'ஞை', u'ஒ': u'ஞொ', u'ஓ': u'ஞோ', u'ஔ': u'ஞௌ'
                                      },
                             u'ட்': { u'அ': u'ட', u'ஆ': u'டா', u'இ': u'டி', u'ஈ': u'டீ',
                                      u'உ': u'டு', u'ஊ': u'டூ', u'எ': u'டெ', u'ஏ': u'டே',
                                      u'ஐ': u'டை', u'ஒ': u'டொ', u'ஓ': u'டோ', u'ஔ': u'டௌ'
                                      },
                             u'ண்': { u'அ': u'ண', u'ஆ': u'ணா', u'இ': u'ணி', u'ஈ': u'ணீ',
                                      u'உ': u'ணு', u'ஊ': u'ணூ', u'எ': u'ணெ', u'ஏ': u'ணே',
                                      u'ஐ': u'ணை', u'ஒ': u'ணொ', u'ஓ': u'ணோ', u'ஔ': u'ணௌ'
                                      },
                             u'த்': { u'அ': u'த', u'ஆ': u'தா', u'இ': u'தி', u'ஈ': u'தீ',
                                      u'உ': u'து', u'ஊ': u'தூ', u'எ': u'தெ', u'ஏ': u'தே',
                                      u'ஐ': u'தை', u'ஒ': u'தொ', u'ஓ': u'தோ', u'ஔ': u'தௌ'
                                      },
                             u'ந்': { u'அ': u'ந', u'ஆ': u'நா', u'இ': u'நி', u'ஈ': u'நீ',
                                      u'உ': u'நு', u'ஊ': u'நூ', u'எ': u'நெ', u'ஏ': u'நே',
                                      u'ஐ': u'நை', u'ஒ': u'நொ', u'ஓ': u'நோ', u'ஔ': u'நௌ'
                                      },
                             u'ப்': { u'அ': u'ப', u'ஆ': u'பா', u'இ': u'பி', u'ஈ': u'பீ',
                                      u'உ': u'பு', u'ஊ': u'பூ', u'எ': u'பெ', u'ஏ': u'பே',
                                      u'ஐ': u'பை', u'ஒ': u'பொ', u'ஓ': u'போ', u'ஔ': u'பௌ'
                                      },
                             u'ம்': { u'அ': u'ம', u'ஆ': u'மா', u'இ': u'மி', u'ஈ': u'மீ',
                                      u'உ': u'மு', u'ஊ': u'மூ', u'எ': u'மெ', u'ஏ': u'மே',
                                      u'ஐ': u'மை', u'ஒ': u'மொ', u'ஓ': u'மோ', u'ஔ': u'மௌ'
                                      },
                             u'ய்': { u'அ': u'ய', u'ஆ': u'யா', u'இ': u'யி', u'ஈ': u'யீ',
                                      u'உ': u'யு', u'ஊ': u'யூ', u'எ': u'யெ', u'ஏ': u'யே',
                                      u'ஐ': u'யை', u'ஒ': u'யொ', u'ஓ': u'யோ', u'ஔ': u'யௌ'
                                      },
                             u'ர்': { u'அ': u'ர', u'ஆ': u'ரா', u'இ': u'ரி', u'ஈ': u'ரீ',
                                      u'உ': u'ரு', u'ஊ': u'ரூ', u'எ': u'ரெ', u'ஏ': u'ரே',
                                      u'ஐ': u'ரை', u'ஒ': u'ரொ', u'ஓ': u'ரோ', u'ஔ': u'ரௌ'
                                      },
                             u'ல்': { u'அ': u'ல', u'ஆ': u'லா', u'இ': u'லி', u'ஈ': u'லீ',
                                      u'உ': u'லு', u'ஊ': u'லூ', u'எ': u'லெ', u'ஏ': u'லே',
                                      u'ஐ': u'லை', u'ஒ': u'லொ', u'ஓ': u'லோ', u'ஔ': u'லௌ'
                                      },
                             u'வ்': { u'அ': u'வ', u'ஆ': u'வா', u'இ': u'வி', u'ஈ': u'வீ',
                                      u'உ': u'வு', u'ஊ': u'வூ', u'எ': u'வெ', u'ஏ': u'வே',
                                      u'ஐ': u'வை', u'ஒ': u'வொ', u'ஓ': u'வோ', u'ஔ': u'வௌ'
                                      },
                             u'ழ்': { u'அ': u'ழ', u'ஆ': u'ழா', u'இ': u'ழி', u'ஈ': u'ழீ',
                                      u'உ': u'ழு', u'ஊ': u'ழூ', u'எ': u'ழெ', u'ஏ': u'ழே',
                                      u'ஐ': u'ழை', u'ஒ': u'ழொ', u'ஓ': u'ழோ', u'ஔ': u'ழௌ'
                                      },
                             u'ள்': { u'அ': u'ள', u'ஆ': u'ளா', u'இ': u'ளி', u'ஈ': u'ளீ',
                                      u'உ': u'ளு', u'ஊ': u'ளூ', u'எ': u'ளெ', u'ஏ': u'ளே',
                                      u'ஐ': u'ளை', u'ஒ': u'ளொ', u'ஓ': u'ளோ', u'ஔ': u'ளௌ'
                                      },
                             u'ற்': { u'அ': u'ற', u'ஆ': u'றா', u'இ': u'றி', u'ஈ': u'றீ',
                                      u'உ': u'று', u'ஊ': u'றூ', u'எ': u'றெ', u'ஏ': u'றே',
                                      u'ஐ': u'றை', u'ஒ': u'றொ', u'ஓ': u'றோ', u'ஔ': u'றௌ'
                                      },
                             u'ன்': { u'அ': u'ன', u'ஆ': u'னா', u'இ': u'னி', u'ஈ': u'னீ',
                                      u'உ': u'னு', u'ஊ': u'னூ', u'எ': u'னெ', u'ஏ': u'னே',
                                      u'ஐ': u'னை', u'ஒ': u'னொ', u'ஓ': u'னோ', u'ஔ': u'னௌ'
                                      },
                             u'ஜ்': { u'அ': u'ஜ', u'ஆ': u'ஜா', u'இ': u'ஜி', u'ஈ': u'ஜீ',
                                      u'உ': u'ஜு', u'ஊ': u'ஜூ', u'எ': u'ஜெ', u'ஏ': u'ஜே',
                                      u'ஐ': u'ஜை', u'ஒ': u'ஜொ', u'ஓ': u'ஜோ', u'ஔ': u'ஜௌ'
                                      },
                             u'ஸ்': { u'அ': u'ஸ', u'ஆ': u'ஸா', u'இ': u'ஸி', u'ஈ': u'ஸீ',
                                      u'உ': u'ஸு', u'ஊ': u'ஸூ', u'எ': u'ஸெ', u'ஏ': u'ஸே',
                                      u'ஐ': u'ஸை', u'ஒ': u'ஸொ', u'ஓ': u'ஸோ', u'ஔ': u'ஸௌ'
                                      },
                             u'ஷ்': { u'அ': u'ஷ', u'ஆ': u'ஷா', u'இ': u'ஷி', u'ஈ': u'ஷீ',
                                      u'உ': u'ஷு', u'ஊ': u'ஷூ', u'எ': u'ஷெ', u'ஏ': u'ஷே',
                                      u'ஐ': u'ஷை', u'ஒ': u'ஷொ', u'ஓ': u'ஷோ', u'ஔ': u'ஷௌ'
                                      },
                             u'ஹ்': { u'அ': u'ஹ', u'ஆ': u'ஹா', u'இ': u'ஹி', u'ஈ': u'ஹீ',
                                      u'உ': u'ஹு', u'ஊ': u'ஹூ', u'எ': u'ஹெ', u'ஏ': u'ஹே',
                                      u'ஐ': u'ஹை', u'ஒ': u'ஹொ', u'ஓ': u'ஹோ', u'ஔ': u'ஹௌ'
                                      }
                             }


COMBINATIONS_BY_VOWEL = {
                         u'அ': {
                                 u'க்': u'க', u'ங்': u'ங', u'ச்': u'ச', u'ஞ்': u'ஞ', u'ட்': u'ட', u'ண்': u'ண',
                                 u'த்': u'த', u'ந்': u'ந', u'ப்': u'ப', u'ம்': u'ம', u'ய்': u'ய', u'ர்': u'ர',
                                 u'ல்': u'ல', u'வ்': u'வ', u'ழ்': u'ழ', u'ள்': u'ள', u'ற்': u'ற', u'ன்': u'ன',
                                 u'ஜ்': u'ஜ', u'ஷ்': u'ஷ', u'ஸ்': u'ஸ', u'ஹ்': u'ஹ'
                                 },
                         u'ஆ': {
                                 u'க்': u'கா', u'ங்': u'ஙா', u'ச்': u'சா', u'ஞ்': u'ஞா', u'ட்': u'டா', u'ண்': u'ணா',
                                 u'த்': u'தா', u'ந்': u'நா', u'ப்': u'பா', u'ம்': u'மா', u'ய்': u'யா', u'ர்': u'ரா',
                                 u'ல்': u'லா', u'வ்': u'வா', u'ழ்': u'ழா', u'ள்': u'ளா', u'ற்': u'றா', u'ன்': u'னா',
                                 u'ஜ்': u'ஜா', u'ஷ்': u'ஷா', u'ஸ்': u'ஸா', u'ஹ்': u'ஹா'
                                 },
                         u'இ': {
                                 u'க்': u'கி', u'ங்': u'ஙி', u'ச்': u'சி', u'ஞ்': u'ஞி', u'ட்': u'டி', u'ண்': u'ணி',
                                 u'த்': u'தி', u'ந்': u'நி', u'ப்': u'பி', u'ம்': u'மி', u'ய்': u'யி', u'ர்': u'ரி',
                                 u'ல்': u'லி', u'வ்': u'வி', u'ழ்': u'ழி', u'ள்': u'ளி', u'ற்': u'றி', u'ன்': u'னி',
                                 u'ஜ்': u'ஜி', u'ஷ்': u'ஷி', u'ஸ்': u'ஸி', u'ஹ்': u'ஹி'
                                 },
                         u'ஈ': {
                                 u'க்': u'கீ', u'ங்': u'ஙீ', u'ச்': u'சீ', u'ஞ்': u'ஞீ', u'ட்': u'டீ', u'ண்': u'ணீ',
                                 u'த்': u'தீ', u'ந்': u'நீ', u'ப்': u'பீ', u'ம்': u'மீ', u'ய்': u'யீ', u'ர்': u'ரீ',
                                 u'ல்': u'லீ', u'வ்': u'வீ', u'ழ்': u'ழீ', u'ள்': u'ளீ', u'ற்': u'றீ', u'ன்': u'னீ',
                                 u'ஜ்': u'ஜீ', u'ஷ்': u'ஷீ', u'ஸ்': u'ஸீ', u'ஹ்': u'ஹீ'
                                 },
                         u'உ': {
                                 u'க்': u'கு', u'ங்': u'ஙு', u'ச்': u'சு', u'ஞ்': u'ஞு', u'ட்': u'டு', u'ண்': u'ணு',
                                 u'த்': u'து', u'ந்': u'நு', u'ப்': u'பு', u'ம்': u'மு', u'ய்': u'யு', u'ர்': u'ரு',
                                 u'ல்': u'லு', u'வ்': u'வு', u'ழ்': u'ழு', u'ள்': u'ளு', u'ற்': u'று', u'ன்': u'னு',
                                 u'ஜ்': u'ஜு', u'ஷ்': u'ஷு', u'ஸ்': u'ஸு', u'ஹ்': u'ஹு'
                                 },
                         u'ஊ': {
                                 u'க்': u'கூ', u'ங்': u'ஙூ', u'ச்': u'சூ', u'ஞ்': u'ஞூ', u'ட்': u'டூ', u'ண்': u'ணூ',
                                 u'த்': u'தூ', u'ந்': u'நூ', u'ப்': u'பூ', u'ம்': u'மூ', u'ய்': u'யூ', u'ர்': u'ரூ',
                                 u'ல்': u'லூ', u'வ்': u'வூ', u'ழ்': u'ழூ', u'ள்': u'ளூ', u'ற்': u'றூ', u'ன்': u'னூ',
                                 u'ஜ்': u'ஜூ', u'ஷ்': u'ஷூ', u'ஸ்': u'ஸூ', u'ஹ்': u'ஹூ'
                                 },
                         u'எ': {
                                 u'க்': u'கெ', u'ங்': u'ஙெ', u'ச்': u'செ', u'ஞ்': u'ஞெ', u'ட்': u'டெ', u'ண்': u'ணெ',
                                 u'த்': u'தெ', u'ந்': u'நெ', u'ப்': u'பெ', u'ம்': u'மெ', u'ய்': u'யெ', u'ர்': u'ரெ',
                                 u'ல்': u'லெ', u'வ்': u'வெ', u'ழ்': u'ழெ', u'ள்': u'ளெ', u'ற்': u'றெ', u'ன்': u'னெ',
                                 u'ஜ்': u'ஜெ', u'ஷ்': u'ஷெ', u'ஸ்': u'ஸெ', u'ஹ்': u'ஹெ'
                                 },
                         u'ஏ': {
                                 u'க்': u'கே', u'ங்': u'ஙே', u'ச்': u'சே', u'ஞ்': u'ஞே', u'ட்': u'டே', u'ண்': u'ணே',
                                 u'த்': u'தே', u'ந்': u'நே', u'ப்': u'பே', u'ம்': u'மே', u'ய்': u'யே', u'ர்': u'ரே',
                                 u'ல்': u'லே', u'வ்': u'வே', u'ழ்': u'ழே', u'ள்': u'ளே', u'ற்': u'றே', u'ன்': u'னே',
                                 u'ஜ்': u'ஜே', u'ஷ்': u'ஷே', u'ஸ்': u'ஸே', u'ஹ்': u'ஹே'
                                 },
                         u'ஐ': {
                                 u'க்': u'கை', u'ங்': u'ஙை', u'ச்': u'சை', u'ஞ்': u'ஞை', u'ட்': u'டை', u'ண்': u'ணை',
                                 u'த்': u'தை', u'ந்': u'நை', u'ப்': u'பை', u'ம்': u'மை', u'ய்': u'யை', u'ர்': u'ரை',
                                 u'ல்': u'லை', u'வ்': u'வை', u'ழ்': u'ழை', u'ள்': u'ளை', u'ற்': u'றை', u'ன்': u'னை',
                                 u'ஜ்': u'ஜை', u'ஷ்': u'ஷை', u'ஸ்': u'ஸை', u'ஹ்': u'ஹை'
                                 },
                         u'ஒ': {
                                 u'க்': u'கொ', u'ங்': u'ஙொ', u'ச்': u'சொ', u'ஞ்': u'ஞொ', u'ட்': u'டொ', u'ண்': u'ணொ',
                                 u'த்': u'தொ', u'ந்': u'நொ', u'ப்': u'பொ', u'ம்': u'மொ', u'ய்': u'யொ', u'ர்': u'ரொ',
                                 u'ல்': u'லொ', u'வ்': u'வொ', u'ழ்': u'ழொ', u'ள்': u'ளொ', u'ற்': u'றொ', u'ன்': u'னொ',
                                 u'ஜ்': u'ஜொ', u'ஷ்': u'ஷொ', u'ஸ்': u'ஸொ', u'ஹ்': u'ஹொ'
                                 },
                         u'ஓ': {
                                 u'க்': u'கோ', u'ங்': u'ஙோ', u'ச்': u'சோ', u'ஞ்': u'ஞோ', u'ட்': u'டோ', u'ண்': u'ணோ',
                                 u'த்': u'தோ', u'ந்': u'நோ', u'ப்': u'போ', u'ம்': u'மோ', u'ய்': u'யோ', u'ர்': u'ரோ',
                                 u'ல்': u'லோ', u'வ்': u'வோ', u'ழ்': u'ழோ', u'ள்': u'ளோ', u'ற்': u'றோ', u'ன்': u'னோ',
                                 u'ஜ்': u'ஜோ', u'ஷ்': u'ஷோ', u'ஸ்': u'ஸோ', u'ஹ்': u'ஹோ'
                                 },
                         u'ஔ': {
                                 u'க்': u'கௌ', u'ங்': u'ஙௌ', u'ச்': u'சௌ', u'ஞ்': u'ஞௌ', u'ட்': u'டௌ', u'ண்': u'ணௌ',
                                 u'த்': u'தௌ', u'ந்': u'நௌ', u'ப்': u'பௌ', u'ம்': u'மௌ', u'ய்': u'யௌ', u'ர்': u'ரௌ',
                                 u'ல்': u'லௌ', u'வ்': u'வௌ', u'ழ்': u'ழௌ', u'ள்': u'ளௌ', u'ற்': u'றௌ', u'ன்': u'னௌ',
                                 u'ஜ்': u'ஜௌ', u'ஷ்': u'ஷௌ', u'ஸ்': u'ஸௌ', u'ஹ்': u'ஹௌ'
                                 }
                         }


## Other tuples used for testing

COMBINATION_ENDINGS_TUPLE  = (u'\u0BBE', # ஆ -> ா
                             u'\u0BBF', # இ -> ி
                            u'\u0BC0', # ஈ -> ீ
                            u'\u0BC1', # உ -> ு
                            u'\u0BC2',  # ஊ -> ூ
                            u'\u0BC6', # எ -> ெ
                            u'\u0BC7', # ஏ -> ே
                            u'\u0BC8', # ஐ -> ை
                            u'\u0BCA', # ஒ -> ொ
                            u'\u0BCB', # ஓ -> ோ
                            u'\u0BCC' # ஔ -> ௌ
                            )
PULLI =  u'்'
AYTHAM  = u'ஃ'

VALLINAM_CONSONANTS = (u'க்', u'ச்', u'ட்', u'த்', u'ப்', u'ற்')
MELLINAM_CONSONANTS = (u'ங்', u'ஞ்', u'ண்', u'ந்', u'ம்', u'ன்')
IDAIYINAM_CONSONANTS = (u'ய்',u'ர்', u'ல்', u'வ்', u'ழ்', u'ள்')
GRANTHA_CONSONANTS = (u'ஜ்', u'ஷ்', u'ஸ்', u'ஹ்') # removed support for 'க்ஷ்' temporarily and ஶ் permanently

KURIL_VOWELS = (u'அ', u'இ', u'உ', u'எ', u'ஒ')
NEDIL_VOWELS = (u'ஆ', u'ஈ', u'ஊ', u'ஏ', u'ஐ', u'ஓ', u'ஔ')

A_COMBINATIONS = (u'அ', u'ஆ', u'இ', u'ஈ', u'உ', u'ஊ',  u'எ', u'ஏ', u'ஐ', u'ஒ', u'ஓ', u'ஔ')


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

        print "Testing TamilLetter.is_aytham() with aytham - expecting True",

        self.assertTrue(TamilLetter.is_aytham(u'ஃ'))

        print ".... pass"

    def testIsAytham_Vowels(self):
        """is_aytham should return False for all vowels"""

        print "Testing TamilLetter.is_aytham() with vowels - expecting True",

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_aytham(vowel))

        print ".... pass"

    def testIsAytham_Consonants(self):
        """is_aytham should return False for all consonants"""

        print "Testing TamilLetter.is_aytham() with consonants - expecting False",

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_aytham(consonant))

        print ".... pass"

    def testIsAytham_Combinations(self):
        """is_aytham should return False for all combinations"""

        print "Testing TamilLetter.is_aytham() with combinations - expecting False",

        for combination in COMBINATIONS.values():

            self.assertFalse(TamilLetter.is_aytham(combination))

        print ".... pass"


    ## Test is_vowel() with aytham, vowels, consonants and combinations

    def testIsVowel_Aytham(self):
        """is_vowel should return True for aytham"""

        print "Testing TamilLetter.is_vowel() with aytham - expecting False",

        self.assertFalse(TamilLetter.is_vowel(TamilLetter.get_aytham()))

        print ".... pass"

    def testIsVowel_Vowels(self):
        """is_vowel should return True for all vowels"""

        print "Testing TamilLetter.is_vowel() with vowels - expecting True",

        for vowel in TamilLetter.get_vowels():

            self.assertTrue(TamilLetter.is_vowel(vowel))

        print ".... pass"

    def testIsVowel_Consonants(self):
        """is_vowel should return False for all consonants"""

        print "Testing TamilLetter.is_vowel() with consonants - expecting False",

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_vowel(consonant))

        print ".... pass"

    def testIsVowel_Combinations(self):
        """is_vowel should return False for all combinations"""

        print "Testing TamilLetter.is_vowel() with combinations - expecting False",

        for combination in COMBINATIONS.values():

            self.assertFalse(TamilLetter.is_vowel(combination))

        print ".... pass"


    ## Test is_consonant() with aytham, vowels, consonants and combinations

    def testIsConsonant_Aytham(self):
        """is_consonant should return False for aytham"""

        print "Testing TamilLetter.is_consonant() with aytham - expecting False",

        self.assertFalse(TamilLetter.is_consonant(TamilLetter.get_aytham()))

        print ".... pass"

    def testIsConsonant_Vowels(self):
        """is_consonant should return False for all vowels"""

        print "Testing TamilLetter.is_consonant() with vowels - expecting False",

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_consonant(vowel))

        print ".... pass "

    def testIsConsonant_Consonants(self):
        """is_consonant should return True for all consonants"""

        print "Testing TamilLetter.is_consonant() with consonants - expecting True",

        for consonant in TamilLetter.get_consonants():

            self.assertTrue(TamilLetter.is_consonant(consonant))

        print ".... pass"

    def testIsConsonant_Combinations(self):
        """is_consonant should return False for all combinations"""

        print "Testing TamilLetter.is_consonant() with combinations - expecting False",

        for combination in COMBINATIONS.values():

            self.assertFalse(TamilLetter.is_consonant(combination))

        print ".... pass"



    ## Test is_combination() with aytham, vowels, consonants and combinations

    def testIsCombination_Aytham(self):
        """is_combination should return True for aytham"""

        print "Testing TamilLetter.is_combination() with aytham - expecting False",

        self.assertFalse(TamilLetter.is_combination(TamilLetter.get_aytham()))

        print ".... pass"

    def testIsCombination_Vowels(self):
        """is_combination should return False for all vowels"""

        print "Testing TamilLetter.is_combination() with vowels - expecting False",

        for vowel in TamilLetter.get_vowels():

            self.assertFalse(TamilLetter.is_combination(vowel))

        print ".... pass "

    def testIsCombination_Consonants(self):
        """is_combination should return False for all consonants"""

        print "Testing TamilLetter.is_combination() with consonants - expecting True",

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_combination(consonant))

        print ".... pass"

    def testIsCombination_Combinations(self):
        """is_combination should return True for all combinations"""

        print "Testing TamilLetter.is_combination() with combinations - expecting False",

        for combination in COMBINATIONS.values():

            self.assertTrue(TamilLetter.is_combination(combination))

        print ".... pass"


## Test get_script_name()

    def testGetScriptName_Tamil(self):
        """ get_script_name() should return the name of the script that the unicode character is encoded in """

        print "Testing TamilLetter.get_script_name() with Tamil letters",

        tamil_letters = tuple(TamilLetter.get_vowels())+tuple(TamilLetter.get_consonants())+tuple(COMBINATIONS.values())

        # Go through each Tamil letter
        for letter in tamil_letters:

            # format in title case
            result_script_name = TamilLetter.get_script_name(letter).title()
            script_name = 'TAMIL'.title()


            # check for equality
            self.assertEqual(script_name, result_script_name, "Error on letter \'%s\' from script \'%s\'. Function returned \'%s\'" %(letter, script_name, result_script_name))

        print ".... pass"


    def testGetScriptName_otherLanguages(self):
        """ get_script_name() should return the name of the script that the unicode character is encoded in """

        print "Testing TamilLetter.get_script_name() with letters from other scripts",

        other_languages = {
                           u'ඐ': 'SINHALA', u'එ': 'SINHALA', u'ඒ': 'SINHALA', u'ඓ': 'SINHALA',
                           u'ඔ': 'SINHALA', u'ඕ': 'SINHALA', u'ඖ': 'SINHALA', u'ඳ': 'SINHALA',
                           u'ප': 'SINHALA', u'ඵ': 'SINHALA', u'බ': 'SINHALA', u'භ': 'SINHALA',
                           u'ම': 'SINHALA', u'ඹ': 'SINHALA', u'ය': 'SINHALA', u'ර': 'SINHALA',

                           u'ഠ': 'MALAYALAM', u'ഡ': 'MALAYALAM', u'ഢ': 'MALAYALAM', u'ണ': 'MALAYALAM', u'ത': 'MALAYALAM',
                           u'ഥ': 'MALAYALAM', u'ദ': 'MALAYALAM', u'ധ': 'MALAYALAM', u'ന': 'MALAYALAM',

                           u'ಠ': 'KANNADA', u'ಡ': 'KANNADA', u'ಢ': 'KANNADA', u'ಣ': 'KANNADA', u'ತ': 'KANNADA',
                           u'ಥ': 'KANNADA', u'ದ': 'KANNADA', u'ಧ': 'KANNADA', u'ನ': 'KANNADA',

                           u'ఠ': 'TELUGU', u'డ': 'TELUGU', u'ఢ': 'TELUGU', u'ణ': 'TELUGU', u'త': 'TELUGU',
                           u'థ': 'TELUGU', u'ద': 'TELUGU', u'ధ': 'TELUGU', u'న': 'TELUGU',

                           u'ऐ': 'DEVANAGARI', u'ऑ': 'DEVANAGARI', u'ऒ': 'DEVANAGARI', u'ओ': 'DEVANAGARI',
                           u'औ': 'DEVANAGARI', u'क': 'DEVANAGARI', u'ख': 'DEVANAGARI', u'ग': 'DEVANAGARI',
                           u'घ': 'DEVANAGARI', u'ङ': 'DEVANAGARI', u'च': 'DEVANAGARI', u'छ': 'DEVANAGARI',
                           u'ज': 'DEVANAGARI', u'झ': 'DEVANAGARI', u'ञ': 'DEVANAGARI', u'ट': 'DEVANAGARI',

                           u'A': 'LATIN', u'B': 'LATIN', u'C': 'LATIN', u'D': 'LATIN', u'E': 'LATIN',
                           u'F': 'LATIN', u'G': 'LATIN', u'H': 'LATIN', u'I': 'LATIN', u'J': 'LATIN',
                           u'K': 'LATIN', u'L': 'LATIN', u'M': 'LATIN', u'N': 'LATIN', u'O': 'LATIN',

                           u'ฐ': 'THAI', u'ฑ': 'THAI', u'ฒ': 'THAI', u'ณ': 'THAI', u'ด': 'THAI', u'ต': 'THAI',
                           u'ถ': 'THAI', u'ท': 'THAI', u'ธ': 'THAI', u'น': 'THAI', u'บ': 'THAI',
                           u'ป': 'THAI', u'ผ': 'THAI', u'ฝ': 'THAI', u'พ': 'THAI', u'ฟ': 'THAI',

                           u'໐': 'LAO', u'໑': 'LAO', u'໒': 'LAO', u'໓': 'LAO', u'໔': 'LAO', u'໕': 'LAO',
                           u'໖': 'LAO', u'໗': 'LAO', u'໘': 'LAO', u'໙': 'LAO', u'ດ': 'LAO', u'ຕ': 'LAO',
                           u'ຖ': 'LAO', u'ທ': 'LAO', u'ນ': 'LAO', u'ບ': 'LAO', u'ປ': 'LAO', u'ຜ': 'LAO',
                           u'ຝ': 'LAO', u'ພ': 'LAO', u'ຟ': 'LAO',

                           u'ཐ': 'TIBETAN', u'ད': 'TIBETAN', u'དྷ': 'TIBETAN', u'ན': 'TIBETAN', u'པ': 'TIBETAN',
                           u'ཕ': 'TIBETAN', u'བ': 'TIBETAN', u'བྷ': 'TIBETAN', u'མ': 'TIBETAN', u'ཙ': 'TIBETAN',
                           u'ཚ': 'TIBETAN', u'ཛ': 'TIBETAN', u'ཛྷ': 'TIBETAN', u'ཝ': 'TIBETAN', u'ཞ': 'TIBETAN',
                           u'ཟ': 'TIBETAN',

                           u'ថ': 'KHMER', u'ទ': 'KHMER', u'ធ': 'KHMER', u'ន': 'KHMER', u'ប': 'KHMER',
                           u'ផ': 'KHMER', u'ព': 'KHMER', u'ភ': 'KHMER', u'ម': 'KHMER', u'យ': 'KHMER',
                           u'រ': 'KHMER', u'ល': 'KHMER', u'វ': 'KHMER', u'ឝ': 'KHMER', u'ឞ': 'KHMER',
                           u'ស': 'KHMER',

                           u'ᠠ': 'MONGOLIAN', u'ᠡ': 'MONGOLIAN', u'ᠢ': 'MONGOLIAN', u'ᠣ': 'MONGOLIAN',
                           u'ᠤ': 'MONGOLIAN', u'ᠥ': 'MONGOLIAN', u'ᠦ': 'MONGOLIAN', u'ᠧ': 'MONGOLIAN',
                           u'ᠨ': 'MONGOLIAN', u'ᠩ': 'MONGOLIAN', u'ᠪ': 'MONGOLIAN', u'ᠫ': 'MONGOLIAN',
                           u'ᠬ': 'MONGOLIAN', u'ᠭ': 'MONGOLIAN', u'ᠮ': 'MONGOLIAN', u'ᠯ': 'MONGOLIAN'
        }

        # Go through each key, value pair from above
        for letter in other_languages:

            # format in title case
            result_script_name = TamilLetter.get_script_name(letter).title()
            script_name = other_languages[letter].title()

            # check for equality
            self.assertEqual(script_name, result_script_name, "Error on letter \'%s\' from script \'%s\'. Function returned \'%s\'" %(letter, script_name, result_script_name))

        print ".... pass"

    def testIsKuril_kuril(self):
        """ is_kuril() should return True for all kuril letters """

        print "Testing TamilLetter.is_kuril() with kuril letters",

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return true
            self.assertTrue(TamilLetter.is_kuril(vowel), "Vowel \'%s\' returned False for is_kuril(). Should return True." %(vowel))

            # all combinations made from kuril vowels should also return true
            for combination in TamilLetter.get_combination_column(vowel).values():
                self.assertTrue(TamilLetter.is_kuril(combination), "Combination \'%s\' returned False for is_kuril(). Should return True." %(combination))

        print ".... pass"

    def testIsKuril_nedil(self):
        """ is_kuril() should return False for all nedil letters """

        print "Testing TamilLetter.is_kuril() with nedil letters",

        for vowel in NEDIL_VOWELS:

            # all the kuril vowels should return true
            self.assertFalse(TamilLetter.is_kuril(vowel), "Vowel \'%s\' returned True for is_kuril(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_kuril(combination), "Combination \'%s\' returned True for is_kuril(). Should return False." %(combination))

        print ".... pass"

    def testIsKuril_consonantsAndAytham(self):
        """ is_kuril() should return False for all consonants and for aytham """

        # first test consonants
        print "Testing TamilLetter.is_kuril() with consonants",

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_kuril(consonant), "Consonant \'%s\' returned True for is_kuril(). Should return False.")

        print ".... pass"


        #now test aytham
        print "Testing TamilLetter.is_kuril() with aytham (ஃ)",

        self.assertFalse(TamilLetter.is_kuril(AYTHAM), "Aytham (\'%s\') returned True for is_kuril(). Should return False." %AYTHAM)

        print ".... pass"


    def testIsNedil_kuril(self):
        """ is_nedil() should True for all kuril letters """

        print "Testing TamilLetter.is_nedil() with kuril letters",

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return false
            self.assertFalse(TamilLetter.is_nedil(vowel), "Vowel \'%s\' returned True for is_nedil(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_nedil(combination), "Combination \'%s\' returned True for is_nedil(). Should return False." %(combination))

        print ".... pass"

    def testIsNedil_nedil(self):
        """ is_nedil() should True for all kuril letters """

        print "Testing TamilLetter.is_nedil() with kuril letters",

        for vowel in KURIL_VOWELS:

            # all the kuril vowels should return false
            self.assertFalse(TamilLetter.is_nedil(vowel), "Vowel \'%s\' returned True for is_nedil(). Should return False." %(vowel))

            # all combinations made from kuril vowels should also return false
            for combination in TamilLetter.get_combination_column(vowel):
                self.assertFalse(TamilLetter.is_nedil(combination), "Combination \'%s\' returned True for is_nedil(). Should return False." %(combination))

        print ".... pass"

    def testIsNedil_consonantsAndAytham(self):
        """ is_nedil() should return False for all consonants and for aytham """

        # first test consonants
        print "Testing TamilLetter.is_nedil() with consonants",

        for consonant in TamilLetter.get_consonants():

            self.assertFalse(TamilLetter.is_nedil(consonant), "Consonant \'%s\' returned True for is_nedil(). Should return False.")

        print ".... pass"


        #now test aytham
        print "Testing TamilLetter.is_nedil() with aytham (ஃ)",

        self.assertFalse(TamilLetter.is_nedil(AYTHAM), "Aytham (\'%s\') returned True for is_nedil(). Should return False." %AYTHAM)

        print ".... pass"

    def testGetAytham(self):
        """ get_aytham() should return the Aytham (ஃ) character """

        print "Testing TamilLetter.get_aytham()",

        expected = AYTHAM
        received = TamilLetter.get_aytham()

        self.assertEqual(expected, received, "Expected Aytham (\'%s\'), but received \'%s\' instead" %(expected, received))


        print ".... pass"

    def testGetVowels(self):
        """ get_vowels() should return a tuple of all the vowels """

        print "Testing TamilLetter.get_vowels()",

        expected = KURIL_VOWELS + NEDIL_VOWELS
        received = TamilLetter.get_vowels()

        #ensure that both expected and received are tuples
        self.assertTrue(isinstance(expected,tuple), "\'%s\' should be a tuple, but is a %s" %(expected, type(expected)))
        self.assertTrue(isinstance(received,tuple), "\'%s\' should be a tuple, but is a %s" %(received, type(received)))

        #ensure that size of the two tuples is correct
        self.assertEqual(len(expected), len(received), "Vowel Tuple should have %s members" %len(expected))

        # compare as sets, to ignore order
        self.assertEquals(set(expected), set(received), "Expected tuple \'%s\' but received tuple \'%s\'" %(expected, received))

        print ".... pass"

    def testGetConsonants(self):
        """ get_consonants() should return a tuple of all the consonants """

        print "Testing TamilLetter.get_consonants()",

        expected = VALLINAM_CONSONANTS + MELLINAM_CONSONANTS + IDAIYINAM_CONSONANTS + GRANTHA_CONSONANTS
        received = TamilLetter.get_consonants()

        #ensure that both expected and received are tuples
        self.assertTrue(isinstance(expected,tuple), "\'%s\' should be a tuple, but is a %s" %(expected, type(expected)))
        self.assertTrue(isinstance(received,tuple), "\'%s\' should be a tuple, but is a %s" %(received, type(received)))

        #ensure that size of the two tuples is correct
        self.assertEqual(len(expected), len(received), "Consonant tuple should have %s members" %len(received))

        # compare as sets, to ignore order
        self.assertEquals(set(expected), set(received), "Expected tuple \'%s\' but received tuple \'%s\'" %(expected, received))

        print ".... pass"

    def testGetCombination_validInput(self):
        """ get_combination() should return the result of combining a given consonant, vowel tuple """

        print "Testing TamilLetter.get_combination() with valid input (i.e. all possible with consonant, vowel) tuples",

        # get tuple/list of consonants, vowels and combinations
        consonants = TamilLetter.get_consonants()
        vowels = TamilLetter.get_vowels()

        # loop through each consonant, vowel pair
        for consonant in consonants:

            for vowel in vowels:

                expected = COMBINATIONS[(consonant, vowel)]
                received = TamilLetter.get_combination(consonant, vowel)
                self.assertEquals(expected, received, "The combination \'%s\' should have resulted from consonant \'%s\' and vowel \'%s\'. \'%s\' was received" %(expected, vowel, consonant, received))


        print ".... pass"

    def testGetCombination_invalidInput(self):
        """ get_combination() should raise an exception if the input is not a consonant, vowel tuple """

        # get tuple/list of consonants, vowels and combinations
        consonants = TamilLetter.get_consonants()
        vowels = TamilLetter.get_vowels()
        combinations = COMBINATIONS.values()

        # Test every possible vowel, vowel tuple. Should raise a ValueError
        print "Testing TamilLetter.get_combination() with vowel, vowel tuples",

        for vowel1 in vowels:

            for vowel2 in vowels:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(vowel1, vowel2)

        print ".... pass"


        # Test every possible consonant, consonant tuple. Should raise a ValueError
        print "Testing TamilLetter.get_combination() with consonant, consonant tuples",

        for consonant1 in consonants:

            for consonant2 in consonants:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(consonant1, consonant2)

        print ".... pass"


        # Test every possible combination, combination tuple. Should raise a ValueError
        print "Testing TamilLetter.get_combination() with combination, combination tuples",

        for combination1 in combinations:

            for combination2 in combinations:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(combination1, combination2)

        print ".... pass"


        # Test every possible vowel, consonant combination (get_combination) expects consonant, vowel input
        print "Testing TamilLetter.get_combination() with vowel, consonant tuples (get_combination() expects the consonant first, then the vowel)",

        for vowel in vowels:

            for consonant in consonants:

                with self.assertRaises(ValueError):
                    _ = TamilLetter.get_combination(vowel, consonant)

        print ".... pass"


    def testSplitCombination(self):
        """ split_combination() should return the correct consonant, vowel tuple when given a letter """

        # Test for all combinations
        print "Testing TamilLetter.split_combination() with all combinations",

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEquals(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print ".... pass"

        # Test for all consonants
        print "Testing TamilLetter.split_combination() with all consonants",

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:

            expected = (consonant, u'')
            received = TamilLetter.split_combination(consonant)

            self.assertEquals(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], consonant, received[0], received[1]))

        print ".... pass"

        # Test for all vowels
        print "Testing TamilLetter.split_combination() with all combinations",

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEquals(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print ".... pass"

        # Test for aytham
        print "Testing TamilLetter.split_combination() with all combinations",

        for consonant_vowel_tuple in COMBINATIONS:

            expected = consonant_vowel_tuple
            received = TamilLetter.split_combination(COMBINATIONS[consonant_vowel_tuple])

            self.assertEquals(expected, received, "Expected tuple (\'%s\', \'%s\') for combination \'%s\'. Received tuple (\'%s\', \'%s\')" %(expected[0], expected[1], COMBINATIONS[consonant_vowel_tuple], received[0], received[1]))

        print ".... pass"


    def testGetLetterType(self):
        """ get_letter_type() should return the letter type for a given letter (e.g. vowel, consonant, combination, aytham) """

        # Test for Aytham
        print "Testing TamilLetter.get_letter_type() with Aytham (ஃ)",
        letter = AYTHAM
        expected = 'AYTHAM'
        received = TamilLetter.get_letter_type(letter)

        self.assertEquals(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, letter, received))

        print ".... pass"


        # Test for vowels
        print "Testing TamilLetter.get_letter_type() with vowels",

        vowels = TamilLetter.get_vowels()

        for vowel in vowels:
            expected = 'VOWEL'
            received = TamilLetter.get_letter_type(vowel)

            self.assertEquals(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, vowel, received))

        print ".... pass"

        # Test for consonants
        print "Testing TamilLetter.get_letter_type() with consonants",

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:
            expected = 'CONSONANT'
            received = TamilLetter.get_letter_type(consonant)

            self.assertEquals(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, consonant, received))

        print ".... pass"


        # Test for combinations
        print "Testing TamilLetter.get_letter_type() with combinations",

        combinations = COMBINATIONS.values()

        for combination in combinations:
            expected = 'COMBINATION'
            received = TamilLetter.get_letter_type(combination)

            self.assertEquals(expected, received, "Expected letter type \'%s\' for letter \'%s\'. Received \'%s\'" %(expected, combination, received))

        print ".... pass"


    def testGetVowelType_validInput(self):
        """ get_vowel_type() should return the vowel type (kuril or nedil) for all vowels and combination """

        # Test with kuril vowels
        print "Testing TamilLetter.get_vowel_type() with kuril vowels and their combinations",

        for vowel in KURIL_VOWELS:

            expected = 'KURIL'

            # Test the vowel itself
            received = TamilLetter.get_vowel_type(vowel)
            self.assertEquals(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

            # Test for each combination involving a kuril vowel
            combinations = TamilLetter.get_combination_column(vowel).values()
            for combination in combinations:

                received = TamilLetter.get_vowel_type(combination)
                self.assertEquals(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

        print ".... pass"


        # Test with nedil vowels
        print "Testing TamilLetter.get_vowel_type() with nedil vowels and their combinations",

        for vowel in NEDIL_VOWELS:

            expected = 'NEDIL'

            # Test the vowel itself
            received = TamilLetter.get_vowel_type(vowel)
            self.assertEquals(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

            # Test for each combination involving a kuril vowel
            combinations = TamilLetter.get_combination_column(vowel).values()
            for combination in combinations:

                received = TamilLetter.get_vowel_type(combination)
                self.assertEquals(expected, received, "Expected vowel \'%s\' to be of type \'%s\'. Received \'%s\'." %(vowel, expected, received))

        print ".... pass"


    def testGetVowelType_invalidInput(self):
        """ get_vowel_type() should raise a ValueError for Aytham and consonants """

        # Test with aytham
        print "Testing TamilLetter.get_vowel_type() with aytham",

        letter = TamilLetter.get_aytham()
        with self.assertRaises(ValueError):
            _ = TamilLetter.get_vowel_type(letter)

        print ".... pass"


        # Test with all consonants
        print "Testing TamilLetter.get_vowel_type() with consonants",

        consonants = TamilLetter.get_consonants()

        for consonant in consonants:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_vowel_type(consonant)

        print ".... pass"


    def testIsVallinam_TrueCases(self):
        """ is_vallinam() should return True for all vallinam consonants """

        print "Testing TamilLetter.is_vallinam() with vallinam consonants",

        for consonant in VALLINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_vallinam(consonant), "\'%s\' is a vallinam consonant, but is_vallinam() returned False" %consonant)

        print ".... pass"


    def testIsVallinam_FalseCases(self):
        """ is_vallinam() should return False for aytham and for all vowels, combinations and mellinam, idaiyinam and grantha consonants """

        # Test with aytham
        print "Testing TamilLetter.is_vallinam() with aytham",

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_vallinam(letter), "\'%s\' is Aytham, but is_vallinam() returned True" %letter)

        print ".... pass"


        # Test with vowels
        print "Testing TamilLetter.is_vallinam() with vowels",

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_vallinam(vowel), "\'%s\' is a vowel, but is_vallinam() returned True" %vowel)

        print ".... pass"


        # Test with combinations
        print "Testing TamilLetter.is_vallinam() with combinations",

        combinations = COMBINATIONS.values()
        for combination in combinations:

            self.assertFalse(TamilLetter.is_vallinam(combination), "\'%s\' is a combination, but is_vallinam() returned True" %combination)

        print ".... pass"


        # Test with mellinam consonants
        print "Testing TamilLetter.is_vallinam() with mellinam consonant",

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_vallinam(consonant), "\'%s\' is a mellinam consonant, but is_vallinam() returned True" %consonant)

        print ".... pass"


        # Test with idaiyinam consonants
        print "Testing TamilLetter.is_vallinam() with idaiyinam consonant",

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_vallinam(consonant), "\'%s\' is an idaiyinam consonant, but is_vallinam() returned True" %consonant)

        print ".... pass"


    def testIsMellinam_TrueCases(self):
        """ is_mellinam() should return True for all mellinam consonants """

        print "Testing TamilLetter.is_mellinam() with mellinam consonants",

        for consonant in MELLINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_mellinam(consonant), "\'%s\' is a mellinam consonant, but is_mellinam() returned False" %consonant)

        print ".... pass"


    def testIsMellinam_FalseCases(self):
        """ is_mellinam() should return False for aytham and for all vowels, combinations and vallinam, idaiyinam and grantha consonants """

        # Test with aytham
        print "Testing TamilLetter.is_mellinam() with aytham",

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_mellinam(letter), "\'%s\' is Aytham, but is_mellinam() returned True" %letter)

        print ".... pass"


        # Test with vowels
        print "Testing TamilLetter.is_mellinam() with vowels",

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_mellinam(vowel), "\'%s\' is a vowel, but is_mellinam() returned True" %vowel)

        print ".... pass"


        # Test with combinations
        print "Testing TamilLetter.is_mellinam() with combinations",

        combinations = COMBINATIONS.values()
        for combination in combinations:

            self.assertFalse(TamilLetter.is_mellinam(combination), "\'%s\' is a combination, but is_mellinam() returned True" %combination)

        print ".... pass"


        # Test with mellinam consonants
        print "Testing TamilLetter.is_mellinam() with vallinam consonant",

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is a vallinam consonant, but is_mellinam() returned True" %consonant)

        print ".... pass"


        # Test with idaiyinam consonants
        print "Testing TamilLetter.is_mellinam() with idaiyinam consonant",

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is an idaiyinam consonant, but is_mellinam() returned True" %consonant)

        print ".... pass"

        # Test with grantha consonants
        print "Testing TamilLetter.is_mellinam() with grantha consonant",

        for consonant in GRANTHA_CONSONANTS:

            self.assertFalse(TamilLetter.is_mellinam(consonant), "\'%s\' is a grantha consonant, but is_mellinam() returned True" %consonant)

        print ".... pass"


    def testIdaiyinam_TrueCases(self):
        """ is_GRANTHA() should return True for all idaiyinam consonants """

        print "Testing TamilLetter.is_idaiyinam() with idaiyinam consonants",

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertTrue(TamilLetter.is_idaiyinam(consonant), "\'%s\' is a idaiyinam consonant, but is_idaiyinam() returned False" %consonant)

        print ".... pass"


    def testIdaiyinam_FalseCases(self):
        """ is_idaiyinam() should return False for aytham and for all vowels, combinations and vallinam, mellinam and grantha consonants """

        # Test with aytham
        print "Testing TamilLetter.is_idaiyinam() with aytham",

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_idaiyinam(letter), "\'%s\' is Aytham, but is_idaiyinam() returned True" %letter)

        print ".... pass"


        # Test with vowels
        print "Testing TamilLetter.is_idaiyinam() with vowels",

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_idaiyinam(vowel), "\'%s\' is a vowel, but is_idaiyinam() returned True" %vowel)

        print ".... pass"


        # Test with combinations
        print "Testing TamilLetter.is_idaiyinam() with combinations",

        combinations = COMBINATIONS.values()
        for combination in combinations:

            self.assertFalse(TamilLetter.is_idaiyinam(combination), "\'%s\' is a combination, but is_idaiyinam() returned True" %combination)

        print ".... pass"


        # Test with idaiyinam consonants
        print "Testing TamilLetter.is_idaiyinam() with vallinam consonant",

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is a vallinam consonant, but is_idaiyinam() returned True" %consonant)

        print ".... pass"


        # Test with idaiyinam consonants
        print "Testing TamilLetter.is_idaiyinam() with mellinam consonant",

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is an mellinam consonant, but is_idaiyinam() returned True" %consonant)

        print ".... pass"

        # Test with grantha consonants
        print "Testing TamilLetter.is_idaiyinam() with grantha consonant",

        for consonant in GRANTHA_CONSONANTS:

            self.assertFalse(TamilLetter.is_idaiyinam(consonant), "\'%s\' is an grantha consonant, but is_idaiyinam() returned True" %consonant)

        print ".... pass"


    def testIsGrantha_TrueCases(self):
        """ is_grantha() should return True for all grantha consonants """

        print "Testing TamilLetter.is_grantha() with grantha consonants",

        for consonant in GRANTHA_CONSONANTS:

            self.assertTrue(TamilLetter.is_grantha(consonant), "\'%s\' is a grantha consonant, but is_grantha() returned False" %consonant)

        print ".... pass"


    def testIsGrantha_FalseCases(self):
        """ is_grantha() should return False for aytham and for all vowels, combinations and vallinam, mellinam and idaiyinam consonants """

        # Test with aytham
        print "Testing TamilLetter.is_grantha() with aytham",

        letter = AYTHAM
        self.assertFalse(TamilLetter.is_grantha(letter), "\'%s\' is Aytham, but is_grantha() returned True" %letter)

        print ".... pass"


        # Test with vowels
        print "Testing TamilLetter.is_grantha() with vowels",

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            self.assertFalse(TamilLetter.is_grantha(vowel), "\'%s\' is a vowel, but is_grantha() returned True" %vowel)

        print ".... pass"


        # Test with combinations
        print "Testing TamilLetter.is_grantha() with combinations",

        combinations = COMBINATIONS.values()
        for combination in combinations:

            self.assertFalse(TamilLetter.is_grantha(combination), "\'%s\' is a combination, but is_grantha() returned True" %combination)

        print ".... pass"


        # Test with grantha consonants
        print "Testing TamilLetter.is_grantha() with vallinam consonant",

        for consonant in VALLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is a vallinam consonant, but is_grantha() returned True" %consonant)

        print ".... pass"


        # Test with grantha consonants
        print "Testing TamilLetter.is_grantha() with mellinam consonant",

        for consonant in MELLINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is an mellinam consonant, but is_grantha() returned True" %consonant)

        print ".... pass"

        # Test with grantha consonants
        print "Testing TamilLetter.is_grantha() with idaiyinam consonant",

        for consonant in IDAIYINAM_CONSONANTS:

            self.assertFalse(TamilLetter.is_grantha(consonant), "\'%s\' is an idaiyinam consonant, but is_grantha() returned True" %consonant)

        print ".... pass"

    def testGetCombinationColumn_validInput(self):
        """ get_combination_column() should return a dictionary mapping consonant -> combination for a given vowel """

        print "Testing TamilLetter.get_combination_column() with vowels",

        vowels = TamilLetter.get_vowels()

        # ensure that the correct row is returned for each vowel
        for vowel in vowels:

            expected = COMBINATIONS_BY_VOWEL[vowel]
            received = TamilLetter.get_combination_column(vowel)

            self.assertEquals(expected, received, "Expected dictionary %s to be equal to dictionary %s" %(expected, received))


        print ".... pass"


    def testGetCombinationColumn_invalidInput(self):
        """ get_combination_column() should raise a ValueError for all consonants, combinations and aytham """

        # Test Aytham
        print "Testing TamilLetter.get_combination_column() with Aytham (ஃ) - expecting ValueError",

        letter = AYTHAM

        with self.assertRaises(ValueError):
            _ = TamilLetter.get_combination_column(letter)

        print ".... pass"

        # Test consonants
        print "Testing TamilLetter.get_combination_column() with consonants - expecting ValueError",

        consonants = TamilLetter.get_consonants()
        for consonant in consonants:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_column(consonant)

        print ".... pass"

        # Test Combinations
        print "Testing TamilLetter.get_combination_column() with combinations - expecting ValueError",

        combinations = COMBINATIONS.values()

        for combination in combinations:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_column(combination)

        print ".... pass"


    def testGetCombinationRow_validInput(self):
        """ get_combination_row() should return a dictionary mapping vowel -> combination for a given consonant """

        print "Testing TamilLetter.get_combination_row() with consonants - Expecting a dictionary of vowel->combination mappings for the given consonant",

        consonants = TamilLetter.get_consonants()

        # ensure that the correct row is returned for each consonant
        for consonant in consonants:

            expected = COMBINATIONS_BY_CONSONANT[consonant]
            received = TamilLetter.get_combination_row(consonant)

            self.assertEquals(expected, received, "Expected dictionary %s to be equal to dictionary %s" %(expected, received))


        print ".... pass"


    def testGetCombinationRow_invalidInput(self):
        """ get_combination_row() should raise a ValueError for all consonants, combinations and aytham """

        # Test Aytham
        print "Testing TamilLetter.get_combination_row() with Aytham (ஃ) - expecting ValueError",

        letter = AYTHAM

        with self.assertRaises(ValueError):
            _ = TamilLetter.get_combination_row(letter)

        print ".... pass"

        # Test consonants
        print "Testing TamilLetter.get_combination_row() with vowels - expecting ValueError",

        vowels = TamilLetter.get_vowels()
        for vowel in vowels:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_row(vowel)

        print ".... pass"

        # Test Combinations
        print "Testing TamilLetter.get_combination_row() with combinations - expecting ValueError",

        combinations = COMBINATIONS.values()

        for combination in combinations:

            with self.assertRaises(ValueError):
                _ = TamilLetter.get_combination_row(combination)

        print ".... pass"


    def testGetCombinationEndings(self):
        """ get_combination_endings() should return a tuple of all the combination endings """

        print "Testing TamilLetter.get_combination_endings()",

        expected_tuple = COMBINATION_ENDINGS_TUPLE
        received_tuple = TamilLetter.get_combination_endings()

        self.assertEqual(set(expected_tuple), set(received_tuple), "Expected tuple \'%s\' but received \'%s\'" %(expected_tuple, received_tuple) )

        print ".... pass"



def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TamilLetterTest))
    return suite

def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)


if __name__ == '__main__':
    main()
