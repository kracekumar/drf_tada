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
