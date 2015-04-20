# -*- coding: utf-8 -*-

from .task_entity import NoteEntity
from . import note_repo


def create(note_entity):
    """Create a new Task object.
    """
    ignore_fields = ['modified', 'created', 'pk']
    kwargs = note_entity.to_dict(ignore_fields=ignore_fields)
    kwargs['owner_id'] = kwargs.pop('created_by')

    note = note_repo.create(**kwargs)

    return _create_entity(note=note)


def get(pk):
    note = note_repo.get(pk=pk)
    return _create_entity(note=note)


def delete(pk):
    note_repo.delete(pk=pk)
    return True


def update(pk, description):
    note = note_repo.update(pk=pk, description=description)

    if note:
        return _create_entity(note=note)
    return None


def _create_entity(note):
    return NoteEntity(pk=note.pk, description=note.description,
                      created_by=note.owner_id, created=note.created,
                      modified=note.modified, task_id=note.task_id)
