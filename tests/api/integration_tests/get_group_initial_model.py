import unittest
import json
from time import sleep

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_GetInitialGroupModelTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        retrieved_model_data = client.get_group_initial_model(group.get_id())

        self.assertEqual(model_data.keys(), retrieved_model_data.keys())
        self.assertEqual(model_data, retrieved_model_data)

        client.delete_group(group.get_id())
