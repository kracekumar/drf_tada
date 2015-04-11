# -*- coding: utf-8 -*-

from rest_framework.permissions import BasePermission


class LoggedInPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_anonymous() is False
