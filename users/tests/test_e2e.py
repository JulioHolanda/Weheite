from selenium import webdriver
from django.test import LiveServerTestCase, TestCase
import pytest
from selenium.webdriver.common.by import By

import time


class Interface_Test(LiveServerTestCase):
    def setUp(self):
        self.browser =webdriver.Chrome()
        

    def tearDown(self):
        self.browser.close()

    def test_display(self):
        self.browser.get(self.live_server_url)
        time.sleep(10)
        self.browser.find_element(By.ID, 'h1')
        

        
