from selenium import webdriver
from django.test import LiveServerTestCase, TestCase


class Interface_Test(LiveServerTestCase):
    def setUp(self):
        self.browser =webdriver.Chrome()
        

    def tearDown(self):
        self.browser.close()

    def test_alert(self):
        self.browser.get(self.live_server_url)
        