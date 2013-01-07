# -*- coding: utf-8 -*-
#!/usr/bin/python

from django.db import models

# Create your models here.
# Part of Speech
class PartOfSpeech(models.Model):
    tamil           = models.CharField(max_length=20)   # Tamil Part of Speech
    english         = models.CharField(max_length=20)   # Equivalent English PoS 
    
    # pedagogical information
    example         = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    
    # string representation of part of speech: display Tamil
    def __unicode__(self):
        return  u'%s / %s' % (self.english, self.tamil)
    
    class Meta:
        verbose_name_plural = "Parts of speech"
    

# Finite choice of letters types
VERB_TENSE_TYPES = (
    ('pres', 'Present Tense'),    
    ('futr', 'Future Tense'),    
    ('past', 'Past Tense'),    
)

# The different verb stem transformations under past, present and future tenses
# This would serve as a foreign key to the VerbClass model so that each VerbClass
# can match itself up with a particular verb stem
class VerbStem(models.Model):
    
    # the actual verb stem. E.g. for செய் would be வ் in the past tense 
    stem                = models.CharField(max_length=10)
    
    # in the present tense, there are two possible stems: (க்)கிற் & (க்)க்கிற்
    # the first of those would be the default
    # this field indicates whether the default is being used
    default             = models.BooleanField(default=True)
    
    # whether the stem should remove the last character
    remove_last_char    = models.BooleanField(default=False)


class VerbRoot(models.Model):
    name                = models.CharField(max_length=30)
    
    verb_class          = models.ForeignKey('VerbClass')
    

# Verb class
class VerbClass(models.Model):
    category            = models.IntegerField()
    subcategory         = models.CharField(max_length=1, null=True, blank=True, default="")

    # pedagogical information
    example             = models.TextField(null=True, blank=True)
    description         = models.TextField(null=True, blank=True)
    
    # identification pattern: last letter
    ending_letters      = models.ManyToManyField('Letter')
    
    # identification pattern: regex pattern matching formula  
    ending_pattern      = models.CharField(max_length=10, null=True, blank=True)
    
    # present tense indicator stem. There are two valid stems for all verbs
    present_stem        = models.CharField(max_length=10)
    present_stem_alt    = models.CharField(max_length=10)   
    
    #
   

# A Tamil word
class Word(models.Model):
    tamil           = models.CharField(max_length=30)   # Tamil spelling
    english         = models.CharField(max_length=50)   # English spelling
    
    # pedagogical information
    example         = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    
    # the part of speech that this word is
    part_of_speech  = models.ForeignKey('PartOfSpeech')
    
    # whether a word has been verified by an administrator
    # this will allow words that have been crowdsourced to be checked for 
    # spelling, etc. before being used in lessons and exercises
    verified        = models.BooleanField(blank=True, default=False)

    audio_file      = models.FileField(null=True, blank=True, upload_to='/media/words/')

    
    # string representation of word: display Tamil
    def __unicode__(self):
        return  u'%s / %s' % (self.tamil, self.english)


# Finite choice of letters types
LETTER_TYPES = (
    ('ay', 'Aytham'),
    ('sv', 'Short Vowel' ),
    ('lv', 'Long Vowel'),
    ('hc', 'Hard Consonant'),    
    ('sc', 'Soft Consonant'),
    ('mc', 'Medium Consonant'),    
    ('gc', 'Grantha Consonant'),    
    ('cb', 'Combination'),    
)

# A Tamil letter
class Letter(models.Model):
    tamil       = models.CharField(max_length=30)   # Tamil letter
    english     = models.CharField(max_length=50)   # English equivalent (Unicode/Anjal)
    
    # whether the letter is a vowel, consonant or combination
    type        = models.CharField(max_length=2, choices=LETTER_TYPES)
    
    # audio file (preferably .ogg format) with pronunciation     
    audio_file  = models.FileField(null=True, blank=True, upload_to='/media/letters/')
    
    # string representation of the letter: display Tamil
    def __unicode__(self):
        return  u'%s / %s' % (self.english, self.tamil)
    

# Finite choice of rule types
RULE_TYPES = (
    ('al', 'Alphabet'),
    ('gr', 'Grammar' ),
    ('sp', 'Spoken Tamil'),    
)

# An alphabet or grammar rule 
class Rule(models.Model):
    
    # the name of the rule
    title       = models.CharField(max_length=30)
    
    # whether the rule is an alphabet, grammar or spoken Tamil rule
    type        = models.CharField(max_length=2, choices=LETTER_TYPES)    
    
    # a description of the rule
    description = models.TextField()
    
