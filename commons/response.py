# -*- coding: utf-8 -*-

from enum import Enum

from .decorators import set_init_args
from rest_framework import status, serializers
from rest_framework.response import Response


__all__ = ['BusinessAction', 'BusinessResponse', 'make_response']


# TODO: Better name, pls!


class BusinessResponse(object):
    @set_init_args
    def __init__(self, is_success, instance=None, errors=None, action=None):
        """Instance of this class should be written by interactors.
        `view` can check if `is_success` is `True`. If the action is
        successful, `instance` will contain entity else `errors`
        will be `dict`.
        """


def make_response(obj, serializer_cls=None):
    """This is a helper function to return Response serialize the object/dict to
    proper json with HTTP Codes.

    :param serializer_cls: REST framework serializer class.
    :param obj: Instance of `BusinessResponse`
    :returns: REST Framework Response
    :rtype:

    """
    is_repsonse_obj = isinstance(obj, BusinessResponse)
    is_serializer_obj = isinstance(obj, serializers.Serializer)
    assert is_repsonse_obj or is_serializer_obj

    if is_repsonse_obj:
        return _make_response_from_business_response(
            obj=obj, serializer_cls=serializer_cls)
    return _make_response_from_serializer(obj=obj,
                                          serializer_cls=serializer_cls)


class BusinessAction(Enum):
    RESOURCE_CREATED = 'resource_created'
    RESOURCE_UPDATED = 'resource_updated'
    RESOURCE_DELETED = 'resource_deleted'
    RESOURCE_READ = 'resource_read'
    RESOURCE_ACCESS_DENIED = 'resource_access_denied'


resource_status_mapping = {
    BusinessAction.RESOURCE_CREATED: status.HTTP_201_CREATED,
    BusinessAction.RESOURCE_DELETED: status.HTTP_204_NO_CONTENT,
    BusinessAction.RESOURCE_UPDATED: status.HTTP_202_ACCEPTED,
    BusinessAction.RESOURCE_READ: status.HTTP_200_OK,
    BusinessAction.RESOURCE_ACCESS_DENIED: status.HTTP_403_FORBIDDEN}


# helper/internal functions
def _make_response_from_business_response(obj, serializer_cls):
    assert serializer_cls

    if obj.is_success:
        instance = serializer_cls(instance=obj.instance)
        _status = resource_status_mapping.get(obj.action,
                                              status.HTTP_200_OK)
        return Response(status=_status, data=instance.data)
    else:
        if obj.action == BusinessAction.RESOURCE_ACCESS_DENIED:
            return Response(status=resource_status_mapping.get(obj.action))
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)


def _make_response_from_serializer(obj):
    if obj.errors:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)
    return Response(status=status.HTTP_200_OK, data=obj.data)
