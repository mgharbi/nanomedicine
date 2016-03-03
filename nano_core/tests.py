# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate
 
class TestHomePage(TestCase):
 
    def test_uses_home_template(self):
        activate('en-us')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "nano_core/home.html")
 
    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")

    def test_uses_nav_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "nano_core/shared/nav.html")
