# -*- coding: utf-8 -*-

from rest_framework import serializers

from commons.serializers import TimeStampedSerializerMixin, MetaDataSerializer


class BaseTodoBucketSerializerMixin(serializers.Serializer):
    """Mixin with common fields for TodoBucket"""
    title = serializers.CharField(max_length=30, required=True)
    description = serializers.CharField(default='')
    is_public = serializers.BooleanField(default=False)


class TodoBucketReadSerializer(BaseTodoBucketSerializerMixin,
                               TimeStampedSerializerMixin):
    id = serializers.IntegerField(source='pk')
    created_by = serializers.IntegerField()


class TodoBucketWriteSerializer(BaseTodoBucketSerializerMixin):
    """TodoBucket serializer used during create"""


class TodoBucketUpdateSerializer(BaseTodoBucketSerializerMixin):
    pass


class TodoBucketListSerializer(serializers.Serializer):
    meta = MetaDataSerializer()
    objects = TodoBucketReadSerializer(many=True)
