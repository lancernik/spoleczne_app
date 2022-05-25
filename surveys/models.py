from django.db import models

# Create your models here.




class Survey(models.Model):
    #sample_text = models.CharField(verbose_name='Imię imax_length=1024, blank=True, null=True)
    question_1 = models.BooleanField(verbose_name="Czy jesteś studentem lub absolwentem Akademii Górniczo-Hutniczej w Krakowie?", blank=True, null=True, default=False)
    question_2 = models.BooleanField(verbose_name="Czy jesteś obecnie studentem?", blank=True, null=True, default=False)
    question_3 = models.IntegerField(verbose_name='Ile masz lat?')

    question_4_choices = (('1', 'studiuję, jeszcze nie mam dyplomu'),('2', 'wyższe '),('3', 'zawodowe '),('4', 'zawodowe+wyższe '))
    question_4 = models.CharField(verbose_name='Jakie posiadasz wykształcenie?',max_length=1024, choices=question_4_choices)

    question_5_choices = (('1', 'licencjat'),('2', 'inżynier '),('3', 'magister '),('4', 'doktor '),('5', 'doktor habilitowany '),('6', 'profesor '))
    question_5 = models.CharField(verbose_name='Jakie posiadasz wykształcenie?',max_length=1024, choices=question_4_choices)

    question_6 = models.IntegerField(verbose_name='Jak nazywa/ł się twój kierunek studiów?')
    question_7 = models.IntegerField(verbose_name=' na jakim jesteś/byłeś  wydziale?')

    question_8 = models.IntegerField(verbose_name='Ile wynoszą twoje miesięczne zarobki brutto?', default=48)
    question_9 = models.IntegerField(verbose_name='W jakim wymiarze godzin pracujesz?(dodać więcej godzin)', default=48)

    question_10 = models.IntegerField(verbose_name='Ile masz lat doświadczenia? (Rozpoczętych lat)')
    question_11 = models.BooleanField(verbose_name="Czy jesteś zadowolony ze swoich zarobków?", blank=True, null=True, default=False)
    question_12 = models.BooleanField(verbose_name="Czy uważasz, że osoby w twojej firmie na tym samym stanowisku zarabiają więcej?", blank=True, null=True, default=False)
    question_13 = models.BooleanField(verbose_name="Czy pracujesz zdalnie?", blank=True, null=True, default=False)

    question_14 = models.IntegerField(verbose_name='Ile uważasz, że powinieneś zarabiać na swoim stanowisku?')
    question_15 = models.IntegerField(verbose_name='ilu firmach pracowałeś dotychczas(łącznie z obecną)?')

    question_16_choices = (('1', 'własny biznes'),('2', 'startup '),('3', 'firma zatrudniająca 1-25 pracowników '),
    ('4', 'firma zatrudniająca 26-50 pracowników '),('5', 'firma zatrudniająca 51-100  pracowników '),('6', 'firma zatrudniająca 101-300 pracowników ')
    ,('7', 'firma zatrudniająca 301-500 pracowników '),('8', 'firma zatrudniająca 500+ '))
    question_16 = models.CharField(verbose_name='Twoja obecna firma to:',max_length=1024, choices=question_16_choices)

    
    question_17 = models.BooleanField(verbose_name="Umowa o pracę", blank=True, null=True, default=False)
    question_18 = models.BooleanField(verbose_name="Umowa o dzieło", blank=True, null=True, default=False)
    question_19 = models.BooleanField(verbose_name="Umowa zlecenie", blank=True, null=True, default=False)
    question_20 = models.BooleanField(verbose_name="B2B", blank=True, null=True, default=False)

    question_21 = models.CharField(verbose_name='Na jakim stanowisku pracujesz?',max_length=1024, choices=question_16_choices)
    question_22 = models.BooleanField(verbose_name="Czy pracujesz w zawodzie?", blank=True, null=True, default=False)
