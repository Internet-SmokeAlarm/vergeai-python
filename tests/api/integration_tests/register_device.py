import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_RegisterDeviceTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)
        group = client.create_group("sim_test_group")

        device = client.register_device(group.get_id())

        self.assertIsNotNone(device.get_id())
        self.assertIsNotNone(device.get_api_key())

        client.delete_group(group.get_id())
