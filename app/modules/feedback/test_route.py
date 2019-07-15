import requests
import ujson
import unittest


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/feedback'


class TestFeedback(unittest.TestCase):

    def test_no_body(self):
        r = requests.post(url=STAGING_URL)

        self.assertTrue(r.status_code, 404)

    def test_incorrect_params(self):
        body = {
            "message": "This is a test of the route."
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)

    def test_valid_post(self):
        body = {
            "msg": "This is a test of the route."
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 200)
