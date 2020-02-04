import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_IsDeviceActiveTestCase(unittest.TestCase):

    def test_fail_invalid_device_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, "213234", "213234", 12344)

    def test_fail_invalid_device_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, "2jlk23", "213234", None)

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, 1234, "213234", "213234")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, None, "213234", "2jlk23")

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, "1234", 1234, "213234")

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.is_device_active, "None", None, "2jlk23")
