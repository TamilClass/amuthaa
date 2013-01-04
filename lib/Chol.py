# -*- coding: utf-8 -*-
#!/usr/bin/python

# import Ezhuthu class
from Ezhuthu import Ezhuthu


# Add skeletal outline for functions. Removed redundant function. Modified import command

class Chol:
    """
    Module to handle the processing of Tamil words
    """

    @staticmethod
    def validate_word(word=u''):
        """ docstring """   
        #TODO: add docstring
        
        #TODO: implement method
        #TODO: check for pulli or combination_ending at the beginning of a word 
        
    @staticmethod
    def validate_noun_class(noun_class = 0):
        """ docstring """
        #TODO: add docstring
        
        #TODO: implement method

    
    @staticmethod
    def validate_verb_class(noun_class = 0):
        """ docstring """
        #TODO: add docstring
        
        #TODO: implement method
    
    
    @staticmethod
    def split_letters(word=u''):
        """ Returns the graphemes (i.e. the Tamil characters) in a given word as a list """   
        
        # ensure that the word is a valid word
        Chol.validate_word(word)
        
        # list (which will be returned to user)
        letters = []
        
        # a tuple of all combination endings and of all அ combinations
        combination_endings = Ezhuthu.get_combination_endings()
        a_combinations = Ezhuthu.get_combination_column(u'அ').values()
        
        # loop through 
        for codepoint in word: 
            
            # if codepoint is an அ combination, a vowel, aytham or a space, add it to the list 
            if codepoint in a_combinations or Ezhuthu.is_whitespace(codepoint) or Ezhuthu.is_vowel(codepoint) or Ezhuthu.is_aytham(codepoint):
                letters.append(codepoint)
            
            # if codepoint is a combination ending or a pulli ('்'), add it to the end of the previously-added codepoint
            elif codepoint in combination_endings or codepoint==Ezhuthu.get_pulli():
                
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
        
        for letter in Chol.get_letters(word):
            print letter, delimiter,
        
        # go to new line
        print
        
    
    
    @staticmethod
    def num_syllables(word=u''):
        """ docstring """
        #TODO: add docstring
        
        #TODO: Implement method
        
    
    @staticmethod
    def add_noun_suffix(word = u'', word_class=0, suffix = ''):
        """ docstring """
        #TODO: add docstring
        
        #TODO: Implement method
    
    
    @staticmethod
    def pluralize(word = u''):
        """ docstring """
        #TODO: add docstring
        
        #TODO: Implement method
        
    
          
    
    @staticmethod
    def get_noun_root(word):
            """ docstring """
        #TODO: add docstring
        
        #TODO: Implement method
        

    @staticmethod
    def get_conjugation(verb=u'', verbclass=0, tense='PRESENT'):
            """ docstring """
        #TODO: add docstring
        
        #TODO: Implement method


