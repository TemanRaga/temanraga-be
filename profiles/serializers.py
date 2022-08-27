from django.db.models import fields
from rest_framework import serializers
from authentication.models import User
from authentication.serializers import UserSerializer

class UserSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'address']