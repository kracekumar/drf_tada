# -*- coding: utf-8 -*-

from commons.decorators import set_init_args
from commons.dict_mixin import DictMixin
from commons.class_mixins import UpdateMixin


class TodoBucketEntity(DictMixin, UpdateMixin):
    @set_init_args
    def __init__(self, title, description, created_by,
                 pk=None, is_public=False, created=None,
                 modified=None):
        """TodoBucket Entity
        """


class TodoBucketListEntity:
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
        data['object'] = [obj.to_dict() for obj in self.objects]

        return data
