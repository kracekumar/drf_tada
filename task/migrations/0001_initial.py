# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20150409_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, blank=True, default=django.utils.timezone.now)),
                ('description', models.TextField(default='')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(verbose_name='created', editable=False, blank=True, default=django.utils.timezone.now)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(verbose_name='modified', editable=False, blank=True, default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=255)),
                ('due_date', models.DateTimeField(null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('remind', models.DateTimeField(null=True)),
                ('bucket', models.OneToOneField(to='todo.TodoBucket')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='note',
            name='task',
            field=models.ForeignKey(to='task.Task'),
            preserve_default=True,
        ),
    ]
