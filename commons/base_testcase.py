# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


class BaseApiTestCase(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.email = "johndoe@example.com"
        self.first_name = 'John'
        self.last_name = 'Doe'
        self.username = 'johndoe'
        self.user = User.objects.create(first_name=self.first_name,
                                        last_name=self.last_name,
                                        username=self.username,
                                        email=self.email)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
