from urllib import response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class ProfileViewTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='prof', password='rob12345', email='rob@cesar.com', professor = 1)
        
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_true_professor(self):
        a = User.objects.get(professor = 1)
        self.assertTrue(a)
    
    def test_username(self):
        a = User.objects.get(username = 'prof')
        self.assertTrue(a)

    def test_email(self):
        a = User.objects.get(email = 'rob@cesar.com')
        self.assertTrue(a)

    


# class ProfileViewTestCase(TestCase):

#    def test_template_profile(self):
#         response = self.client.get(reverse("profile"))
#         self.assertTemplateUsed(response,"users/profile.html")

#    def test_status_200(self):
#       response= self.client.get(reverse('profile'))
#       self.assertEqual(response.status_code, 200)

#    def test_birth_date(self):
#       response = self.client.get(reverse('profile'))
#       self.assertNotEqual(response, None)

   