# -*- coding: utf-8 -*-

"""Functions for handling `TodoBucket` related tasks.
"""

from commons.response import BusinessResponse

from todo import todo_bucket_service


def create(todo_bucket_entity):
    entity = todo_bucket_service.create(todo_bucket_entity=todo_bucket_entity)
    return BusinessResponse(is_success=True, instance=entity)
