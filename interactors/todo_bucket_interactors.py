# -*- coding: utf-8 -*-

"""Functions for handling `TodoBucket` related tasks.
"""

from commons.response import BusinessResponse, BusinessAction
from todo import todo_bucket_service
from todo import permissions


def create(todo_bucket_entity):
    entity = todo_bucket_service.create(todo_bucket_entity=todo_bucket_entity)
    instance = BusinessResponse(is_success=True, instance=entity,
                                action=BusinessAction.RESOURCE_CREATED)
    return instance


def get(pk, user_id=None):
    entity = todo_bucket_service.get(pk=pk)
    if permissions.can_access(todo_bucket_entity=entity, user_id=user_id):
        instance = BusinessResponse(is_success=True, instance=entity,
                                    action=BusinessAction.RESOURCE_READ)
    else:
        instance = BusinessResponse(
            is_success=False, action=BusinessAction.RESOURCE_ACCESS_DENIED)
    return instance


def delete(pk, user_id=None):
    entity = todo_bucket_service.get(pk=pk)
    if permissions.can_delete(todo_bucket_entity=entity, user_id=user_id):
        todo_bucket_service.delete(pk=pk)
        return BusinessResponse(is_success=True,
                                action=BusinessAction.RESOURCE_DELETED)
    return BusinessResponse(is_success=False,
                            action=BusinessAction.RESOURCE_ACCESS_DENIED)


def get_objects(user_id, limit=20, offset=0):
    entity = todo_bucket_service.get_objects(user_id=user_id,
                                             limit=limit, offset=offset)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_READ,
                            instance=entity)


def update(todo_bucket_entity, update_fields=None):
    to_update = {field: getattr(todo_bucket_entity, field)
                 for field in update_fields}
    entity = todo_bucket_service.update(pk=todo_bucket_entity.pk,
                                        **to_update)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_UPDATED,
                            instance=entity)
