# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from commons.base_testcase import BaseApiTestCase

User = get_user_model()


class TaskListApiTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
                'is_public': False}

        resp = self.client.post(url, format='json', data=data)
        self.todo_bucket_id = resp.data['id']
        self.todo_bucket_url = reverse('todo-bucket-detail',
                                       args=[self.todo_bucket_id])

    def test_create_task_without_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        client = APIClient()
        resp = client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_task_with_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED

        assert resp.data['id']
        assert resp.data['title'] == data['title']
        assert resp.data['created']
        assert resp.data['modified']
        assert resp.data['created_by'] == self.user.id

    def test_create_task_by_non_owner_of_bucket(self):
        user = User.objects.create(first_name="first_name",
                                   last_name="last_name",
                                   username="username",
                                   email="foo@foo.org")
        client = APIClient()
        client.force_authenticate(user=user)

        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add Readme'}
        resp = client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_403_FORBIDDEN


class TaskDetailApiViewTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
                'is_public': False}

        resp = self.client.post(url, format='json', data=data)
        self.todo_bucket_id = resp.data['id']
        self.todo_bucket_url = reverse('todo-bucket-detail',
                                       args=[self.todo_bucket_id])

    def test_read_task_with_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        resp = self.client.get(url, format='json')

        assert resp.data['id']
        assert resp.data['notes'] == []
        assert resp.data['title'] == data['title']
        assert resp.data['created']
        assert resp.data['modified']
        assert resp.data['created_by'] == self.user.id

    def test_read_task_without_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        client = APIClient()
        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_task_without_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        client = APIClient()
        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_task_with_login(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        resp = self.client.delete(url, format='json')

        assert resp.status_code == status.HTTP_204_NO_CONTENT

    def test_update_task_title(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        data['title'] = 'Foo'
        resp = self.client.patch(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

        assert resp.data['title'] == data['title']

    def test_update_task_is_archived(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        data = {'is_archived': True}
        resp = self.client.patch(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

        assert resp.data['is_archived'] == data['is_archived']

    def test_update_task_due_date_and_reminder(self):
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        url = reverse('task-detail', args=[self.todo_bucket_id,
                                           resp.data['id']])

        data = {'due_date': 1429465000, 'reminder': 1429465000}
        resp = self.client.patch(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

        assert int(resp.data['due_date']) == data['due_date']
        assert int(resp.data['reminder']) == data['reminder']


class NoteListApiTestCase(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        url = reverse('todo-bucket-list')
        data = {'title': 'Release 0.1',
                'description': 'List of tasks required to release the project',
                'is_public': False}

        resp = self.client.post(url, format='json', data=data)
        self.todo_bucket_id = resp.data['id']
        self.todo_bucket_url = reverse('todo-bucket-detail',
                                       args=[self.todo_bucket_id])
        url = reverse('task-list', args=[self.todo_bucket_id])
        data = {'title': 'Add some more tests'}
        resp = self.client.post(url, format='json', data=data)

        assert resp.status_code == status.HTTP_201_CREATED
        self.task_id = resp.data['id']
        self.task_url = reverse('task-detail', args=[self.todo_bucket_id,
                                                     self.task_id])

    def test_create_note(self):
        kwargs = {'todo_bucket_pk': self.todo_bucket_id,
                  'task_pk': self.task_id}
        url = reverse('note-list', kwargs=kwargs)
        data = {'description': 'Write tests which will write tests'}
        resp = self.client.post(url, data=data, format='json')

        assert resp.status_code == status.HTTP_201_CREATED

        assert resp.data['id']
        assert resp.data['description'] == data['description']
        assert resp.data['created']
        assert resp.data['modified']

        expected_uri = '{}notes/{}/'.format(self.task_url, resp.data['id'])
        assert resp.data['resource_uri'] == expected_uri

    def test_read_note(self):
        kwargs = {'todo_bucket_pk': self.todo_bucket_id,
                  'task_pk': self.task_id}
        url = reverse('note-list', kwargs=kwargs)
        data = {'description': 'Write tests which will write tests'}
        resp = self.client.post(url, data=data, format='json')

        assert resp.status_code == status.HTTP_201_CREATED

        kwargs['note_pk'] = resp.data['id']
        url = reverse('note-detail', kwargs=kwargs)

        resp = self.client.get(url, format='json')

        assert resp.data['id']
        assert resp.data['description'] == data['description']
        assert resp.data['created']
        assert resp.data['modified']
        assert resp.data['resource_uri'] == url

    def test_delete_note(self):
        kwargs = {'todo_bucket_pk': self.todo_bucket_id,
                  'task_pk': self.task_id}
        url = reverse('note-list', kwargs=kwargs)
        data = {'description': 'Write tests which will write tests'}
        resp = self.client.post(url, data=data, format='json')

        assert resp.status_code == status.HTTP_201_CREATED

        kwargs['note_pk'] = resp.data['id']
        url = reverse('note-detail', kwargs=kwargs)

        resp = self.client.delete(url, format='json')

        assert resp.status_code == status.HTTP_204_NO_CONTENT

    def test_update_note(self):
        kwargs = {'todo_bucket_pk': self.todo_bucket_id,
                  'task_pk': self.task_id}
        url = reverse('note-list', kwargs=kwargs)
        data = {'description': 'Write tests which will write tests'}
        resp = self.client.post(url, data=data, format='json')

        assert resp.status_code == status.HTTP_201_CREATED

        data['description'] = 'Foo'
        kwargs['note_pk'] = resp.data['id']
        url = reverse('note-detail', kwargs=kwargs)

        resp = self.client.patch(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

        assert resp.data['id']
        assert resp.data['description'] == data['description']
        assert resp.data['created']
        assert resp.data['modified']
        assert resp.data['resource_uri'] == url
