# -*- coding: utf-8 -*-

import copy

from .todo_bucket_entity import TodoBucketEntity
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


def get(pk):
    obj = todo_repo.get(pk=pk)
    return _create_entity(obj=obj)


def _create_entity(obj):
    return TodoBucketEntity(pk=obj.pk, title=obj.title,
                            description=obj.description,
                            created_by=obj.owner_id,
                            is_public=obj.is_public,
                            created=obj.created,
                            modified=obj.modified)
