import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Value(models.Model):
    value = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color + " " + str(self.value)


class Person(models.Model):
    # lista wartości do wyboru w formie krotek
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    # wskazanie listy poprzez przypisanie do parametru choices
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Osoba(models.Model):
    MONTH = (
        ('1', 'Styczeń'),
        ('2', 'Luty'),
        ('3', 'Marzec'),
        ('4', 'Kwiecień'),
        ('5', 'Maj'),
        ('6', 'Czerwiec'),
        ('7', 'Lipiec'),
        ('8', 'Sierpień'),
        ('9', 'Wrzesień'),
        ('10', 'Październik'),
        ('11', 'Listopad'),
        ('12', 'Grudzień'),
    )
    imie = models.CharField(max_length=20, null=False, blank=False)
    nazwisko = models.CharField(max_length=20, null=False, blank=False)
    miesiac_urodzenia = models.CharField(default=1, max_length=2, choices=MONTH)
    data_dodania = models.DateField(auto_now=True)
