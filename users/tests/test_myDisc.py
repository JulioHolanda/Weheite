from urllib import response
from django.test import TestCase
from django.urls import reverse

class myDiscViewTestCase(TestCase):

   def test_template_profile(self):
        response = self.client.get(reverse("myDiscs"))
        self.assertTemplateUsed(response,"users/myDiscs.html")

   def test_status_200(self):
      response= self.client.get(reverse('myDiscs'))
      self.assertEqual(response.status_code, 200)