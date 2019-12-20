import unittest
import json

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi

class IT_SubmitModelUpdateTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))

        success = client.submit_model_update(model_data, group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue(success)

        client.delete_group(group.get_id())
