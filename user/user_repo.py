# -*- coding: utf-8 -*-


from django.contrib.auth import get_user_model
from commons import base_repo


User = get_user_model()


def get(pk, model=User):
    return base_repo.get(model=User, pk=pk)
