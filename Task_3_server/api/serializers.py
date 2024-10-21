from rest_framework import serializers

class InverseSerializer(serializers.Serializer):
    key1 = serializers.CharField(max_length=100)