import unittest
import json
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

from .get_env_vars import load_env_vars

class IT_GetRoundStartModelDownloadLinkTestCase(unittest.TestCase):

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

        round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        round_start_model_url = client.get_round_start_model_download_link(group.get_id(), round.get_id())

        self.assertIsNotNone(round_start_model_url)
        self.assertTrue("model_url" in round_start_model_url)

        client.delete_group(group.get_id())
