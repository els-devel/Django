from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import subprocess

from profiles_api import serializers

class Heartbeat(APIView):
    """Test API View"""

    def get(self, request, format=None):

        return Response("API is ALIVE.")

class Eric(APIView):
    """Full API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        return Response("API is ALIVE.")

    def post(self, request):
        """Create a Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            # gives you a dictionaries of the errors based on the validation rules applied to the serializer

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class SecretsEngine(APIView):
    """Full API View"""
    serializer_class = serializers.GetSecretsSerializer

    def get(self, request, format=None):
        return Response("API is ALIVE.")

    def post(self, request):
        """Create a Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            key = serializer.validated_data.get('key')
            message = f'Hello {key}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            # gives you a dictionaries of the errors based on the validation rules applied to the serializer

    def put(self, request, pk=None):
        """Handling updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})