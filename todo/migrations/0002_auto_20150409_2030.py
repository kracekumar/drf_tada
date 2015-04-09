# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoBucket',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, blank=True, verbose_name='created', editable=False)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, blank=True, verbose_name='modified', editable=False)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('description', models.TextField(blank=True, verbose_name='description', null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='owner',
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
