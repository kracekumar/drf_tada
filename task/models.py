# -*- coding: utf-8 -*-

from django.conf import settings

from django.db import models
from django_extensions.db.models import TimeStampedModel

from todo.models import TodoBucket

User = settings.AUTH_USER_MODEL


class Task(TimeStampedModel):
    bucket = models.ForeignKey(to=TodoBucket)
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(null=True)
    is_archived = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    reminder = models.DateTimeField(null=True)
    owner = models.ForeignKey(to=User)


class Note(TimeStampedModel):
    description = models.TextField(default='')
    # There can be more than one note for task
    task = models.ForeignKey(to=Task, related_name='notes')
    owner = models.ForeignKey(to=User)
