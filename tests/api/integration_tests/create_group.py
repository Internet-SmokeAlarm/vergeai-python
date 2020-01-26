import unittest

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_CreateGroupTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("sim_test_group")

        self.assertIsNotNone(group.get_id())

        client.delete_group(group.get_id())
