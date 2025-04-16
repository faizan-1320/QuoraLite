# answer/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from question.models import Question
from answer.models import Answer

User = get_user_model()

class AnswerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='responder', password='pass123')
        self.question = Question.objects.create(title='What is Django?', body='Explain Django framework.', user=self.user)

    def test_answer_creation(self):
        answer = Answer.objects.create(body='Django is a Python web framework.', user=self.user, question=self.question)
        self.assertEqual(answer.body, 'Django is a Python web framework.')
        self.assertEqual(answer.question.title, 'What is Django?')
        self.assertEqual(answer.user.username, 'responder')
