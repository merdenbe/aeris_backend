import requests
import ujson
import unittest
import os


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/feedback'


class TestFeedback(unittest.TestCase):

    def test_no_body(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        r = requests.post(url=STAGING_URL, headers=headers)

        self.assertTrue(r.status_code, 404)

    def test_incorrect_params(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            "message": "This is a test of the route."
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 404)

    def test_unathorized_post(self):
        headers = {'Authorization': 'Bearer ' + '1235467800'}
        body = {
            "msg": "This is a test of the route."
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 200)

    def test_valid_post(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            "msg": "This is a test of the route."
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 200)
