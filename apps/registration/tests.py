from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
   def setUp(self):
      # Creamos un usuario de pruebas
      User.objects.create_user('test','test@test.com', 'test1234')
   # Ejecutamos nuestro test
   def test_profile_exists(self):
      exists = Profile.objects.filter(user__username='test').exists()
      self.assertEqual(exists,True)

