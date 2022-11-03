from django.contrib import admin

from .models import Question, Choice, Value, Person, Team


class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'nazwisko', 'shirt_size', 'team']

class DruzynaAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Value)
admin.site.register(Person, PersonAdmin)
admin.site.register(Team, DruzynaAdmin)
