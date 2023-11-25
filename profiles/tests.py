from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTest(TestCase):
    def test_profile_creation(self):
        profile = User(first_name = 'Juan', last_name = 'Carlos')
        profile.save()

        self.assertEqual(profile.first_name, 'Juan')
        self.assertEqual(profile.last_name, 'Carlos')