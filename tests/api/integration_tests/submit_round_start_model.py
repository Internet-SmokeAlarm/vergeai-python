from .base import BaseTest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn.models.termination_criteria import DurationTerminationCriteria
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.exceptions import FedLearnApiException
from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_SubmitRoundStartModelTestCase(BaseTest):

    def test_pass(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        success = self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        self.assertTrue(success)

        self.client.delete_group(group.get_id())

    def test_fail_round_complete(self):
        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round_id, device.get_id())

        sleep(4)

        self.assertRaises(FedLearnApiException, self.client.submit_round_start_model, model_data, group.get_id(), round_id)

        self.client.delete_group(group.get_id())
