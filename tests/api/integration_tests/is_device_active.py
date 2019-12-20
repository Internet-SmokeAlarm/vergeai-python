import unittest

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi

class IT_IsDeviceActiveTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        device_2 = client.register_device(group.get_id())

        self.assertTrue(client.is_device_active(group.get_id(), device.get_id()))
        self.assertFalse(client.is_device_active(group.get_id(), device_2.get_id()))

        client.delete_group(group.get_id())
