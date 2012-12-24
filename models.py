from django.db import models

# Create your models here.
# Part of Speech
class PartOfSpeech(models.Model):
    tamil           = models.CharField(max_length=20)   # Tamil Part of Speech
    english         = models.CharField(max_length=20)   # Equivalent English PoS 
    
    # ppedagogical information
    example         = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)

    
    # string representation of word: display Tamil
    def __unicode__(self):
        return  u'%s / %s:\n%s' % (self.tamil, self.english, self.description)
    

# A Tamil word
class Word(models.Model):
    tamil           = models.CharField(max_length=30)   # Tamil spelling
    english         = models.CharField(max_length=50)   # English spelling
    
    # pedagogical information
    example         = models.TextField(null=True, blank=True)
    description     = models.TextField(null=True, blank=True)
    
    # the part of speech that this word is
    part_of_speech  = models.ForeignKey('PartOfSpeech')
    
    # lesson number in which word was taught
    lesson          = models.IntegerField(null=True, blank=True)
    
    # whether word was directly taught 
    # the alternative is if the word is implied, i.e. it isn't directly taught
    #   but can be figured out with the knowledge the student has at that lesson
    taught          = models.BooleanField(null=True, blank=True, default=False)
    
    # whether a word has been verified by an administrator
    # this will allow words that have been crowdsourced to be checked for 
    # spelling, etc. before being used in lessons and exercises
    verified        = models.BooleanField(null=True, blank=True, default=False)

    audio_file      = models.FileField(upload_to='')

    
    # string representation of word: display Tamil
    def __unicode__(self):
        return  u'%s' % (self.tamil)

# Finite choice of letters types
LETTER_TYPES = (
    ('vw', 'Vowel' ),
    ('cn', 'Consonant'),
    ('cb', 'Combination'),    
)

# A Tamil letter
class Letter(models.Model):
    tamil       = models.CharField(max_length=30)   # Tamil letter
    english     = models.CharField(max_length=50)   # English equivalent (Unicode/Anjal)
    
    # whether the letter is a vowel, consonant or combination
    type        = models.CharField(max_length=2, choices=LETTER_TYPES)
    
    # lesson number in which word was taught
    lesson      = models.IntegerField()
    
    # The "Tamil Course for European Schools" lesson number
    tces_lesson = models.IntegerField()
    
    # audio file (preferably .ogg format) with pronunciation     
    audio_file  = models.FileField()
    
    # string representation of the letter: display Tamil
    def __unicode__(self):
        return  u'%s' % (self.tamil)
