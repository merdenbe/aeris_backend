import requests
import ujson
import unittest


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/register'


class TestRegister(unittest.TestCase):

    def test_valid_request(self):
        body = {
            'email': 'susanJones@gmail.com',
            'password': 'password',
            'firstName': 'Susan',
            'lastName': 'Jones',
            'gradYear': 2020,
            'major': 'Computer Science'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 200)

    def test_invalid_request(self):
        body = {
            'email': 'susanJones@gmail.com',
            'password': 'password',
            'major': 'Computer Science'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)
