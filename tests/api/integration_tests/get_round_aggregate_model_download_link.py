import unittest
import json
from time import sleep

from fedlearn import FedLearnApi
from fedlearn.models import RoundConfiguration
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundAggregateModelDownloadLinkTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = client.create_group("sim_test_group")
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        client.submit_model_update(model_data, group.get_id(), learning_round.get_id(), device.get_id())

        # Need to wait for the submit model update to trigger the model_uploaded lambda function
        # And the aggregate models function
        while not client.get_round(group.get_id(), learning_round.get_id()).is_completed():
            sleep(1)
        sleep(1)

        url_data = client.get_round_aggregate_model_download_link(group.get_id(), learning_round.get_id())

        self.assertTrue("model_url" in url_data)

        client.delete_group(group.get_id())

    def test_fail_round_incomplete(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("the_expanse_is_awesome")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round_config = RoundConfiguration("0", "RANDOM")
        round = client.start_round(group.get_id(), round_config)

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, group.get_id(), round.get_id())

        client.delete_group(group.get_id())

    def test_fail_round_nonexistant(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("the_expanse_is_awesome")

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, group.get_id(), "213123")

        client.delete_group(group.get_id())
