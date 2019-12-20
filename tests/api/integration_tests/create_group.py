import unittest

from fedlearn import FedLearnApi

class IT_CreateGroupTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertIsNotNone(group.get_id())

        client.delete_group(group.get_id())
