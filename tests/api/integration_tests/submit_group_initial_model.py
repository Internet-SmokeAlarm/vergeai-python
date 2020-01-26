import unittest
import json

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_SubmitGroupInitialModelTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")

        success = client.submit_group_initial_model(model_data, group.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())
