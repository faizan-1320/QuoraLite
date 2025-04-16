# user/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('pass123'))
        self.assertEqual(user.email, 'test@example.com')
