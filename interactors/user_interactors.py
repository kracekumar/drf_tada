# -*- coding: utf-8 -*-

from user import user_service
from user.user_entity import UserEntity


def get(pk):
    user = user_service.get(pk=pk)
    if user:
        return UserEntity(id=user.pk, username=user.username,
                          first_name=user.first_name,
                          last_name=user.last_name)
    return None
