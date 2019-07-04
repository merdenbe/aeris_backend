import requests
import ujson
import unittest


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/reauthenticate'


class TestReauthenticate(unittest.TestCase):

    def test_valid_combo(self):
        body = {
            'email': 'susanJones@gmail.com',
            'password': 'password'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 200)

    def test_invalid_combo(self):
        body = {
            'email': 'susanJones@gmail.com',
            'password': 'passwordpassword'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 401)

    def test_invalid_request(self):
        body = {
            'email': 'susanJones@gmail.com'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)

    def test_unknown_email(self):
        body = {
            'email': 'unkown32489270348@gmail.com'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 401)
