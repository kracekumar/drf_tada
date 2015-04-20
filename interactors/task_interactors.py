# -*- coding: utf-8 -*-

from commons.response import BusinessResponse, BusinessAction
from task import task_service


def create(task_entity):
    entity = task_service.create(task_entity=task_entity)
    return BusinessResponse(is_success=True, instance=entity,
                            action=BusinessAction.RESOURCE_CREATED)


def get(pk):
    entity = task_service.get(pk=pk)
    return BusinessResponse(is_success=True, instance=entity,
                            action=BusinessAction.RESOURCE_READ)


def delete(pk):
    task_service.delete(pk=pk)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_DELETED)


def update(task_entity, update_fields=None):
    to_update = {field: getattr(task_entity, field)
                 for field in update_fields}
    entity = task_service.update(pk=task_entity.pk,
                                 **to_update)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_UPDATED,
                            instance=entity)


def get_objects(user_id, limit=20, offset=0):
    entity = task_service.get_objects(user_id=user_id,
                                      limit=limit, offset=offset)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_READ,
                            instance=entity)
