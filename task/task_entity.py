# -*- coding: utf-8 -*-

from commons.decorators import set_init_args
from commons.dict_mixin import DictMixin
from commons.class_mixins import UpdateMixin


class TaskEntity(DictMixin, UpdateMixin):
    @set_init_args
    def __init__(self, title, created_by, is_archived,
                 is_completed, bucket_id, pk=None,
                 due_date=None, bucket=None,
                 reminder=None, notes=None,
                 created=None, modified=None):
        self.notes = self.notes or []

    def to_dict(self, ignore_fields=None, **kwargs):
        ignore_fields = ignore_fields or []
        kwargs['ignore_fields'] = ignore_fields
        data = super().to_dict(**kwargs)
        if 'notes' in ignore_fields:
            data.pop('notes', None)
        else:
            notes = [note.to_dict() for note in self.notes]
            data['notes'] = notes
        return data


class NoteEntity(DictMixin, UpdateMixin):
    @set_init_args
    def __init__(self, description, created_by, task_id, pk=None,
                 created=None, modified=None):
        pass


class TaskListEntity:
    @set_init_args
    def __init__(self, meta, objects):
        """
        param objects: `List` of `TodoBucketEntity`
        param meta: `dict` containing metadata about the `TodoBucket`
        """

    def to_dict(self):
        assert isinstance(self.meta, dict)

        data = {}

        data['meta'] = self.meta
        data['objects'] = [obj.to_dict() for obj in self.objects]

        return data
