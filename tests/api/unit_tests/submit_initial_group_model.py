import unittest
import json

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_SubmitInitialGroupModelTestCase(unittest.TestCase):

    def test_fail_invalid_model_json(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, None, "3123123")

    def test_fail_invalid_model_json_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, "232341", "1232432")

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, model_data, None)

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, model_data, 123124)
