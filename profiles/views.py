import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from authentication.utils import AllowAnyOnGet
from rest_framework.response import Response
from rest_framework import status
from profiles.serializers import UserSerializerUpdate
from events.models import Event
from events.serializers import EventSerializer


# Create your views here.
class ProfileDetail(APIView):
    permission_classes = (AllowAnyOnGet,)

    def get(self, request, format=None):
        user = request.user
        current_datetime = datetime.datetime.now()

        event_soon = Event.objects.filter(
            participants=user, finish__gte=current_datetime).order_by('start')
        event_created = Event.objects.filter(created_by=user).order_by('start')
        event_done = Event.objects.filter(
            participants=user, finish__lte=current_datetime).order_by('start')

        data = {}
        data['user'] = UserSerializer(user).data
        data['event_soon'] = EventSerializer(event_soon, many=True).data
        data['event_created'] = EventSerializer(event_created, many=True).data
        data['event_done'] = EventSerializer(event_done, many=True).data

        return Response({"message": "success", "data": data})

    def put(self, request, format=None):
        user = request.user
        data = request.data
        serializer = UserSerializerUpdate(
            user, data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": UserSerializer(user).data})
        return Response({"message": "errors", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
