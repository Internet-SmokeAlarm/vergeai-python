import unittest

from vergeai.clients import DummyClient

class UT_DummyClientTestCase(unittest.TestCase):

    def test_post_pass(self):
        client = DummyClient()
        response = client.post({}, "url")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"object_name" : "you called 'post'!"})
        self.assertEqual(response.json, {
            "status_code" : 200,
            "data" : {"object_name" : "you called 'post'!"}
        })

    def test_get_pass(self):
        pass
