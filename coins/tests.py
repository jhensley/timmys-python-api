from django.test import TestCase
import json

class TestCoinsAPI(TestCase):
    def test_total(self):

        response = self.client.get("/coins?total=22.20")
        total = response.json()["total"]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(type(total), float)
        self.assertEqual(total, 22.20)

        self.assertEqual(type(response.json()["coins"]), dict)
    