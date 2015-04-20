# -*- coding: utf-8 -*-

from functools import partial
from commons import base_repo

from .models import Note


def create(description, owner_id, task_id):
    kwargs = locals()
    return base_repo.create(model=Note, **kwargs)


get = partial(base_repo.get, model=Note)
count = partial(base_repo.count, model=Note)
get_objects = partial(base_repo.filter, model=Note)
update = partial(base_repo.update, model=Note)
delete = partial(base_repo.delete, model=Note)
