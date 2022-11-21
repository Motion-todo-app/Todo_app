from django.test import TestCase
from .models import User
from django.conf import settings

# Create your tests here.
class UserManagerTestCase(TestCase):
    def test_main_create_user(self):
        user = CustomUser.objects.create_user('jdoe@gmail.com', 'password123')
        self.assertTrue(isinstance(user, User))
