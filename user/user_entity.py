# -*- coding: utf-8 -*-

from commons.decorators import set_init_args
from commons.dict_mixin import DictMixin


class UserEntity(DictMixin):
    @set_init_args
    def __init__(self, username, first_name, last_name, password='*',
                 id=None):
        """User Entity
        """
