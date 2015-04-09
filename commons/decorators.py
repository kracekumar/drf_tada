# -*- coding: utf-8 -*-

import wrapt
import inspect

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


@wrapt.decorator
def set_init_args(wrapped, instance, args, kwargs):
    """Assign all passed arguments to `__init__`.

    Example:
    >>>class Foo(object):
           @set_init_args
           def __init__(self, bar, baz):
               pass

    >>>f = Foo(bar='bar', baz='baz')
    >>>f.bar
    bar
    >>>f.baz
    baz
    """
    args, varargs, keywords, defaults = inspect.getargspec(wrapped)
    # If no defaults, len function won't work so assign empty list
    defaults = defaults or []
    # Get all default values specified in `__init__`
    default_values = dict(zip(args[-len(defaults):], defaults))
    values = {}
    values.update(default_values)
    # Now update the passed arguments
    values.update(kwargs)
    # Find missing and extra args
    _check_attrs(values.keys(), args[1:])
    instance.__dict__.update(values)
    wrapped(**values)


# Private
def _check_attrs(passed_on_attrs, defined_attrs):
    passed_on_attrs_set = set(passed_on_attrs)
    defined_attrs_set = set(defined_attrs)
    # Find missing and extra args
    missing_attrs = defined_attrs_set - passed_on_attrs_set
    extra_attrs = passed_on_attrs_set - defined_attrs_set

    if missing_attrs or extra_attrs:
        msg = u"__init__() got an unexpected keyword argument {}".format(
            list(missing_attrs or extra_attrs))
        raise TypeError(msg)


@wrapt.decorator
def handle_doesnt_exists_exception(wrapped, instance, args, kwargs):
    try:
        return wrapped(*args, **kwargs)
    except ObjectDoesNotExist:
        return Response(status=404)
