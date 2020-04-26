from .base import BaseTest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundStatus
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")

        self.client.register_device(group.get_id())

        learning_round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round = self.client.get_round(group.get_id(), learning_round_id)

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round_id)
        self.assertEqual(RoundStatus.INITIALIZED, round.get_status())

        self.client.delete_group(group.get_id())

    def test_pass_2(self):
        group = self.client.create_group("sim_test_group")

        self.client.register_device(group.get_id())

        learning_round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        learning_round_2_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))

        round = self.client.get_round(group.get_id(), learning_round_2_id)

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round_2_id)
        self.assertEqual(RoundStatus.INITIALIZED, round.get_status())

        self.client.delete_group(group.get_id())

    def test_fail_nonexistant_round_id(self):
        group = self.client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, self.client.get_round, group.get_id(), "i_dont_exist_woo_hoo")

        self.client.delete_group(group.get_id())

    def test_fail_no_devices(self):
        group = self.client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, self.client.start_round, group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
