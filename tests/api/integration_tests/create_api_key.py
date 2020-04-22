from .base import BaseTest
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_CreateApiKeyTestCase(BaseTest):

    def test_pass(self):
        api_key_plaintext = self.client.create_api_key()

    def test_not_authorized(self):
        client = FedLearnApi(self.cloud_gateway_url, "im_a_fake_key_woo_hoo")

        self.assertRaises(FedLearnApiException, client.create_api_key)
