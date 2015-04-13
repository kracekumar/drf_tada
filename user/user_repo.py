# -*- coding: utf-8 -*-

from functools import partial

from django.contrib.auth import get_user_model
from commons import base_repo


User = get_user_model()


def get(pk, model=User):
    return base_repo.get(model=User, pk=pk)


def set_password(pk, password):
    try:
        user = User.objects.get(pk=pk)
        user.set_password(password)
        return user
    except User.DoesNotExist:
        return None


update = partial(base_repo.update, model=User)
