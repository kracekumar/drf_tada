# -*- coding: utf-8 -*-

"""List of all Mixins which can be used with serializers.
"""

from rest_framework import serializers


class TimeStampedSerializerMixin(object):
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
