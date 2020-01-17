import unittest
import json
from time import sleep

from fedlearn import FedLearnApi
from fedlearn.models import RoundConfiguration
from fedlearn.exceptions import FedLearnApiException

class IT_GetRoundStartModelTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        round_start_model = client.get_round_start_model(group.get_id(), round.get_id())

        self.assertEqual(model_data, round_start_model)

        client.delete_group(group.get_id())

    def test_pass_2(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("0", "RANDOM"))
        round_start_model = client.get_round_start_model(group.get_id(), round.get_id())

        self.assertEqual(model_data, round_start_model)

        client.delete_group(group.get_id())

    def test_pass_3(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        with open("tests/data/mnist_cnn.json", "r") as f:
            group_initial_model_data = json.load(f)

        with open("tests/data/mnist_cnn.json", "r") as f:
            device_update_model_data = json.load(f)

        client.submit_group_initial_model(group_initial_model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        client.submit_model_update(device_update_model_data, group.get_id(), round.get_id(), device.get_id())

        sleep(4)

        round_2 = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))
        round_2_start_model = client.get_round_start_model(group.get_id(), round_2.get_id())

        self.assertEqual(device_update_model_data, round_2_start_model)

        client.delete_group(group.get_id())
