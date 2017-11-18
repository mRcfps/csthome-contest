from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Contestant


class UserTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test'
        )
        self.client = APIClient()

    def test_login(self):
        url = reverse('users:login')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], None)


class ContestantTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test', password='test'
        )
        self.contestant = Contestant.objects.create(
            user=self.user,
            name='marc',
            score=50
        )
        self.client = APIClient()

    def test_get_score_board(self):
        url = reverse('users:scores')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['score'], 50)
