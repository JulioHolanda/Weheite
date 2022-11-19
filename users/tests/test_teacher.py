from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

class ProfessorTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='prof', password='rob12345', email='rob@cesar.com', professor = 1)
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_true_professor(self):
        a = User.objects.get(professor = 1)
        self.assertTrue(a)
    

     