import unittest

from fedlearn.api_client import ApiClient

class UT_FedLearnApiClientTestCase(unittest.TestCase):

    def test_assemble_url(self):
        api_client = ApiClient("GATEWAY_URL", "API_KEY")

        base_url = "/v1/ROUND_ID/GROUP_ID/hello_world"
        data = {
            "ROUND_ID" : "1234",
            "GROUP_ID" : "456456"
        }

        built_url = api_client._assemble_url(base_url, data)

        self.assertEqual("/v1/1234/456456/hello_world", built_url)
