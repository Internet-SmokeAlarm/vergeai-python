from .base import BaseTest
import json
from time import sleep

from fedlearn import FedLearnApi
from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.exceptions import FedLearnApiException

class IT_IsDeviceActiveTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        device_2 = self.client.register_device(group.get_id())
        self.client.register_device(group.get_id())
        self.client.register_device(group.get_id())

        self.assertTrue(self.client.is_device_active(group.get_id(), round_id, device.get_id()))
        self.assertFalse(self.client.is_device_active(group.get_id(), round_id, device_2.get_id()))

        self.client.delete_group(group.get_id())

    def test_pass_2(self):
        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        device_2 = self.client.register_device(group.get_id())
        self.client.register_device(group.get_id())
        self.client.register_device(group.get_id())

        self.assertTrue(self.client.is_device_active(group.get_id(), round_id, device.get_id()))
        self.assertFalse(self.client.is_device_active(group.get_id(), round_id, device_2.get_id()))

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round_id, device.get_id())

        sleep(4)

        self.assertFalse(self.client.is_device_active(group.get_id(), round_id, device.get_id()))

        self.client.delete_group(group.get_id())
