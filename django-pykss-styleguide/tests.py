#!/usr/bin/env python

from django.test import TestCase
from django.core.urlresolvers import reverse


class StyleguideTest(TestCase):

    def test_styleguide(self):
        url = reverse('django-pykss-styleguide:styleguide')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
