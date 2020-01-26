import unittest

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_DeleteGroupTestCase(unittest.TestCase):

    def test_pass_nonexistant_group(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        self.assertTrue(client.delete_group("i_dont_exist_woo_hoo"))
