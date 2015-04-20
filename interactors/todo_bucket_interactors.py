# -*- coding: utf-8 -*-

"""Functions for handling `TodoBucket` related tasks.
"""

from commons.response import BusinessResponse, BusinessAction
from todo import todo_bucket_service


def create(todo_bucket_entity):
    entity = todo_bucket_service.create(todo_bucket_entity=todo_bucket_entity)
    instance = BusinessResponse(is_success=True, instance=entity,
                                action=BusinessAction.RESOURCE_CREATED)
    return instance


def get(pk):
    entity = todo_bucket_service.get(pk=pk)
    return BusinessResponse(is_success=True, instance=entity,
                            action=BusinessAction.RESOURCE_READ)


def delete(pk):
    todo_bucket_service.delete(pk=pk)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_DELETED)


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
