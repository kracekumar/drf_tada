# -*- coding: utf-8 -*-


class DictMixin(object):
    """DictMixin is for converting object to dict and creating object from dict.
    """
    def to_dict(self, ignore_fields=None, ignore_underscore_fields=True):
        """Convert object attributes to dict. Any field_name starting with `_`
        can be ignored.
        """
        data = self.__dict__.copy()
        ignore_fields = ignore_fields or []

        for field in ignore_fields:
            data.pop(field, None)

        if ignore_underscore_fields:
            return {key: value for key, value in data.items()
                    if not key.startswith('_')}
        return data

    @classmethod
    def from_dict(cls, dictionary):
        """Create an object from dictionary.

        :param cls: `class` which uses this mixin.
        :param dictionary: `dict` containing attribute and values.
        :returns: instance of `cls`.
        :rtype: `object`.

        """
        assert isinstance(dictionary, dict)
        return cls(**dictionary)
