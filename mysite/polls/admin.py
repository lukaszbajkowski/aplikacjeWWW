from django.contrib import admin

from .models import Question, Choice, Value, Person, Osoba

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Value)
admin.site.register(Person)
admin.site.register(Osoba)
