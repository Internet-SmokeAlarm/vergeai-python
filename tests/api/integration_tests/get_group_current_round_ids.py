from .base import BaseTest
import json
from time import sleep

from fedlearn.exceptions import FedLearnApiException
from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy

class IT_GetGroupCurrentRoundIdsTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("my_sim_test_group")
        device = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))

        current_round_ids = self.client.get_group_current_round_ids(group.get_id())

        self.assertTrue(round_id in current_round_ids)
        self.assertEqual(len(current_round_ids), 1)

        self.client.delete_group(group.get_id())

    def test_pass_2(self):
        group = self.client.create_group("my_sim_test_group")
        device = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round_id_2 = self.client.start_round(group.get_id(), round_id, RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round_id_3 = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))

        current_round_ids = self.client.get_group_current_round_ids(group.get_id())

        self.assertTrue(round_id in current_round_ids)
        self.assertTrue(round_id_3 in current_round_ids)
        self.assertFalse(round_id_2 in current_round_ids)
        self.assertEqual(len(current_round_ids), 2)

        self.client.delete_group(group.get_id())

    def test_pass_3(self):
        group = self.client.create_group("my_sim_test_group")

        current_round_ids = self.client.get_group_current_round_ids(group.get_id())

        self.assertEqual(len(current_round_ids), 0)

        self.client.delete_group(group.get_id())
