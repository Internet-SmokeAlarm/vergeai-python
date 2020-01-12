import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_GetGroupTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("DOES NOT MATTER")
        group = client.create_group("sim_test_group")

        returned_group = client.get_group(group.get_id())

        self.assertEqual(returned_group.get_id(), group.get_id())

        client.delete_group(group.get_id())
