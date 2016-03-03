# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase  
from django.utils.translation import activate
 
class HomeNewVisitorTest(StaticLiveServerTestCase): 
    def setUp(self):
        activate('en-us')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
 
    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("nanomedicinelab", self.browser.title)

    # def test_home_files(self):
    #     self.browser.get(self.live_server_url + "/robots.txt")
    #     self.assertNotIn("Not Found", self.browser.title)
    #     self.browser.get(self.live_server_url + "/humans.txt")
    #     self.assertNotIn("Not Found", self.browser.title)

    def test_internationalization(self):
        for lang, h3_text in [('en-us', 'Welcome !'),
                                    ('fr', 'Bienvenue !')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h3 = self.browser.find_element_by_tag_name("h3")
            self.assertEqual(h3.text, h3_text)
