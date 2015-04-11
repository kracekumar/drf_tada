# -*- coding: utf-8 -*-

"""List of all Mixins which can be used with serializers.
"""

from rest_framework import serializers


class TimeStampedSerializerMixin(serializers.Serializer):
    created = serializers.DateTimeField(format='%s')
    modified = serializers.DateTimeField(format='%s')


class LimitOffsetSerializer(serializers.Serializer):
    limit = serializers.IntegerField(min_value=1, max_value=100, default=20)
    offset = serializers.IntegerField(min_value=0, default=0)


class ListQueryParamsSerializer(LimitOffsetSerializer):
    """Use this serializer for validating query params on List Get method.
    """


class MetaDataSerializer(LimitOffsetSerializer):
    total = serializers.IntegerField()
