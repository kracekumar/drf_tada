# -*- coding: utf-8 -*-

from rest_framework import serializers


class UserReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    email = serializers.EmailField()
    username = serializers.CharField(max_length=30, required=True)
    first_name = serializers.CharField(allow_blank=True, max_length=30)
    last_name = serializers.CharField(allow_blank=True, max_length=30)


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    first_name = serializers.CharField(allow_blank=True, max_length=30)
    last_name = serializers.CharField(allow_blank=True, max_length=30)


class UserPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)
