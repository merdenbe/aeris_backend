import requests
import unittest


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/majors'


class TestMajor(unittest.TestCase):

    def test_valid_request(self):
        r = requests.get(url=STAGING_URL)

        self.assertTrue(r.status_code, 200)
