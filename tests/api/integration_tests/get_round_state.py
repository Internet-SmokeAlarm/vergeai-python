import unittest

from fedlearn.models import RoundConfiguration
from fedlearn.models import RoundStatus
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundStateTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))

        round = client.get_round_state(group.get_id(), learning_round.get_id())

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round.get_id())
        self.assertEqual(RoundStatus.IN_PROGRESS, round.get_status())
        self.assertEqual(round.get_previous_round_id(), "N/A")

        client.delete_group(group.get_id())

    def test_pass_2(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        learning_round_2 = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))

        round = client.get_round_state(group.get_id(), learning_round_2.get_id())

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round_2.get_id())
        self.assertEqual(RoundStatus.IN_PROGRESS, round.get_status())
        self.assertEqual(round.get_previous_round_id(), learning_round.get_id())

        client.delete_group(group.get_id())

    def test_fail_nonexistant_round_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        self.assertRaises(FedLearnApiException, client.get_round_state, group.get_id(), "i_dont_exist_woo_hoo")

        client.delete_group(group.get_id())

    def test_fail_nonexistant_group_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_state, "i_dont_exist_woo_hoo", "i_dont_exist_woo_hoo")
