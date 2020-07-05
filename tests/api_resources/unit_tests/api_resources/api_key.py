import unittest
import vergeai
from vergeai.clients import DummyClient


class UT_APIKeyTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.APIKey.create()

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'post'!\"})", str(resp))
