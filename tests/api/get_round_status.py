import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnException
from fedlearn.exceptions import FedLearnApiException

class GetRoundStatusTestCase(unittest.TestCase):

    def test_get_round_status_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id())

        response_learning_round = client.get_round_status(group.get_id(), learning_round.get_id())

        self.assertIsNotNone(response_learning_round)
        self.assertEqual(response_learning_round.get_id(), learning_round.get_id())
        self.assertEqual(0, len(response_learning_round.get_models()))

        client.delete_group(group.get_id())

    def test_get_round_status_fail_invalid_group_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id())
        self.assertRaises(FedLearnApiException, client.get_round_status, None, learning_round.get_id())

        client.delete_group(group.get_id())

    def test_get_round_status_fail_invalid_round_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id())
        self.assertRaises(FedLearnApiException, client.get_round_status, group.get_id(), None)

        client.delete_group(group.get_id())

    def test_get_round_status_fail_nonexistant_round_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id())
        self.assertRaises(FedLearnApiException, client.get_round_status, group.get_id(), "i_dont_exist_woo_hoo")

        client.delete_group(group.get_id())
