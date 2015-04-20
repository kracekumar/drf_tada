# -*- coding: utf-8 -*-

from todo import todo_bucket_service
from .task_entity import TaskEntity, TaskListEntity, NoteEntity
from . import task_repo

from commons.constants import _sentinel
from commons.arguments import filter_default_arguments


def create(task_entity):
    """Create a new Task object.
    """
    ignore_fields = ['modified', 'created', 'pk', 'notes', 'bucket']
    kwargs = task_entity.to_dict(ignore_fields=ignore_fields)
    kwargs['owner_id'] = kwargs.pop('created_by')

    obj = task_repo.create(**kwargs)

    return _create_entity(obj=obj)


def get(pk):
    obj = task_repo.get(pk=pk)
    return _create_entity(obj=obj)


def delete(pk):
    task_repo.delete(pk=pk)
    return True


def update(pk, title=_sentinel, is_archived=_sentinel, is_completed=_sentinel,
           due_date=_sentinel, reminder=_sentinel):
    fields = filter_default_arguments(**locals())
    obj = task_repo.update(**fields)

    if obj:
        return _create_entity(obj=obj)
    return None


def get_objects(user_id, limit, offset):
    objects = task_repo.get_objects(owner_id=user_id,
                                    limit=limit,
                                    offset=offset)
    total = task_repo.count(owner_id=user_id)
    meta = {'total': total, 'limit': limit, 'offset': offset}
    entities = [_create_entity(obj, skip_notes=True) for obj in objects]
    entity = TaskListEntity(meta=meta, objects=entities)
    return entity


def _create_entity(obj, skip_notes=False):
    bucket = todo_bucket_service.create_entity(obj=obj.bucket)
    if skip_notes:
        notes = []
    else:
        notes = [_create_note_entity(note) for note in obj.notes.all()]
    return TaskEntity(pk=obj.pk, title=obj.title,
                      created_by=obj.owner_id,
                      bucket_id=obj.bucket_id,
                      bucket=bucket,
                      is_archived=obj.is_archived,
                      is_completed=obj.is_completed,
                      due_date=obj.due_date,
                      reminder=obj.reminder,
                      notes=notes,
                      created=obj.created,
                      modified=obj.modified)


def _create_note_entity(note):
    return NoteEntity(pk=note.pk, description=note.description,
                      created_by=note.owner_id, created=note.created,
                      modified=note.modified, task_id=note.task_id)
