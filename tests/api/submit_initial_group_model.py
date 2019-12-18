import unittest
import json

from fedlearn import FedLearnApi

from fedlearn.exceptions import FedLearnException
from fedlearn.exceptions import FedLearnApiException

class SubmitInitialGroupModelTestCase(unittest.TestCase):

    def test_submit_initial_group_model_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")

        success = client.submit_initial_group_model(model_data, group.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())

    def test_submit_initial_group_model_fail(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, None, group.get_id())

        client.delete_group(group.get_id())

    def test_submit_initial_group_model_fail_3(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, "testing", group.get_id())

        client.delete_group(group.get_id())

    def test_submit_initial_group_model_fail_2(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, model_data, None)

        client.delete_group(group.get_id())
