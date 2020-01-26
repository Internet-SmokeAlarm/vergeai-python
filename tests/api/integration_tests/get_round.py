import unittest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn.models import RoundStatus
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_GetRoundTestCase(unittest.TestCase):

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

        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))

        round = client.get_round(group.get_id(), learning_round.get_id())

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round.get_id())
        self.assertEqual(RoundStatus.IN_PROGRESS, round.get_status())
        self.assertEqual(round.get_previous_round_id(), "N/A")

        client.delete_group(group.get_id())

    def test_pass_2(self):
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
        learning_round_2 = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))

        round = client.get_round(group.get_id(), learning_round_2.get_id())

        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round_2.get_id())
        self.assertEqual(RoundStatus.IN_PROGRESS, round.get_status())
        self.assertEqual(round.get_previous_round_id(), learning_round.get_id())

        client.delete_group(group.get_id())

    def test_fail_nonexistant_round_id(self):
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
        self.assertRaises(FedLearnApiException, client.get_round, group.get_id(), "i_dont_exist_woo_hoo")

        client.delete_group(group.get_id())
