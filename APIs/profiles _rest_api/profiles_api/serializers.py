from rest_framework import serializers
import subprocess


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)


class GetSecretsSerializer(serializers.Serializer):
    """Serializers a name field for testing out APIView"""
    key = serializers.CharField(max_length=10)
   # value = subprocess.run(f"su -u USER -c psql SELECT {key} FOR ...")
