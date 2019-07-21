import requests
import ujson
import unittest
import os


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/questions'


class TestQuestions(unittest.TestCase):

    def test_valid_post(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            "question": "Couldnt see me as spider man, but now Im spitten venom?",
            "user_email": "merdenbe@nd.edu"
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 200)

    def test_valid_get(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}

        r = requests.get(url=STAGING_URL, headers=headers)

        self.assertTrue(r.status_code, 200)
