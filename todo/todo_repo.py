# -*- coding: utf-8 -*-

from functools import partial
from commons import base_repo

from .models import TodoBucket


def create(title, description, owner_id, is_public):
    kwargs = locals()
    return base_repo.create(model=TodoBucket, **kwargs)


get = partial(base_repo.get, model=TodoBucket)
count = partial(base_repo.count, model=TodoBucket)
get_objects = partial(base_repo.filter, model=TodoBucket)
update = partial(base_repo.update, model=TodoBucket)
delete = partial(base_repo.delete, model=TodoBucket)
