from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer


class PersonList(APIView):
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def person_list(request):
#     if request.method == 'GET':
#         persons_list = Person.objects.filter(first_name__contains = 'a')
#         serializer = PersonSerializer(persons_list, many=True)
#         return Response(serializer.data)

class PersonDetail(APIView):
    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def person_detail(request, pk):
#     try:
#         person = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         person = Person.objects.get(pk=pk)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = PersonSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         person.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team = Team.objects.get(pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
