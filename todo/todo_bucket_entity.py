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
