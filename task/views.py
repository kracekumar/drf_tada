# -*- coding: utf-8 -*-

# Third party import
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Non current app imports

from commons.decorators import handle_doesnt_exists_exception
from commons.permissions import LoggedInPermission
from commons.response import make_response
from commons.serializers import ListQueryParamsSerializer

from interactors import task_interactors, note_interactors
from todo.permissions import TodoBucketDetailPermission
# current app imports
from .task_entity import TaskEntity, NoteEntity
from .serializers import (NoteReadSerializer, NoteUpdateSerializer,
                          NoteWriteSerializer, TaskReadSerializer,
                          TaskUpdateSerializer, TaskWriteSerializer,
                          TaskListSerializer)


class TaskListApiView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TodoBucketDetailPermission]

    def post(self, request, todo_bucket_pk):
        data = request.DATA
        obj = TaskWriteSerializer(data=data)
        if obj.is_valid():
            dictionary = dict(obj.data)
            user_id = request.user.id
            dictionary['created_by'] = user_id
            dictionary['bucket_id'] = todo_bucket_pk
            task_entity = TaskEntity.from_dict(
                dictionary=dictionary)

            resp = task_interactors.create(task_entity=task_entity)
            return make_response(obj=resp,
                                 serializer_cls=TaskReadSerializer)

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)

    def get(self, request, todo_bucket_pk):
        param_serializer = ListQueryParamsSerializer(data=request.QUERY_PARAMS)
        user_id = request.user.id
        if param_serializer.is_valid():
            limit = param_serializer.data['limit']
            offset = param_serializer.data['offset']
            obj = task_interactors.get_objects(
                limit=limit, offset=offset, user_id=user_id)
            return make_response(obj=obj,
                                 serializer_cls=TaskListSerializer)

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=param_serializer.errors)


class TaskDetailApiView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TodoBucketDetailPermission]

    @handle_doesnt_exists_exception
    def get(self, request, todo_bucket_pk, task_pk):
        resp = task_interactors.get(pk=task_pk)
        return make_response(obj=resp,
                             serializer_cls=TaskReadSerializer)

    @handle_doesnt_exists_exception
    def delete(self, request, todo_bucket_pk, task_pk):
        resp = task_interactors.delete(pk=task_pk)
        return make_response(obj=resp)

    @handle_doesnt_exists_exception
    def patch(self, request, todo_bucket_pk, task_pk):
        resp = task_interactors.get(pk=task_pk)
        data = request.DATA
        task_entity = resp.instance
        task_entity.bulk_update(**data)
        #import ipdb;ipdb.set_trace()
        obj = TaskUpdateSerializer(data=task_entity.to_dict())
        if obj.is_valid():
            # Update the entities after validation
            task_entity.bulk_update(**obj.data)
            response = task_interactors.update(
                task_entity, update_fields=obj.data.keys())
            return make_response(obj=response,
                                 serializer_cls=TaskReadSerializer)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)


class NoteListApiView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TodoBucketDetailPermission]

    def post(self, request, todo_bucket_pk, task_pk):
        data = request.DATA
        obj = NoteWriteSerializer(data=data)
        if obj.is_valid():
            dictionary = dict(obj.data)
            user_id = request.user.id
            dictionary['created_by'] = user_id
            dictionary['task_id'] = task_pk
            note_entity = NoteEntity.from_dict(
                dictionary=dictionary)

            resp = note_interactors.create(note_entity=note_entity)
            return make_response(obj=resp,
                                 serializer_cls=NoteReadSerializer)

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)


class NoteDetailApiView(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TodoBucketDetailPermission]

    @handle_doesnt_exists_exception
    def get(self, request, todo_bucket_pk, task_pk, note_pk):
        resp = note_interactors.get(pk=note_pk)
        return make_response(obj=resp,
                             serializer_cls=NoteReadSerializer)

    @handle_doesnt_exists_exception
    def delete(self, request, todo_bucket_pk, task_pk, note_pk):
        resp = note_interactors.delete(pk=note_pk)
        return make_response(obj=resp)

    @handle_doesnt_exists_exception
    def patch(self, request, todo_bucket_pk, task_pk, note_pk):
        resp = note_interactors.get(pk=note_pk)
        data = request.DATA
        note_entity = resp.instance
        note_entity.bulk_update(**data)
        obj = NoteUpdateSerializer(data=note_entity.to_dict())
        if obj.is_valid():
            # Update the entities after validation
            note_entity.bulk_update(**obj.data)
            response = note_interactors.update(
                note_entity, update_fields=obj.data.keys())
            return make_response(obj=response,
                                 serializer_cls=NoteReadSerializer)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)
