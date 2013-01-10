# -*- coding: utf-8 -*-
#!/usr/bin/python

# import TamilLetter class
from TamilLetter import TamilLetter


# Add skeletal outline for functions. Removed redundant function. Modified import command

class TamilWord:
    """ Module to handle the processing of Tamil words """
    
    def __init__(self, text=u''):
        """ Constructor for TamilWord class. Takes a unicode string composed of Tamil characters as an optional input. """ 
        
        self._text          = u''
        self._syllables     = []
        self._letters       = []
        
        # if text is entered, call the text property's setter (which generates the syllables and letters lists)
        if text: self.text(text)
        
    
    def __getitem__(self,index):
        """ Read the letter at the given position in the letters list """
        
        self._letters[index]
    
    
    def __setitem__(self, index, value):
        """ Modify a member at the given position in the letters list """
        
        self._letters[index] =  value
        
    
    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
    
        # if valid text is entered, calculate syllables and letters
    
        if self.validate():
            self.text = text
            
            self._letters = self.split_letters(text)
            #TODO: calculate syllables
        
        # if invalid text is entered, initialize to empty string
        else:
            self.text = u''
    
    
    @property
    def syllables(self):
        return self._syllables
    
    @property
    def letters(self):
        return self._letters
    
            
    def validate(self):
        """ Checks whether the given word is valid """   
        
        # simple test: every element of the string has to be a valid Tamil character
        for codepoint in self.text:
            TamilLetter.validate_letter(codepoint)
         
        
        #TODO: implement method this more thoroughly
        #TODO: check for pulli or combination_ending at the beginning of a word 
        
        return True

    
    @staticmethod
    def split_letters(word=u''):
        """ Returns the graphemes (i.e. the Tamil characters) in a given word as a list """   
        
        # ensure that the word is a valid word
        TamilWord.validate_word(word)
        
        # list (which will be returned to user)
        letters = []
        
        # a tuple of all combination endings and of all அ combinations
        combination_endings = TamilLetter.get_combination_endings()
        a_combinations = TamilLetter.get_combination_column(u'அ').values()
        
        # loop through 
        for codepoint in word: 
            
            # if codepoint is an அ combination, a vowel, aytham or a space, add it to the list 
            if codepoint in a_combinations or TamilLetter.is_whitespace(codepoint) or TamilLetter.is_vowel(codepoint) or TamilLetter.is_aytham(codepoint):
                letters.append(codepoint)
            
            # if codepoint is a combination ending or a pulli ('்'), add it to the end of the previously-added codepoint
            elif codepoint in combination_endings or codepoint==TamilLetter.get_pulli():
                
                # ensure that at least one character already exists
                if len(letters) > 0:
                    letters[-1] = letters[-1] + codepoint 
                
                # otherwise raise an Error. validate_word() should catch this, however
                else:
                    raise ValueError("Unknown error: The combination ending %s cannot be the first character of a word" %(codepoint))
            
            # if codepoint was neither a vowel, aytham, a pulli or a combination ending, an unexpected error has occurred
            else:
                raise ValueError("Unknown error: The codepoint \'%s\' in word %s is neither a vowel, consonant, combination or aytham" %(codepoint, word))
            
        
        #TODO: Write extensive test cases for this
        
        return letters
        
    @staticmethod
    def print_letters(word = u'', delimiter="-"):
        """ Prints all the graphemes in a word, separated by a delimiter (default: "-") """
        
        for letter in TamilWord.get_letters(word):
            print letter, delimiter,
        
        # go to new line
        print
        
    
    @staticmethod
    def split_syllables(letters = []):
        """ Returns the syllables in a given word as a list """   
        
        ## Generic algorithm:
        ## Each vowel and combination is its own syllable. Consonants and aytham get added to the end of the previous syllable
        
        # ensure that the word is a valid word
        TamilWord.validate_word(''.join(letters))
        
        # initialize empty list
        syllables = []
        
        # loop through letters in the word
        for letter in letters: 
            
            # if letter is a vowel or combination, it gets its own syllable 
            if TamilLetter.is_combination(letter) or TamilLetter.is_vowel(letter):
                syllables.append(letter)
            
            # if codepoint is a consonant or aytham, add it to the end of the previously-added codepoint
            elif TamilLetter.is_consonant(letter) or TamilLetter.is_aytham(letter):
                
                # ensure that at least one character already exists
                if len(syllables) > 0:
                    syllables[-1] = syllables[-1] + letter
                
                # if the first letter is a consonant (probably b/c it' s a loanword), add it to the beginning of the string
                else:
                    syllables.append(letter) 
                
            # if codepoint was neither a vowel, aytham, a pulli or a combination ending, an unexpected error has occurred
            else:
                raise Exception("Unknown error: The letter \'%s\' in word %s is neither a vowel, consonant, combination or aytham" %(letter, ''.join(letters)))
            
        
        #TODO: Write extensive test cases for this

        
    
           
        
    




