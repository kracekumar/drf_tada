# -*- coding: utf-8 -*-

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
