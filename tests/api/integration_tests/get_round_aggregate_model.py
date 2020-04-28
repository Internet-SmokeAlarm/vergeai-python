from .base import BaseTest
import json
from time import sleep
import torch
from torch import tensor

from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi

class IT_GetRoundAggregateModel(BaseTest):

    def test_pass_1(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round_id, device.get_id())

        # Need to wait for the submit model update to trigger the model_uploaded lambda function
        # And the aggregate models function
        while not self.client.get_round(group.get_id(), round_id).is_complete():
            sleep(1)

        aggregate_model = self.client.get_round_aggregate_model(group.get_id(), round_id)

        self.assertEqual(aggregate_model, model_data)

        self.client.delete_group(group.get_id())

    def test_pass_2(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        with open("tests/data/mnist_cnn_2.json", "r") as f:
            model_data_2 = json.load(f)

        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())
        device_2 = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(2, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round_id, device.get_id())

        device_client_2 = FedLearnApi(self.cloud_gateway_url, device_2.get_api_key())
        device_client_2.submit_model_update(model_data_2, group.get_id(), round_id, device_2.get_id())

        # Need to wait for the submit model update to trigger the model_uploaded lambda function
        # And the aggregate models function
        while not self.client.get_round(group.get_id(), round_id).is_complete():
            sleep(1)

        aggregate_model = self.client.get_round_aggregate_model(group.get_id(), round_id)

        self.assertTrue(
            torch.equal(tensor([-0.105678745, 0.03920024, 0.02667633, -0.05052743, 0.08841841]),
            tensor(aggregate_model["conv1.bias"])))

        self.client.delete_group(group.get_id())
