# -*- coding: utf-8 -*-
# from django.http import Http404
# from django.core.exceptions import ObjectDoesNotExist

# from rest_framework.permissions import BasePermission
# from todo import permissions


# class BaseTaskPermission(BasePermission):
#     def _get(self, pk):
#         from interactors import task_interactors
#         try:
#             return task_interactors.get(pk=pk).instance
#         except ObjectDoesNotExist:
#             raise Http404

#     def is_owner(self, entity, user_id=None):
#         return entity.created_by == user_id


# class TodoBucketListPermission(BaseTodoPermission):
#     def has_permission(self, request, view):
#         user_id = request.user.id
#         if request.method == 'GET':
#             return True
#         elif request.method == 'POST':
#             return not user_id is None
#         return False


# class TodoBucketDetailPermission(BaseTodoPermission):
#     def has_permission(self, request, view):
#         user_id = request.user.id
#         if request.method == 'GET':
#             return self.can_read(pk=view.kwargs['todo_bucket_pk'],
#                                  user_id=user_id)
#         elif request.method == 'PATCH':
#             return self.can_update(pk=view.kwargs['todo_bucket_pk'],
#                                    user_id=user_id)
#         elif request.method == 'DELETE':
#             return self.can_delete(pk=view.kwargs['todo_bucket_pk'],
#                                    user_id=user_id)
#         return False

#     def can_read(self, pk, user_id=None):
#         entity = self._get(pk=pk)
#         if entity.is_public is True:
#             return True
#         return self.is_owner(entity=entity, user_id=user_id)

#     def can_delete(self, pk, user_id=None):
#         entity = self._get(pk=pk)
#         return self.is_owner(entity=entity, user_id=user_id)

#     def can_update(self, pk, user_id=None):
#         entity = self._get(pk=pk)
#         return self.is_owner(entity=entity, user_id=user_id)

# from rest_framework.permissions import BasePermission



# def can_access(task_entity, user_id=None):
#     return permissions.can_access(
#         todo_bucket_entity=task_entity.bucket,
#         user_id=user_id)


# def can_create(task_entity, user_id):
#     return permissions.is_owner(
#         todo_bucket_entity=task_entity.bucket,
#         user_id=user_id)


# def can_delete(task_entity, user_id=None):
#     return permissions.can_delete(
#         todo_bucket_entity=task_entity.bucket,
#         user_id=user_id)


# def can_update(task_entity, user_id=None):
#     return permissions.can_update(
#         todo_bucket_entity=task_entity.bucket,
#         user_id=user_id)


# class TaskPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.is_anonymous() is False
