from django.test import TestCase
import json

class TestPeopleAPI(TestCase):
    def test_greeting(self):
        data = {
            "job": "doctor",
            "name": "Sally",
            "patients": ["Bob", "Mohammed", "Claire"]
        }
        response = self.client.post("/people", json.dumps(data), content_type="application/json")
        greeting = response.json()["greeting"]

        self.assertEqual(response.status_code, 200)

        # We have to encode the value to detect type
        self.assertEqual(type(greeting.encode('utf-8')), str)
        self.assertEqual(greeting, "Hi Sally!")
    
    def test_treatments(self):
        data = {
            "job": "doctor",
            "name": "Sally",
            "patients": ["Bob", "Mohammed", "Claire"]
        }
        response = self.client.post("/people", json.dumps(data), content_type="application/json")
        patients = response.json()["patients"]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(type(patients), list)

        self.assertEqual(patients[0]["patient"], "Bob")
        self.assertEqual(patients[0]["treatment"], "flu shot")

        self.assertEqual(patients[1]["patient"], "Mohammed")
        self.assertEqual(patients[1]["treatment"], "flu shot")

        self.assertEqual(patients[2]["patient"], "Claire")
        self.assertEqual(patients[2]["treatment"], "flu shot")

    def test_vet_treatments(self):
        data = {
            "job": "vet",
            "name": "Steve",
            "patients": ["Pickles", "Mr. Bojangles"]
        }
        response = self.client.post("/people", json.dumps(data), content_type="application/json")
        patients = response.json()["patients"]

        self.assertEqual(response.status_code, 200)

        self.assertEqual(type(patients), list)

        self.assertEqual(patients[0]["patient"], "Pickles")
        self.assertEqual(patients[0]["treatment"], "shots and a chew toy")

        self.assertEqual(patients[1]["patient"], "Mr. Bojangles")
        self.assertEqual(patients[1]["treatment"], "shots and a chew toy")