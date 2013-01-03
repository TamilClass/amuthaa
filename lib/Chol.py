# -*- coding: utf-8 -*-
#!/usr/bin/python

# import Ezhuthu class
try:
    from learntamil.apps.amuthaa.lib.Ezhuthu import Ezhuthu
except ImportError:
    import sys
    from os.path import join, abspath, dirname
    parentpath = abspath(join(dirname(__file__), '..'))
    srcpath = join(parentpath, 'lib')
    sys.path.append(srcpath)
    from Ezhuthu import Ezhuthu


class Chol:
    
    @staticmethod
    def get_letters(word = ""):
        #TODO: Implement this
        pass
    
    
    
    @staticmethod    
    def final_letter(word = ""):
        """ 
        Returns the final letter in a word
        """
        
        # ensure that word has at least one character
        if len(word) == 0:
            raise TypeError("Input must be at least character long")
        
        # return last letter of string
        #TODO: Fix this so that it takes graphemes into account
        return word[-1]    