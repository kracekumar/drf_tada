# -*- coding: utf-8 -*-

from django.conf import settings

from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

# Create your models here.


class TodoBucket(TitleDescriptionModel, TimeStampedModel):
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    is_public = models.BooleanField(default=False)
