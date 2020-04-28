from .base import BaseTest
import json
from time import sleep

from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundConfiguration
from fedlearn.exceptions import FedLearnApiException
from fedlearn import FedLearnApi

class IT_GetRoundStartModelTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        round_start_model = self.client.get_round_start_model(group.get_id(), round_id)

        self.assertEqual(model_data, round_start_model)

        self.client.delete_group(group.get_id())

    def test_pass_2(self):
        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            group_initial_model_data = json.load(f)

        with open("tests/data/mnist_cnn.json", "r") as f:
            device_update_model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round_2_id = self.client.start_round(group.get_id(), round_id, RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(group_initial_model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(device_update_model_data, group.get_id(), round_id, device.get_id())

        sleep(4)

        round_2_start_model = self.client.get_round_start_model(group.get_id(), round_2_id)

        self.assertEqual(device_update_model_data, round_2_start_model)

        self.client.delete_group(group.get_id())

    def test_pass_3(self):
        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            group_initial_model_data = json.load(f)

        with open("tests/data/mnist_cnn.json", "r") as f:
            device_update_model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(group_initial_model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(device_update_model_data, group.get_id(), round_id, device.get_id())

        sleep(4)

        round_2_id = self.client.start_round(group.get_id(), round_id, RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        round_2_start_model = self.client.get_round_start_model(group.get_id(), round_2_id)

        self.assertEqual(device_update_model_data, round_2_start_model)

        self.client.delete_group(group.get_id())
