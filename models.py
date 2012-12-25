from django.db import models

# Create your models here.
# Part of Speech
class PartOfSpeech(models.Model):
    tamil           = models.CharField(max_length=20)   # Tamil Part of Speech
    english         = models.CharField(max_length=20)   # Equivalent English PoS 
    
    # pedagogical information
    example         = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    
    # string representation of word: display Tamil
    def __unicode__(self):
        return  u'%s / %s:\n%s' % (self.tamil, self.english, self.description)
    
    class Meta:
        verbose_name_plural = "Parts of speech"
    

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
        return  u'%s' % (self.tamil)

# Finite choice of letters types
LETTER_TYPES = (
    ('vow', 'Vowel' ),
    ('con', 'Consonant'),
    ('cmb', 'Combination'),    
)

# A Tamil letter
class Letter(models.Model):
    tamil       = models.CharField(max_length=30)   # Tamil letter
    english     = models.CharField(max_length=50)   # English equivalent (Unicode/Anjal)
    
    # whether the letter is a vowel, consonant or combination
    type        = models.CharField(max_length=3, choices=LETTER_TYPES)
    
    # audio file (preferably .ogg format) with pronunciation     
    audio_file  = models.FileField(null=True, blank=True, upload_to='/media/letters/')
    
    # string representation of the letter: display Tamil
    def __unicode__(self):
        return  u'%s' % (self.tamil)
    

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
    
