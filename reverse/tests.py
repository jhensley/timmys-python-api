# -*- coding: utf-8 -*-

from django.test import TestCase

# Create your tests here.

class TestReverseAPI(TestCase):
    def test_simple_string(self):

        response = self.client.post("/reverse?input=foobar")
        reversed = response.json()["reversed"]

        self.assertEqual(response.status_code, 200)

        # We have to encode the value to detect type
        self.assertEqual(type(reversed.encode('utf-8')), str)
        self.assertEqual(reversed, "raboof")

    def test_twobyte_character_string(self):

        response = self.client.post("/reverse?input=éöÿ")
        reversed = response.json()["reversed"]

        self.assertEqual(response.status_code, 200)

        # We have to encode the value to detect type
        self.assertEqual(type(reversed.encode('utf-8')), str)
        self.assertEqual(reversed, u"ÿöé")

    def test_reverse_float_zero_decimals(self):

        response = self.client.post("/reverse?input=309834")
        reversed = response.json()["reversed"]

        self.assertEqual(response.status_code, 200)

        # We have to encode the value to detect type
        self.assertEqual(type(reversed), float)
        self.assertEqual(reversed, 438903)

    def test_reverse_float(self):

        response = self.client.post("/reverse?input=34.09")
        reversed = response.json()["reversed"]

        self.assertEqual(response.status_code, 200)

        # We have to encode the value to detect type
        self.assertEqual(type(reversed), float)
        self.assertEqual(reversed, 90.43)