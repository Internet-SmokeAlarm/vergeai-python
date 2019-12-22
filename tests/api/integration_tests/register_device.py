import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_RegisterDeviceTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        device = client.register_device(group.get_id())

        self.assertIsNotNone(device.get_id())
        self.assertIsNotNone(device.get_api_key())

        client.delete_group(group.get_id())

    def test_fail_nonexistant_group_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.register_device, "i_dont_exist_100_guarantee")
