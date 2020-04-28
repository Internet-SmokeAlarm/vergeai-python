from .base import BaseTest
import json
from time import sleep

from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundConfiguration
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundStartModelDownloadLinkTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        round_start_model_url = self.client.get_round_start_model_download_link(group.get_id(), round_id)

        self.assertIsNotNone(round_start_model_url)
        self.assertTrue("model_url" in round_start_model_url)

        self.client.delete_group(group.get_id())
