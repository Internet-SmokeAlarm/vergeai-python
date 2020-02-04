import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_CreateApiKeyTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        api_key_plaintext = client.create_api_key()

    def test_not_authorized(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, "im_a_fake_key_woo_hoo")

        self.assertRaises(FedLearnApiException, client.create_api_key)
