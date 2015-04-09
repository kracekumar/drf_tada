# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIClient

from commons.base_testcase import BaseApiTestCase


class UserApiTestCase(BaseApiTestCase):
    def test_user_read_detail(self):
        url = reverse('user-detail', args=[self.user.pk])
        data = {'id': self.user.pk,
                'first_name': self.user.first_name,
                'last_name': self.user.last_name,
                'username': self.user.username,
                'email': self.user.email}

        resp = self.client.get(url, format='json')

        assert resp.status_code == status.HTTP_200_OK
        assert resp.data == data

    def test_user_read_detail_without_login(self):
        client = APIClient()
        url = reverse('user-detail', args=[self.user.pk])

        resp = client.get(url, format='json')

        assert resp.status_code == status.HTTP_401_UNAUTHORIZED

    def test_change_password(self):
        url = reverse('change-password', args=[self.user.pk])

        data = {'password': 'password'}

        resp = self.client.post(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

    def test_update_user_details(self):
        url = reverse('user-detail', args=[self.user.pk])

        data = {'username': 'Joker'}

        resp = self.client.patch(url, data=data, format='json')

        assert resp.status_code == status.HTTP_202_ACCEPTED

        expected_data = {'id': self.user.pk,
                         'first_name': self.user.first_name,
                         'last_name': self.user.last_name,
                         'username': data['username'],
                         'email': self.user.email}

        assert resp.data == expected_data
