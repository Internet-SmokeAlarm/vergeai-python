import json
from time import sleep

from .base import BaseTest
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException
from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundStatus

class IT_CancelRoundTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        self.client.register_device(group.get_id())

        learning_round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        success = self.client.cancel_round(learning_round_id)
        round = self.client.get_round(group.get_id(), learning_round_id)

        self.assertTrue(success)
        self.assertIsNotNone(round)
        self.assertEqual(round.get_id(), learning_round_id)
        self.assertEqual(RoundStatus.CANCELLED, round.get_status())

        self.client.delete_group(group.get_id())

    def test_fail_round_complete(self):
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

        self.assertRaises(FedLearnApiException, self.client.cancel_round, round_id)

        self.client.delete_group(group.get_id())
