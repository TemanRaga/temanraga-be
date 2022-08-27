from django.shortcuts import render
from rest_framework.views import APIView
from authentication.serializers import UserSerializer
from authentication.utils import AllowAnyOnGet
from rest_framework.response import Response
from rest_framework import status
from profiles.serializers import UserSerializerUpdate


# Create your views here.
class ProfileDetail(APIView):
    permission_classes = (AllowAnyOnGet,)

    def put(self, request, format=None):
        user = request.user
        data = request.data
        serializer = UserSerializerUpdate(user, data, context= {'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": UserSerializer(user).data})
        return Response({"message": "errors", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)