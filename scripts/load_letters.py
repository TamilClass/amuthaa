import csv
from apps.amuthaa.models import Letter

# initiative Django environment settings
from django.core.management import setup_environ
import learntamil.settings.stage
setup_environ(learntamil.settings.stage)


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]
        
        
def import_letter(letter_tamil, letter_english, letter_type):
    
    l = Letter(tamil=letter_tamil, english=letter_english, type=letter_type)
    l.save()
    print Letter.objects.all()


def main():
    filename = '../../../docs/data/letters.csv'
    reader = unicode_csv_reader(open(filename))

    for letter_tamil, letter_english, letter_type in reader:
        import_letter(letter_tamil, letter_english, letter_type)

if __name__ == "__main__":
    main()

