# -*- coding: utf-8 -*-

from commons import base_repo

from .models import TodoBucket


def create(title, description, owner_id, is_public):
    kwargs = locals()
    return base_repo.create(model=TodoBucket, **kwargs)
