from polls.models import Person
from polls.serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

person = Person(first_name='Patryk', nazwisko='Biały', shirt_size='L')
person.save()

serializer = PersonSerializer(person)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = PersonSerializer(data=data)

deserializer.is_valid()
deserializer.errors

deserializer.fields
repr(deserializer)

deserializer.validated_data
deserializer.save()
deserializer.data


from polls.models import Team
from polls.serializers import TeamSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

team = Team(name='Pogoń Szczecin', country='PL')
team.save()

serializer = TeamSerializer(team)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = TeamSerializer(data=data)
deserializer.errors
deserializer.fields
repr(deserializer)
deserializer.validated_data
deserializer.save()
deserializer.data
