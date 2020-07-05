import vergeai
from ..abstract_testcase import AbstractTestCase


class IT_APIKeyTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        key_plaintext = vergeai.APIKey.create().data["key"]

        self.assertIsNotNone(key_plaintext)
