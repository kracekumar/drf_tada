# -*- coding: utf-8 -*-

from commons.fields import ResourceUriField


class NoteResourceUriField(ResourceUriField):
    def to_representation(self, value):
        request = self.get_request()
        if request.method == "POST":
            return '{}{}/'.format(request.path, value.pk)
        else:
            return request.path
