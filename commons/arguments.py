# -*- coding: utf-8 -*-

from .constants import _sentinel


def filter_default_arguments(default=_sentinel, **kwargs):
    return {field: val for field, val in kwargs.items() if val != default}
