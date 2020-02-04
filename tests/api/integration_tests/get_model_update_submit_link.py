import unittest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_GetModelUpdateSubmitLinkTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("sim_test_group")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        device_client = FedLearnApi(cloud_gateway_url, device.get_api_key())
        response = device_client.get_model_update_submit_link(group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(learning_round.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(device.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())
