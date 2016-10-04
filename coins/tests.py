from django.test import TestCase
import json

class TestCoinsAPI(TestCase):
    def test_total(self):

        response = self.client.get("/coins?total=22.25")
        total = response.json()["total"]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(type(total), float)
        self.assertEqual(total, 22.25)

        self.assertEqual(type(response.json()["coins"]), dict)

    def test_coins_schema(self):

        response = self.client.get("/coins?total=22.25")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.json()["coins"]), 2)

        self.assertEqual(type(response.json()["coins"]["bars"]), dict)
        self.assertEqual(type(response.json()["coins"]["foos"]), dict)

        # Make sure the Foos object only has 1, 5, 10, 20, 50
        expectedFoos = [u'1', u'5', u'10', u'20', u'50']
        actualFoos = response.json()["coins"]["foos"].keys()
        self.assertEqual(set(expectedFoos), set(actualFoos))

        # Make sure the Bars object only has 1, 2
        expectedBars = [u'1', u'2']
        actualBars = response.json()["coins"]["bars"].keys()
        self.assertEqual(set(expectedBars), set(actualBars))
    
    def test_minimum_coins(self):

        response = self.client.get("/coins?total=22.25")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(type(response.json()["coins"]["bars"]), dict)
        self.assertEqual(type(response.json()["coins"]["foos"]), dict)

        self.assertEqual(response.json()["coins"]["bars"]["2"], 11)
        self.assertEqual(response.json()["coins"]["foos"]["20"], 1)
        self.assertEqual(response.json()["coins"]["foos"]["5"], 1)

        self.assertEqual(response.json()["coins"]["bars"]["1"], 0)
        self.assertEqual(response.json()["coins"]["foos"]["1"], 0)
        self.assertEqual(response.json()["coins"]["foos"]["10"], 0)
        self.assertEqual(response.json()["coins"]["foos"]["50"], 0)

    