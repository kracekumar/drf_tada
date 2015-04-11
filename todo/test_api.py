# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from commons.base_testcase import BaseApiTestCase


class TodoBucketApiTestCase(BaseApiTestCase):
    def test_todo_bucket_creation(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the proejct',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        assert resp.data['id']
        assert resp.data['title'] == data['title']
        assert resp.data['description'] == data['description']
        assert resp.data['is_public'] == data['is_public']
        assert resp.data['created']
        assert resp.data['modified']

    def test_todo_bucket_creation_without_title(self):
        url = reverse('todo-bucket-list')
        data = {'description': 'List of tasks required to release the proejct',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_400_BAD_REQUEST

        assert 'title' in resp.data

    def test_todo_bucket_creation_without_description(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        assert resp.data['id']
        assert resp.data['title'] == data['title']
        assert resp.data['description'] == ''
        assert resp.data['is_public'] == data['is_public']
        assert resp.data['created']
        assert resp.data['modified']

    def test_todo_bucket_read_detail(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'is_public': False}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        pk = resp.data['id']
        url = reverse('todo-bucket-detail', args=[pk])

        resp = self.client.get(url, format='json')

        assert resp.status_code == status.HTTP_200_OK
        assert resp.data['title'] == data['title']
        assert resp.data['is_public'] == data['is_public']
        assert resp.data['id'] == pk
        assert resp.data['created_by'] == self.user.pk
        assert resp.data['created']
        assert resp.data['modified']

    def test_todo_bucket_read_detail_without_login_for_public_bucket(self):
        client = APIClient()

        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        pk = resp.data['id']
        url = reverse('todo-bucket-detail', args=[pk])

        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_200_OK
        assert resp.data['title'] == data['title']
        assert resp.data['is_public'] == data['is_public']
        assert resp.data['id'] == pk
        assert resp.data['created_by'] == self.user.pk
        assert resp.data['created']
        assert resp.data['modified']

    def test_todo_bucket_read_detail_without_login_for_private_bucket(self):
        client = APIClient()

        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'is_public': False}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        pk = resp.data['id']
        url = reverse('todo-bucket-detail', args=[pk])

        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_403_FORBIDDEN

    # def test_change_password(self):
    #     url = reverse('change-password', args=[self.user.pk])

    #     data = {'password': 'password'}

    #     resp = self.client.post(url, data=data, format='json')

    #     assert resp.status_code == status.HTTP_202_ACCEPTED

    # def test_update_user_details(self):
    #     url = reverse('user-detail', args=[self.user.pk])

    #     data = {'username': 'Joker'}

    #     resp = self.client.patch(url, data=data, format='json')

    #     assert resp.status_code == status.HTTP_202_ACCEPTED

    #     expected_data = {'id': self.user.pk,
    #                      'first_name': self.user.first_name,
    #                      'last_name': self.user.last_name,
    #                      'username': data['username'],
    #                      'email': self.user.email}

    #     assert resp.data == expected_data
