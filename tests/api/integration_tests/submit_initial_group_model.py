import unittest
import json

from fedlearn import FedLearnApi

class IT_SubmitInitialGroupModelTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")

        success = client.submit_initial_group_model(model_data, group.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())
