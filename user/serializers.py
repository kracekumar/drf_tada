# -*- coding: utf-8 -*-

from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=30, required=True)
    first_name = serializers.CharField(allow_blank=True, max_length=30)
    last_name = serializers.CharField(allow_blank=True, max_length=30)
    password = serializers.CharField(write_only=True,
                                     max_length=128)
