from .base import BaseTest
from fedlearn.exceptions import FedLearnApiException

class IT_RegisterDeviceTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")

        device = self.client.register_device(group.get_id())

        self.assertIsNotNone(device.get_id())
        self.assertIsNotNone(device.get_api_key())

        self.client.delete_group(group.get_id())
