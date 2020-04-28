from .base import BaseTest
import json
from time import sleep

from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundConfiguration
from fedlearn.exceptions import FedLearnApiException
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnException

class IT_GetRoundAggregateModelDownloadLinkTestCase(BaseTest):

    def test_pass(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        group = self.client.create_group("sim_test_group")
        device = self.client.register_device(group.get_id())

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        device_client.submit_model_update(model_data, group.get_id(), round_id, device.get_id())

        # Need to wait for the submit model update to trigger the model_uploaded lambda function
        # And the aggregate models function
        while not self.client.get_round(group.get_id(), round_id).is_complete():
            sleep(1)

        url_data = self.client.get_round_aggregate_model_download_link(group.get_id(), round_id)

        self.assertTrue("model_url" in url_data)
        self.assertTrue(round_id in url_data["model_url"])
        self.assertTrue("aggregate_model" in url_data["model_url"])

        self.client.delete_group(group.get_id())

    def test_fail_round_incomplete(self):
        group = self.client.create_group("the_expanse_is_awesome")
        device = self.client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        self.assertRaises(FedLearnApiException, self.client.get_round_aggregate_model_download_link, group.get_id(), round_id)

        self.client.delete_group(group.get_id())

    def test_fail_round_nonexistant(self):
        group = self.client.create_group("the_expanse_is_awesome")

        self.assertRaises(FedLearnApiException, self.client.get_round_aggregate_model_download_link, group.get_id(), "213123")

        self.client.delete_group(group.get_id())
