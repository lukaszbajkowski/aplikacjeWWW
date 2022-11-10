from rest_framework import serializers
from .models import Person


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'miesiac_dodania', 'shirt_size', 'team']
        read_only_fields = ['id']
