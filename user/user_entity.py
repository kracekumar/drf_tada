# -*- coding: utf-8 -*-

from commons.decorators import set_init_args
from commons.dict_mixin import DictMixin
from commons.class_mixins import UpdateMixin


class UserEntity(DictMixin, UpdateMixin):
    @set_init_args
    def __init__(self, username, email, first_name='', last_name='',
                 password='*', pk=None):
        """User Entity
        """
