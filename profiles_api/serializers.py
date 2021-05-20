from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """ Serilies fields for HelloApi """
    name = serializers.CharField(max_length=10)
