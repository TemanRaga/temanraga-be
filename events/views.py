import imp
from django.shortcuts import render
from django.http.response import Http404
from authentication.utils import AllowAnyOnGet
from events.models import Event
from events.serializers import EventSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from authentication.models import User

# Create your views here.
class EventList(APIView):
    permission_classes = (AllowAnyOnGet,)

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True, context= {'request': request})
        return Response({"message": "success", "data": serializer.data})

    def post(self, request, format=None):
        try:
            description = request.data.get('description')
            name = request.data.get('name')
            location = request.data.get('location')
            image = request.data.get('image')
            date = request.data.get('date')
            start = request.data.get('start')
            finish = request.data.get('finish')
            gender = request.data.get('gender')
            max_participants = request.data.get('max_participants')
            user = request.user
            event = Event.objects.create(created_by=user, description=description, name=name, location=location, date=date, start=start, finish=finish, gender=gender, max_participants=max_participants, image=image)
            event.participants.add(request.user)
            serializer = EventSerializer(event, context= {'request': request})
            return Response({"message": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "errors", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    permission_classes = (AllowAnyOnGet,)

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, context= {'request': request})
        return Response({"message": "success", "data": serializer.data})

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        if event.created_by != request.user:
            return Response({
                "status": 403,
                "message": "bukan pemilik event"
            }, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        serializer = EventSerializer(event, data, context= {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": serializer.data})
        return Response({"message": "errors", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        if event.created_by != request.user:
            return Response({
                "status": 403,
                "message": "bukan pemilik event"
            }, status=status.HTTP_403_FORBIDDEN)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk, format=None):
        event = self.get_object(pk)
        user = request.user
        if user in event.participants.all():
            return Response({
                "status": 406,
                "message": "user already registered for event"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        event.participants.add(user)
        event.num_participants += 1
        event.save()
        serializer = EventSerializer(event, context= {'request': request})
        return Response({"message": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)