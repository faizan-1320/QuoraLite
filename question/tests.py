# question/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from question.models import Question

User = get_user_model()

class QuestionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='asker', password='pass123')

    def test_question_creation(self):
        question = Question.objects.create(title='What is Django?', body='Explain Django framework.', user=self.user)
        self.assertEqual(question.title, 'What is Django?')
        self.assertEqual(question.user.username, 'asker')
