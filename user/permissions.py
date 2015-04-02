# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.id == int(view.kwargs.get('pk', -1))
