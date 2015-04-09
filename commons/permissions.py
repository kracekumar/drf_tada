# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.id == int(view.kwargs.get('pk', -1))


class LoggedInPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous() is False
