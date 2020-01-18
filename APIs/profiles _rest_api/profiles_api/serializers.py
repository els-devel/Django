from abc import ABC

from rest_framework import serializers
from profiles_api import models

import subprocess


class GetSecretsSerializer(serializers.ModelSerializer):
    """Serializers a name field for testing out APIView"""

    class Meta:
        model = models.Secrets
        fields = ('id', 'key', 'value', 'created_on')

    # def create(self, validated_data):
    #     entry = models.DatabaseItem.make_entry(
    #         key=validated_data['key'],
    #         value=validated_data['value']
    #     )
    #
    #     return entry
    #
    # def get_attribute(self, validated_data):
    #     value = models.DatabaseItem.get_value(
    #         key=validated_data['key'],
    #     )
    #
    #     return value


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

class SecretsSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.Secrets
        fields = ('id', 'key', 'value', 'created_on')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create and return new user"""

        secret = models.Secrets
        id = secret.id
        created_on = secret.created_on
        key = secret.key
        value = secret.value

        # secret = models.Secrets.objects.create_user(
        #     key=validated_data['key'],
        #     value=validated_data['value']
        # )

        return user