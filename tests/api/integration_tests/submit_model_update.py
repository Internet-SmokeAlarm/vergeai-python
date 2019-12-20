import unittest
import json

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_SubmitModelUpdateTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        success = client.submit_model_update(model_data, group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())

    def test_fail_non_existant_group_id(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, "I_dont_exist", "123", "12313")

    def test_fail_round_complete(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        learning_round_2 = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, group.get_id(), learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())

    def test_fail_device_not_in_round(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        device = client.register_device(group.get_id())

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, group.get_id(), learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())
