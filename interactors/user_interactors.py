# -*- coding: utf-8 -*-

from user import user_service
from user.user_entity import UserEntity


def get(pk):
    user = user_service.get(pk=pk)
    if user:
        return _create_user_entity(user)
    return None


def set_password(user_id, password):
    user = user_service.set_password(pk=user_id, password=password)
    if user:
        return _create_user_entity(user)
    return None


def update(user_entity, update_fields):
    to_update = {field: getattr(user_entity, field) for field in update_fields}
    user = user_service.update(pk=user_entity.pk, **to_update)
    if user:
        return _create_user_entity(user)
    return None


def _create_user_entity(user):
    return UserEntity(pk=user.pk, username=user.username,
                      first_name=user.first_name,
                      last_name=user.last_name,
                      email=user.email)
