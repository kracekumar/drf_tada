# -*- coding: utf-8 -*-

from functools import partial
from commons import base_repo

from .models import Task


def create(title, bucket_id, is_archived, is_completed, owner_id, due_date,
           reminder):
    kwargs = locals()
    return base_repo.create(model=Task, **kwargs)


get = partial(base_repo.get, model=Task)
count = partial(base_repo.count, model=Task)
get_objects = partial(base_repo.filter, model=Task)
update = partial(base_repo.update, model=Task)
delete = partial(base_repo.delete, model=Task)
