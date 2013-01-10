# -*- coding: utf-8 -*-

=======
amuthaa
=======

amuthaa provides a number of tools to handle the processing of Tamil letters and words. 

Here is a sampling of the TamilLetter class::
	
	>>> from amuthaa import TamilLetter
	>>> 
	>>> letter = u'ம'
	>>> 
	>>> TamilLetter.is_aytham(letter)
	False
	>>> TamilLetter.is_vowel(letter)
	False
	>>> TamilLetter.is_consonant(letter)
	False
	>>> TamilLetter.is_combination(letter)
	True
	>>> 
	>>> consonant, vowel = TamilLetter.split_combination(letter)
	>>> print consonant
	ம்
	>>> print vowel
	அ
	>>> 
	>>> TamilLetter.is_consonant(consonant)
	True
	>>> TamilLetter.is_vowel(vowel)
	True
	>>> 
	>>> print TamilLetter.get_combination(u'க்', u'ஐ')
	கை
	>>> 
	>>> 
	>>> vowels = TamilLetter.get_vowels()
	>>> 
	>>> for v in vowels:
	...     print v, TamilLetter.get_vowel_type(v)
	... 
	அ KURIL
	இ KURIL
	ஆ NEDIL
	உ KURIL
	ஈ NEDIL
	ஊ NEDIL
	ஏ NEDIL
	எ KURIL
	ஐ NEDIL
	ஓ NEDIL
	ஒ KURIL
	ஔ NEDIL
	>>> 
	>>> consonants = TamilLetter.get_consonants()    
	>>>  
	... for c in consonants:
	...     print c, TamilLetter.get_consonant_type(c)
	... 
	ய் IDAIYINAM
	ர் IDAIYINAM
	ல் IDAIYINAM
	வ் IDAIYINAM
	ழ் IDAIYINAM
	ள் IDAIYINAM
	ஜ் GRANTHA
	ஷ் GRANTHA
	ஸ் GRANTHA
	ஹ் GRANTHA
	க் VALLINAM
	ச் VALLINAM
	ட் VALLINAM
	த் VALLINAM
	ப் VALLINAM
	ற் VALLINAM
	ங் MELLINAM
	ஞ் MELLINAM
	ண் MELLINAM
	ந் MELLINAM
	ம் MELLINAM
	ன் MELLINAM
	>>> 
	>>> foreign_letters = [
	...                    u'ഢ', # Malayalam
	...                    u'ම', # Sinhala
	...                    u'న', # Telugu
	...                    u'ನ', # Kannada 
	...                    u'औ', # Devanagari (Sanskrit, Hindi, Marathi)
	...                    u'ល', # Khmer (Cambodia)
	...                    u'a', # Latin                       
	...                    ]
	>>> 
	>>> for f in foreign_letters:
	...     print "The letter %s is in the %s script" %(f, TamilLetter.get_script_name(f))
	... 
	The letter ഢ is in the MALAYALAM script
	The letter ම is in the SINHALA script
	The letter న is in the TELUGU script
	The letter ನ is in the KANNADA script
	The letter औ is in the DEVANAGARI script
	The letter ល is in the KHMER script
	The letter a is in the LATIN script
	>>> 
