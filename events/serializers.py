from django.db.models import fields
from rest_framework import serializers
from events.models import Event
from authentication.serializers import UserSerializer

class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
