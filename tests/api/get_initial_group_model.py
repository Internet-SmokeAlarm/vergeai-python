import unittest
import json

from fedlearn import FedLearnApi

from fedlearn.exceptions import FedLearnApiException

class GetInitialGroupModelTestCase(unittest.TestCase):

    def test_get_initial_group_model_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        group = client.create_group("sim_test_group")
        client.submit_initial_group_model(model_data, group.get_id())

        retrieved_model_data = client.get_initial_group_model(group.get_id())

        self.assertEqual(model_data.keys(), retrieved_model_data.keys())
        self.assertEqual(model_data, retrieved_model_data)

        client.delete_group(group.get_id())

    def test_get_initial_group_model_fail(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.get_initial_group_model, None)

        client.delete_group(group.get_id())