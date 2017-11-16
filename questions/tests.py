from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import Single, Multiple


class SingleQuestionTests(APITestCase):

    def setUp(self):
        """Set up API client and initialize some questions."""
        self.client = APIClient()

        self.q1 = Single.objects.create(question='q1', answer='A')
        self.q2 = Single.objects.create(question='q2', answer='B')

    def test_get_question_by_id(self):
        """Ensure that we can correctly get the question by its id."""
        url = reverse('question:single_detail')
        response = self.client.get(url, args=[self.q1.id])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], self.q1.question)
        self.assertEqual(response.data['answer'], self.q1.answer)


class MultipleQuestionTests(APITestCase):

    def setUp(self):
        """Set up API client and initialize some questions."""
        self.client = APIClient()

        self.q1 = Multiple.objects.create(question='q1_multi', answer='ABC')
        self.q2 = Multiple.objects.create(question='q2_multi', answer='BCDEFG')

    def test_get_question_by_id(self):
        """Ensure that we can correctly get the question by its id."""
        url = reverse('question:multiple_detail')
        response = self.client.get(url, args=[self.q2.id])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], self.q2.question)
        self.assertEqual(response.data['answer'], self.q2.answer)
