from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=6, write_only=True)
    is_completed = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'gender', 'address', 'is_completed', 'is_verified']

    def create(self, validated_data):
        if len(validated_data) >= 5:
            validated_data['is_completed'] = True
        else:
            validated_data['is_completed'] = False
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=255, read_only=True)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=68, write_only=True)
    name = serializers.CharField(max_length=255, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'tokens', 'name', 'gender', 'address', 'is_completed', 'is_verified']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        return {
            'email': user.email,
            'is_completed': user.is_completed,
            'tokens': user.tokens(),
            'name' : user.name,
            'id': user.id,
            'address': user.address,
            'gender': user.gender,
            'is_verified': user.is_verified
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'id', 'gender', 'is_verified']
