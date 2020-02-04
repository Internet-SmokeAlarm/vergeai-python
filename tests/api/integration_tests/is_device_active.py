import unittest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_IsDeviceActiveTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)
        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        device_2 = client.register_device(group.get_id())

        self.assertTrue(client.is_device_active(group.get_id(), round.get_id(), device.get_id()))
        self.assertFalse(client.is_device_active(group.get_id(), round.get_id(), device_2.get_id()))

        client.delete_group(group.get_id())

    def test_pass_2(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)
        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        device_2 = client.register_device(group.get_id())

        self.assertTrue(client.is_device_active(group.get_id(), round.get_id(), device.get_id()))
        self.assertFalse(client.is_device_active(group.get_id(), round.get_id(), device_2.get_id()))

        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round.get_id(), device.get_id())

        sleep(4)

        self.assertFalse(client.is_device_active(group.get_id(), round.get_id(), device.get_id()))

        client.delete_group(group.get_id())
