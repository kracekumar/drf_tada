# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from commons.base_testcase import BaseApiTestCase


class TodoBucketApiTestCase(BaseApiTestCase):
    def test_todo_bucket_creation(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
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
        data = {'description': 'List of tasks required to release the project',
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

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_todo_bucket_read_detail_when_doesnt_exists(self):
        pk = 23
        url = reverse('todo-bucket-detail', args=[pk])

        resp = self.client.get(url, format='json')

        assert resp.status_code == status.HTTP_404_NOT_FOUND

    def test_todo_bucket_list(self):
        url = reverse('todo-bucket-list')

        for i in range(5):
            data = {'title': 'title {}'.format(i)}
            resp = self.client.post(url, format='json', data=data)
            assert resp.status_code == status.HTTP_201_CREATED

        resp = self.client.get(url, format='json')

        assert resp.status_code == status.HTTP_200_OK

        assert resp.data['meta']
        assert resp.data['meta']['limit'] == 20
        assert resp.data['meta']['offset'] == 0
        assert resp.data['meta']['total'] == 5

        assert resp.data['objects']
        assert len(resp.data['objects']) == 5

    def test_todo_bucket_list_with_custom_offset_limit(self):
        offset, limit = 0, 3
        url = reverse('todo-bucket-list')
        url = url + '?limit={}&offset={}'.format(limit, offset)

        for i in range(5):
            data = {'title': 'title {}'.format(i)}
            resp = self.client.post(url, format='json', data=data)
            assert resp.status_code == status.HTTP_201_CREATED

        resp = self.client.get(url, format='json')

        assert resp.status_code == status.HTTP_200_OK

        assert resp.data['meta']
        assert resp.data['meta']['limit'] == limit
        assert resp.data['meta']['offset'] == offset
        assert resp.data['meta']['total'] == 5

        assert resp.data['objects']
        assert len(resp.data['objects']) == limit

        for index, obj in enumerate(resp.data['objects']):
            assert obj['id'] == index + offset + 1

    def test_todo_bucket_list_without_login(self):
        client = APIClient()
        url = reverse('todo-bucket-list')

        for i in range(5):
            data = {'title': 'title {}'.format(i)}
            resp = self.client.post(url, format='json', data=data)
            assert resp.status_code == status.HTTP_201_CREATED

        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_todo_bucket_details(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        url = reverse('todo-bucket-detail', args=[resp.data['id']])

        new_data = {'title': 'Release 0.2'}

        update_resp = self.client.patch(url, data=new_data, format='json')

        assert update_resp.status_code == status.HTTP_202_ACCEPTED

        assert update_resp.data['title'] == new_data['title']

    def test_update_todo_bucket_details_with_invalid_data(self):
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
                'is_public': True}

        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        url = reverse('todo-bucket-detail', args=[resp.data['id']])

        new_data = {'is_public': 0.2}

        update_resp = self.client.patch(url, data=new_data, format='json')

        assert update_resp.status_code == status.HTTP_400_BAD_REQUEST

        assert 'is_public' in update_resp.data
