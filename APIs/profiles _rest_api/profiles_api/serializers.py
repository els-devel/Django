from rest_framework import serializers
from profiles_api import models

import subprocess


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class GetSecretsSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    key = serializers.CharField(max_length=10)
   # value = subprocess.run(f"su -u USER -c psql SELECT {key} FOR ...")

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return new user"""

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
