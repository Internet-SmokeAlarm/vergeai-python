import unittest

from fedlearn import FedLearnApi

class GroupManagementTestCase(unittest.TestCase):

    def test_create_delete_use_case(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertIsNotNone(group.get_id())

        result = client.delete_group(group.get_id())

        self.assertTrue(result)
