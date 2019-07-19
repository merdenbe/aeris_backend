import requests
import unittest
import ujson
import os


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/course_requests'


class TestCourseRequests(unittest.TestCase):

    def test_unathorized_get(self):
        headers = {'Authorization': 'Bearer ' + '1234567890'}
        r = requests.get(url=STAGING_URL, headers=headers)

        self.assertTrue(r.status_code, 401)

    def test_valid_get(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        r = requests.get(url=STAGING_URL, headers=headers)
        print(r.status_code)

        body = r.json()
        print(body.keys())

        self.assertNotEqual(body["requested_courses"], None)
        self.assertTrue(r.status_code, 200)

    def test_post_invalid_params(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            'account_id': '5'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 404)

    def test_post_unauthorized(self):
        headers = {'Authorization': 'Bearer ' + '123456790'}
        body = {
            'account_id': '5',
            'title': "will fail"
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 401)

    def test_post_contains_profanity(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            'account_id': '5',
            'title': "shit"
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 404)

    def test_post_bad_accountid(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            'account_id': '123214234234',
            'title': 'Discrete Mathematics'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)

        self.assertTrue(r.status_code, 404)

    def test_post_repeat_request(self):
        headers = {'Authorization': 'Bearer ' + os.environ["TEST_TOKEN"]}
        body = {
            'account_id': '1',
            'title': 'Discrete Mathematics'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body), headers=headers)
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)
