# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20150418_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='remind',
            new_name='reminder',
        ),
    ]
