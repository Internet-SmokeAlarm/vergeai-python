import unittest
import json

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_SubmitRoundStartModelTestCase(unittest.TestCase):

    def test_fail_invalid_model_json(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, None, "3123123", "12312313")

    def test_fail_invalid_model_json_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, "232341", "1232432", "1231212")

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, model_data, None, "12312313")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, model_data, 123124, "123123")

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, model_data, "None", 123132)

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_round_start_model, model_data, "123124", None)
