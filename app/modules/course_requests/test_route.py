import requests
import unittest
import ujson


STAGING_URL = 'https://aris-backend-staging.herokuapp.com/course_requests'


class TestCourseRequests(unittest.TestCase):

    def test_valid_get(self):
        r = requests.get(url=STAGING_URL)
        body = r.json()

        self.assertNotEqual(body["requested_courses"], None)
        self.assertTrue(r.status_code, 200)

    def test_post_invalid_params(self):
        body = {
            'account_id': '5'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)

    def test_post_contains_profanity(self):
        body = {
            'account_id': '5',
            'title': "shit"
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)

    def test_post_bad_accountid(self):
        body = {
            'account_id': '123214234234',
            'title': 'Discrete Mathematics'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)

    def test_post_repeat_request(self):
        body = {
            'account_id': '1',
            'title': 'Discrete Mathematics'
        }
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))
        r = requests.post(url=STAGING_URL, data=ujson.dumps(body))

        self.assertTrue(r.status_code, 404)
