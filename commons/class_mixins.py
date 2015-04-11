# -*- coding: utf-8 -*-


class UpdateMixin:
    def update(self, key, value):
        if not key.startswith('_') and key in self.__dict__:
            setattr(self, key, value)

    def bulk_update(self, **kwargs):
        for key, value in kwargs.items():
            self.update(key, value)
