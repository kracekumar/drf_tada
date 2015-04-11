# -*- coding: utf-8 -*-


def can_access(todo_bucket_entity, user_id=None):
    if todo_bucket_entity.is_public is True:
        return True

    return todo_bucket_entity.created_by == user_id
