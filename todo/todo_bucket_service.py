# -*- coding: utf-8 -*-

import copy

from . import todo_repo


def create(todo_bucket_entity):
    """Create a new Todo Bucket object.
    """
    kwargs = todo_bucket_entity.to_dict()
    kwargs.pop('modified', None)
    kwargs.pop('created', None)
    kwargs.pop('pk', None)
    kwargs['owner_id'] = kwargs.pop('created_by')
    obj = todo_repo.create(**kwargs)
    entity = copy.deepcopy(todo_bucket_entity)
    entity.pk = obj.pk
    entity.modified = obj.modified
    entity.created = obj.created
    return entity
