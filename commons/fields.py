# -*- coding: utf-8 -*-

import inspect
import datetime

from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField


# It is taken from `drf-extensions`
# https://github.com/chibisov/drf-extensions/blob/master/rest_framework_extensions/fields.py
class ResourceUriField(HyperlinkedRelatedField):
    """
    Represents a hyperlinking uri that points to the detail view for that object.
    Example:
        class SurveySerializer(serializers.ModelSerializer):
            resource_uri = ResourceUriField(view_name='survey-detail')
            class Meta:
                model = Survey
                fields = ('id', 'resource_uri')
        ...
        {
            "id": 1,
            "resource_uri": "http://localhost/v1/surveys/1/",
        }
    """
    # todo: test me

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('source', '*')
        super(ResourceUriField, self).__init__(*args, **kwargs)

    def get_request(self):
        """Walk up the stack, return the nearest first argument named "request"."""
        #http://nedbatchelder.com/blog/201008/global_django_requests.html
        frame = None
        try:
            for f in inspect.stack()[1:]:
                frame = f[0]
                code = frame.f_code
                if code.co_varnames[:1] == ("request",):
                    return frame.f_locals["request"]
                elif code.co_varnames[:2] == ("self", "request",):
                    return frame.f_locals["request"]
        finally:
            del frame


class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        return value

    def to_internal_value(self, value):
        return datetime.datetime.fromtimestamp(int(value))
