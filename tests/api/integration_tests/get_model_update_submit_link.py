from .base import BaseTest
import json
from time import sleep

from fedlearn import FedLearnApi
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models import RoundConfiguration

class IT_GetModelUpdateSubmitLinkTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        device = self.client.register_device(group.get_id())
        round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        self.client.submit_round_start_model(model_data, group.get_id(), round_id)

        sleep(4)

        device_client = FedLearnApi(self.cloud_gateway_url, device.get_api_key())
        response = device_client.get_model_update_submit_link(group.get_id(), round_id, device.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(round_id in response["model_url"]["fields"]["key"])
        self.assertTrue(device.get_id() in response["model_url"]["fields"]["key"])

        self.client.delete_group(group.get_id())
