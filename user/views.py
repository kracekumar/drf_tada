# -*- coding: utf-8 -*-

from django.http import JsonResponse

# Third party import
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Non current app imports

from commons.decorators import handle_doesnt_exists_exception
from interactors import user_interactors

# current app imports
from .permissions import UserPermission
from .serializers import (UserReadSerializer, UserPasswordSerializer,
                          UserUpdateSerializer)


class UserDetailApiView(views.APIView):
    allowed_methods = ['GET', 'PATCH']
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get(self, request, pk):
        user_entity = user_interactors.get(pk=pk)
        if user_entity:
            serialized_obj = UserReadSerializer(instance=user_entity)
            return Response(data=serialized_obj.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @handle_doesnt_exists_exception
    def patch(self, request, pk):
        user_entity = user_interactors.get(pk=pk)
        data = request.DATA
        user_entity.bulk_update(**data)
        obj = UserUpdateSerializer(data=user_entity.to_dict())
        if obj.is_valid():
            # Update the entities after validation
            user_entity.bulk_update(**obj.data)
            new_user_entity = user_interactors.update(
                user_entity, update_fields=obj.data.keys())
            resp_obj = UserReadSerializer(instance=new_user_entity)
            return Response(status=status.HTTP_202_ACCEPTED,
                            data=resp_obj.data)
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)


class UserChangePasswordApiView(views.APIView):
    allowed_methods = ['POST']
    permission_classes = [UserPermission]
    authentication_classes = [TokenAuthentication]

    def post(self, request, pk):
        obj = UserPasswordSerializer(data=request.DATA)
        if obj.is_valid():
            user_interactors.set_password(user_id=pk,
                                          password=obj.data.get('password'))
            return Response(status=status.HTTP_202_ACCEPTED, data={})
        return Response(status=status.HTTP_400_BAD_REQUEST, data=obj.errors)


class UserListApiView(views.APIView):
    pass
