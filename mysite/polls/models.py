import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

MONTHS = (
    (1, 'Styczeń'),
    (2, 'Luty'),
    (3, 'Marzec'),
    (4, 'Kwiecień'),
    (5, 'Maj'),
    (6, 'Czerwiec'),
    (7, 'Lipiec'),
    (8, 'Sierpień'),
    (9, 'Wrzesień'),
    (10, 'Październik'),
    (11, 'Listopad'),
    (12, 'Grudzień'),
)


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


class Team(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(validators=[MinLengthValidator(2)], max_length=2, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.country = self.country.upper()
        return super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    nazwisko = models.CharField(max_length=20, null=False, blank=False)
    miesiac_dodania = models.IntegerField(choices=MONTHS, default=datetime.date.today().month)
    data_dodania = models.DateField(auto_now_add=True)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Drużyna")

    def __str__(self):
        return self.first_name + " " + self.nazwisko

    class Meta:
        ordering = ["nazwisko"]


