from rest_framework import serializers
from .models import Person, Team, MONTHS, SHIRT_SIZES


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS, default=MONTHS[0][0])
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), allow_null=True)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.team = validated_data.get('team', instance.team)
        instance.save()
        return instance


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance

