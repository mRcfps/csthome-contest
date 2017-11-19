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
        self.contestant = Contestant.objects.create(
            user=self.user,
            name='marc'
        )
        self.client = APIClient()

    def test_login(self):
        url = reverse('users:login')
        data = {'username': 'test', 'password': 'test'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], None)
        self.assertNotEqual(response.data['id'], None)

        self.contestant.refresh_from_db()
        self.assertEqual(self.contestant.logged, True)


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

    def test_get_contestants_list(self):
        url = reverse('users:contestant_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contestant_detail(self):
        url = reverse('users:contestant_detail', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.contestant.name)

    def test_update_contestant_detail(self):
        url = reverse('users:contestant_detail', args=[self.user.id])
        data = {'user': self.user.id, 'name': 'marc', 'score': 100}
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.contestant.refresh_from_db()
        self.assertEqual(self.contestant.score, 100)
