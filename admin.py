from apps.amuthaa.models import PartOfSpeech, Word, Letter, Rule
from django.contrib import admin

class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ('english', 'tamil')

admin.site.register(PartOfSpeech, PartOfSpeechAdmin)
admin.site.register(Letter)
admin.site.register(Word)
admin.site.register(Rule)

