from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from event.serializers import EventSerializers
from event.models import Event


class EventListView(APIView):
    serializer_class = EventSerializers
    def get(self, request, format=None):
        events = Event.objects.all()
        return Response(events, status=status.HTTP_200_OK)



class EventCreateView(APIView):
    def post(self, request, format):
        return Response(request)


class EventDetailView(APIView):
    def get(self, request, format=None):
        return Response(request)

    # def post(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)