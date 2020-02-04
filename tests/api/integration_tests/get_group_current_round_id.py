import unittest
import json
from time import sleep

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException
from fedlearn.models import RoundConfiguration

from .get_env_vars import load_env_vars

class IT_GetGroupCurrentRoundIdTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("my_sim_test_group")
        device = client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        current_round_id = client.get_group_current_round_id(group.get_id())

        self.assertEqual(round.get_id(), current_round_id)

        client.delete_group(group.get_id())

    def test_pass_2(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("my_sim_test_group")
        device = client.register_device(group.get_id())

        current_round_id = client.get_group_current_round_id(group.get_id())

        self.assertEqual("N/A", current_round_id)

        client.delete_group(group.get_id())
