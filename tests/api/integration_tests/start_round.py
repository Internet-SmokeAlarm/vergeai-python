import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_StartRoundTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id())

        self.assertIsNotNone(learning_round.get_id())

        client.delete_group(group.get_id())

    def test_fail_nonexistant_group(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, "i_dont_exist_woo_hoo")