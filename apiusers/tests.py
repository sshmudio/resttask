from rest_framework.test import APIRequestFactory
from django.contrib.auth.hashers import make_password, get_hashers, is_password_usable
from apiusers.models import Users
from datetime import datetime
import time
from django.test import TestCase
import grequests
import requests
from faker import Faker
import random
import string
from apiusers.views import UserDetail
fake = Faker()


class TestQuery(TestCase):
    username = 'suppor'
    email = 'exampleemail@mail.net'
    password = 'examplepassword1'

    def setUp(self):
        Users.objects.create(username=self.username, email=self.email,
                             password=make_password(self.password))

    def test_write_data(self):
        test_username = Users.objects.get(username=self.username)
        self.assertEqual(test_username.email, self.email)
