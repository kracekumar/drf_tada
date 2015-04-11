# -*- coding: utf-8 -*-

from rest_framework import serializers

from commons.serializers import TimeStampedSerializerMixin
from commons.fields import ResourceUriField


class BaseTodoBucketSerializerMixin(object):
    """Mixin with common fields for TodoBucket"""
    title = serializers.CharField(max_length=30, required=True)
    description = serializers.CharField(default='')
    is_public = serializers.BooleanField(default=False)


class TodoBucketReadSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='pk')
    title = serializers.CharField(max_length=30, required=True)
    description = serializers.CharField(default='')
    is_public = serializers.BooleanField(default=False)
    created_by = serializers.IntegerField()
    created = serializers.DateTimeField(format="%s")
    modified = serializers.DateTimeField(format="%s")


class TodoBucketWriteSerializer(serializers.Serializer):
    """TodoBucket serializer used during create"""
    title = serializers.CharField(max_length=30, required=True)
    description = serializers.CharField(default='')
    is_public = serializers.BooleanField(default=False)


class TodoBucketUpdateSerializer(serializers.Serializer):
    pass
