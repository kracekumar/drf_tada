# -*- coding: utf-8 -*-

# Third party import
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Non current app imports

from interactors import user_interactors

# current app imports
from .permissions import UserPermission
from .serializers import UserSerializer


class UserDetailApiView(views.APIView):
    allowed_methods = ['GET', 'PATCH']
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, request, pk=None):
        user_entity = user_interactors.get(pk=pk)
        if user_entity:
            serialized_obj = UserSerializer(data=user_entity.to_dict())
            if serialized_obj.is_valid():
                return Response(data=serialized_obj.data)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=serialized_obj.errors)
        return Response(status=status.HTTP_404_NOT_FOUND)


class UserListApiView(views.APIView):
    pass
