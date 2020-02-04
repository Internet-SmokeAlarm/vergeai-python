import unittest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_SubmitModelUpdateTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        success = device_client.submit_model_update(model_data, group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())

    def test_fail_round_complete_pass_1(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        device_2 = client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        learning_round = client.start_round(group.get_id(), RoundConfiguration("2", "RANDOM"))

        learning_round_2 = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        self.assertRaises(FedLearnApiException, device_client.submit_model_update, {}, group.get_id(), learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())

    def test_fail_round_complete_pass_2(self):
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

        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        learning_round_2 = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        self.assertRaises(FedLearnApiException, device_client.submit_model_update, {}, group.get_id(), learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())

    def test_fail_device_not_in_round(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("sim_test_group")
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        device = client.register_device(group.get_id())

        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        self.assertRaises(FedLearnApiException, device_client.submit_model_update, {}, group.get_id(), learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())
