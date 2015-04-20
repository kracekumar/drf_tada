# -*- coding: utf-8 -*-

from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import BasePermission


class BaseTodoPermission(BasePermission):
    def _get(self, pk):
        from interactors import todo_bucket_interactors
        try:
            return todo_bucket_interactors.get(pk=pk).instance
        except ObjectDoesNotExist:
            raise Http404

    def is_owner(self, entity, user_id=None):
        return entity.created_by == user_id


class TodoBucketListPermission(BaseTodoPermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return not user_id is None
        return False


class TodoBucketDetailPermission(BaseTodoPermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        pk = view.kwargs['todo_bucket_pk']
        if request.method == 'GET':
            return self.can_read(pk=pk, user_id=user_id)
        elif request.method == 'PATCH':
            return self._is_same_user(pk=pk, user_id=user_id)
        elif request.method == 'DELETE':
            return self._is_same_user(pk=pk, user_id=user_id)
        elif request.method == 'POST':
            # this is needed when Task is getting created
            return self._is_same_user(pk=pk, user_id=user_id)
        return False

    def can_read(self, pk, user_id=None):
        entity = self._get(pk=pk)
        if entity.is_public is True:
            return True
        return self.is_owner(entity=entity, user_id=user_id)

    def _is_same_user(self, pk, user_id):
        entity = self._get(pk=pk)
        return self.is_owner(entity=entity, user_id=user_id)
