from urllib import response
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class ProfileViewTestCase(TestCase):

   def test_template_profile(self):
        response = self.client.get(reverse("profile"))
        self.assertTemplateUsed(response,"users/profile.html")

   def test_status_200(self):
      response= self.client.get(reverse('profile'))
      self.assertEqual(response.status_code, 200)

   def test_birth_date(self):
      response = self.client.get(reverse('profile'))



