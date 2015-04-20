# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20150418_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='task',
            field=models.ForeignKey(to='task.Task', related_name='notes'),
        ),
        migrations.AlterField(
            model_name='task',
            name='bucket',
            field=models.ForeignKey(to='todo.TodoBucket'),
        ),
    ]
