# -*- coding: utf-8 -*-


def can_access(todo_bucket_entity, user_id=None):
    if todo_bucket_entity.is_public is True:
        return True

    return _is_owner(todo_bucket_entity=todo_bucket_entity, user_id=user_id)


def can_delete(todo_bucket_entity, user_id=None):
    return _is_owner(todo_bucket_entity=todo_bucket_entity, user_id=user_id)


def _is_owner(todo_bucket_entity, user_id):
    return todo_bucket_entity.created_by == user_id
