import unittest

from vergeai.api_resources.utils import assemble_headers

class UT_AssembleHeadersTestCase(unittest.TestCase):

    def test_pass(self):
        api_key = "lkflsaklf23423fdsfaf234"

        headers = assemble_headers(api_key)

        self.assertEqual({"Authorization" : "lkflsaklf23423fdsfaf234"}, headers)
