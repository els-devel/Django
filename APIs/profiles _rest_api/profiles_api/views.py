import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from profiles_api import models
from profiles_api import permissions
from profiles_api import serializers


class Heartbeat(APIView):
    """Test API View"""

    def get(self, request, format=None):
        return Response("API is ALIVE.")


# class Eric(APIView):
#     """Full API View"""
#     serializer_class = serializers.HelloSerializer
#
#     def get(self, request, format=None):
#         return Response("API is ALIVE.")
#
#     def post(self, request):
#         """Create a Hello Message with our name"""
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f'Hello {name}'
#             return Response({'message': message})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#             # gives you a dictionaries of the errors based on the validation rules applied to the serializer
#
#     def put(self, request, pk=None):
#         """Handling updating an object"""
#         return Response({'method': 'PUT'})
#
#     def patch(self, request, pk=None):
#         """Handle a partial update of an object"""
#         return Response({'message': 'PATCH'})
#
#     def delete(self, request, pk=None):
#         """Delete an object"""
#         return Response({'method': 'DELETE'})
#
#
class SecretsEngine2(generics.ListAPIView):
    queryset = models.Secrets.objects.all()
    serializer_class = serializers.GetSecretsSerializer


class SecretsEngine(APIView):
    """Full API View"""
    serializer_class = serializers.GetSecretsSerializer

    def get(self, request, format=None):
        return Response("API is ALIVE.")

    def post(self, request):
        """Create a Hello Message with our name"""
        serializer = self.serializer_class(data=request.data)
        pk = self.serializer_class

        if serializer.is_valid():
            key = serializer.validated_data.get('key')
            value = serializer.validated_data.get('value')
            message = f'Hello {key}, {value}, {pk}'
            return Response({'message': message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
            # gives you a dictionaries of the errors based on the validation rules applied to the serializer

    # def put(self, request, pk=None):
    #     """Handling updating an object"""
    #     return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})

    ######### VIEWSETS #################################################################


class SecretsViewSet(viewsets.ModelViewSet):
    """API secrets viewset"""
    serializer_class = serializers.GetSecretsSerializer
    queryset = models.Secrets.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
    )

    # def list(self, request):
    #     """Return default message"""
    #     return Response('Uses actions (list, create, retrieve, update, partial_update)')
    #
    # def create(self, request):
    #     """Create a new secret"""
    #     serializer = self.serializer_class(data=request.data)
    #
    #     if serializer.is_valid():
    #         pk = models.DatabaseItem.id
    #         key = serializer.validated_data.get('key')
    #         value = serializer.validated_data.get('value')
    #         created_on = models.DatabaseItem.created_on
    #         message1 = f'Creating a key:value pair, {key}:{value}...'
    #         message2 = f"made database entry ({pk}, {key}, {value}, {created_on})"
    #         return Response({'response1': serializer.validated_data,
    #                          'response2': message2})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
    #
    # def retrieve(self, request, pk=None):
    #     """for retrieving specific object in our viewset based on pk"""
    #     return Response({'http_method': 'GET'})
    #
    # def update(self, request, pk=None):
    #     """Handle updating part of an object"""
    #     return Response({'http_method': 'PUT'})
    #
    # def partial_update(self, request, pk=None):
    #     """update part of an object"""
    #     return Response({'http_method': 'PATCH'})
    #
    # def destroy(self, request, pk=None):
    #     """remove an object"""
    #     return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)  # can add as many authentication classes you want for
    # multiple types of authentication
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# class UserProfileFeedViewSet(viewsets.ModelViewSet):
#     """Handles creating, reading, and updating profile feed items"""
#     authentication_classes = (TokenAuthentication,)
#     serializer_class = serializers.ProfileFeedItemSerializer
#     queryset = models.ProfileFeedItem.objects.all()
#     permission_classes = (
#         permissions.UpdateOwnStatus,
#         IsAuthenticated
#     )
#
#     def perform_create(self, serializer):
#         """Sets the user profile to the logged in user"""
#         serializer.save(user_profile=self.request.user)
