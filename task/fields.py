# -*- coding: utf-8 -*-

from commons.fields import ResourceUriField


class NoteResourceUriField(ResourceUriField):
    def to_representation(self, value):
        request = self.get_request()
        if request.method == "POST":
            return '{}{}/'.format(request.path, value.pk)
        else:
            if 'notes' in request.path:
                return request.path
            return '{}notes/{}/'.format(request.path, value.pk)
