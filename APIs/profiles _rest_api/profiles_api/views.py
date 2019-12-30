import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import models
from profiles_api import permissions
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

    ######### VIEWSETS #################################################################


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return as hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """for retrieving specific object in our viewset based on pk"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """update part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """remove an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # can add as many authentication classes you want for
    # multiple types of authentication
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)