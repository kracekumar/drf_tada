# -*- coding: utf-8 -*-


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


def update(pk, **kwargs):
    user = get(pk=pk)
    return base_repo.update(model_object=user, pk=pk, **kwargs)
