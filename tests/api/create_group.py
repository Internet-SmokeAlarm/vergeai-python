import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class CreateGroupTestCase(unittest.TestCase):

    def test_create_group_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertIsNotNone(group.get_id())

        client.delete_group(group.get_id())

    def test_create_group_fail_invalid_name(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.create_group, None)
