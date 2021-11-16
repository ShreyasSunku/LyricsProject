from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Lyrics.models import Actor
from .serializers import ActorSerializer
from rest_framework.parsers import JSONParser


class ActorList(APIView):
    def get(self, request):
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)
        return Response(serializer.data)

    def post(self):
        pass


def Actor_view(request):
    if request.method == 'GET':
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)