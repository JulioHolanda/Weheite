from django.test import TestCase
from django.urls import reverse


class UsersUrlsTeste(TestCase):
    
    def test_feed_url_iscorrect(self):
        url=reverse('home')
        self.assertEqual(url,'/')

       






