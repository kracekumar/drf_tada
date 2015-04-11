# -*- coding: utf-8 -*-

# Third party import
from rest_framework import views, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

# Non current app imports

from commons.decorators import handle_doesnt_exists_exception
from commons.permissions import LoggedInPermission
from commons.response import make_response

from interactors import todo_bucket_interactors

# current app imports
from .todo_bucket_entity import TodoBucketEntity
from .serializers import (TodoBucketWriteSerializer, TodoBucketReadSerializer,
                          TodoBucketUpdateSerializer)


class TodoBucketListApiView(views.APIView):
    allowed_methods = ['GET', 'POST']
    authentication_classes = [TokenAuthentication]
    permission_classes = [LoggedInPermission]

    def post(self, request):
        data = request.DATA
        obj = TodoBucketWriteSerializer(data=data)
        if obj.is_valid():
            dictionary = dict(obj.data)
            dictionary['created_by'] = request.user.id
            todo_bucket_entity = TodoBucketEntity.from_dict(
                dictionary=dictionary)

            resp = todo_bucket_interactors.create(
                todo_bucket_entity=todo_bucket_entity)
            return make_response(obj=resp,
                                 serializer_cls=TodoBucketReadSerializer)

        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data=obj.errors)


class TodoBucketDetailApiView(views.APIView):
    allowed_methods = ['GET', 'PATCH']
    authentication_classes = [TokenAuthentication]

    @handle_doesnt_exists_exception
    def get(self, request, pk):
        entity = todo_bucket_interactors.get(pk=pk,
                                             user_id=request.user.id)
        return make_response(obj=entity,
                             serializer_cls=TodoBucketReadSerializer)

#     @handle_doesnt_exists_exception
#     def patch(self, request, pk):
#         user_entity = user_interactors.get(pk=pk)
#         data = request.DATA
#         user_entity.bulk_update(**data)
#         obj = UserUpdateSerializer(data=user_entity.to_dict())
#         if obj.is_valid():
#             # Update the entities after validation
#             user_entity.bulk_update(**obj.data)
#             new_user_entity = user_interactors.update(
#                 user_entity, update_fields=obj.data.keys())
#             resp_obj = UserReadSerializer(instance=new_user_entity)
#             return Response(status=status.HTTP_202_ACCEPTED,
#                             data=resp_obj.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST,
#                         data=obj.errors)


# class UserChangePasswordApiView(views.APIView):
#     allowed_methods = ['POST']
#     permission_classes = [UserPermission]
#     authentication_classes = [TokenAuthentication]

#     def post(self, request, pk):
#         obj = UserPasswordSerializer(data=request.DATA)
#         if obj.is_valid():
#             user_interactors.set_password(user_id=pk,
#                                           password=obj.data.get('password'))
#             return Response(status=status.HTTP_202_ACCEPTED, data={})
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=obj.errors)


# class UserListApiView(views.APIView):
#     pass
