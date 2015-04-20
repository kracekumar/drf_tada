# -*- coding: utf-8 -*-


from commons.response import BusinessResponse, BusinessAction
from task import note_service
from task import permissions


def create(note_entity):
    entity = note_service.create(note_entity=note_entity)
    return BusinessResponse(is_success=True, instance=entity,
                            action=BusinessAction.RESOURCE_CREATED)


def get(pk):
    entity = note_service.get(pk=pk)
    return BusinessResponse(is_success=True, instance=entity,
                            action=BusinessAction.RESOURCE_READ)


def delete(pk):
    note_service.delete(pk=pk)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_DELETED)


def update(note_entity, update_fields=None):
    to_update = {field: getattr(note_entity, field)
                 for field in update_fields}
    entity = note_service.update(pk=note_entity.pk,
                                 **to_update)
    return BusinessResponse(is_success=True,
                            action=BusinessAction.RESOURCE_UPDATED,
                            instance=entity)
