# -*- coding: utf-8 -*-

from .todo_bucket_entity import TodoBucketEntity, TodoBucketListEntity
from . import todo_repo

from commons.constants import _sentinel
from commons.arguments import filter_default_arguments


def create(todo_bucket_entity):
    """Create a new Todo Bucket object.
    """
    ignore_fields = ['modified', 'created', 'pk']
    kwargs = todo_bucket_entity.to_dict(ignore_fields=ignore_fields)
    kwargs['owner_id'] = kwargs.pop('created_by')

    obj = todo_repo.create(**kwargs)

    return _create_entity(obj=obj)


def get(pk):
    obj = todo_repo.get(pk=pk)
    return _create_entity(obj=obj)


def get_objects(user_id, limit, offset):
    objects = todo_repo.get_objects(owner_id=user_id,
                                    limit=limit,
                                    offset=offset)
    total = todo_repo.count(owner_id=user_id)
    meta = {'total': total, 'limit': limit, 'offset': offset}
    entities = [_create_entity(obj) for obj in objects]
    entity = TodoBucketListEntity(meta=meta, objects=entities)
    return entity


def update(pk, title=_sentinel, description=_sentinel, is_public=_sentinel):
    fields = filter_default_arguments(**locals())
    obj = todo_repo.update(**fields)

    if obj:
        return _create_entity(obj=obj)
    return None


def _create_entity(obj):
    return TodoBucketEntity(pk=obj.pk, title=obj.title,
                            description=obj.description,
                            created_by=obj.owner_id,
                            is_public=obj.is_public,
                            created=obj.created,
                            modified=obj.modified)
