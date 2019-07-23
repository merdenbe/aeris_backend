import requests
import ujson
import unittest
import os


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/profile'


class TestProfile(unittest.TestCase):

    def test_valid_post(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {'account_id': 8}
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 200)

    def test_valid_put(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            'gradYear': '2020',
            'firstName': 'Michael',
            'lastName': 'Smith',
            'major': 'Computer Science'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 200)
