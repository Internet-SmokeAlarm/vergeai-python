import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_RegisterDeviceTestCase(unittest.TestCase):

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.register_device, None)

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.register_device, 123124)
