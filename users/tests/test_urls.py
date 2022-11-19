from django.test import TestCase
from django.urls import reverse


class UsersUrlsTeste(TestCase):

    def test_profile_urls_is_correct(self):
        url= reverse('profile')
        self.assertEqual(url,'/profile/')
    def test_feed_url_iscorrect(self):
        url=reverse('home')
        self.assertEqual(url,'/')


       






