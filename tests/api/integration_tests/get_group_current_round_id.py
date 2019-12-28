import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException
from fedlearn.models import RoundConfiguration

class IT_GetGroupCurrentRoundIdTestCase(unittest.TestCase):

    def test_pass(self):
        client = FedLearnApi("doesnt_matter")

        group = client.create_group("my_sim_test_group")
        device = client.register_device(group.get_id())
        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        current_round_id = client.get_group_current_round_id(group.get_id())

        self.assertEqual(round.get_id(), current_round_id)

        client.delete_group(group.get_id())

    def test_pass_2(self):
        client = FedLearnApi("doesnt_matter")

        group = client.create_group("my_sim_test_group")
        device = client.register_device(group.get_id())

        current_round_id = client.get_group_current_round_id(group.get_id())

        self.assertEqual("N/A", current_round_id)

        client.delete_group(group.get_id())
