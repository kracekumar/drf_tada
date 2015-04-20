# -*- coding: utf-8 -*-

from rest_framework import serializers

from commons.serializers import (TimeStampedSerializerMixin, MetaDataSerializer,
                                 IdSerializerMixin, TitleSerializerMixin,
                                 IdTitleSerializerMixin)
from .fields import NoteResourceUriField
from commons.fields import UnixEpochDateField


class BaseNoteSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=255)


class NoteReadSerializer(IdSerializerMixin, BaseNoteSerializer,
                         TimeStampedSerializerMixin):
    resource_uri = NoteResourceUriField(view_name='note-detail',
                                        read_only=True)


class NoteWriteSerializer(BaseNoteSerializer):
    pass


class NoteUpdateSerializer(BaseNoteSerializer):
    pass


class TaskReadSerializer(IdTitleSerializerMixin, TimeStampedSerializerMixin):
    is_archived = serializers.BooleanField(default=False)
    is_completed = serializers.BooleanField(default=False)
    due_date = serializers.DateTimeField(format='%s')
    reminder = serializers.DateTimeField(format='%s')
    notes = NoteReadSerializer(many=True)
    created_by = serializers.IntegerField()


class TaskWriteSerializer(TitleSerializerMixin):
    is_archived = serializers.BooleanField(default=False)
    is_completed = serializers.BooleanField(default=False)
    due_date = serializers.DateTimeField(format='%s', required=False)
    reminder = serializers.DateTimeField(format='%s', required=False)


class TaskUpdateSerializer(TitleSerializerMixin):
    is_archived = serializers.BooleanField(default=False)
    is_completed = serializers.BooleanField(default=False)
    due_date = UnixEpochDateField(required=False, allow_null=True)
    reminder = UnixEpochDateField(required=False, allow_null=True)


class TaskReadListSerializer(IdTitleSerializerMixin,
                             TimeStampedSerializerMixin):
    is_archived = serializers.BooleanField(default=False)
    is_completed = serializers.BooleanField(default=False)
    due_date = serializers.DateTimeField(format='%s')
    reminder = serializers.DateTimeField(format='%s')
    created_by = serializers.IntegerField()


class TaskListSerializer(serializers.Serializer):
    meta = MetaDataSerializer()
    objects = TaskReadListSerializer(many=True)
