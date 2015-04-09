# -*- coding: utf-8 -*-

from .decorators import set_init_args

# TODO: Better name, pls!


class BusinessResponse(object):
    @set_init_args
    def __init__(self, is_success, instance=None, errors=None):
        """Instance of this class should be written by interactors.
        `view` can check if `is_success` is `True`. If the action is
        successful, `instance` will contain entity else `errors`
        will be `dict`.
        """
