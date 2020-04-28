from .base import BaseTest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundStartModelSubmitLinkTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round_start_model_url = self.client.get_round_start_model_submit_link(group.get_id(), round_id)

        self.assertIsNotNone(round_start_model_url)
        self.assertTrue("model_url" in round_start_model_url)

        self.client.delete_group(group.get_id())
