import unittest
import json
from time import sleep
import torch
from torch import tensor

from fedlearn import FedLearnApi
from fedlearn.models import RoundConfiguration

class IT_GetRoundAggregateModel(unittest.TestCase):

    def test_pass_1(self):
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

        aggregate_model = client.get_round_aggregate_model(group.get_id(), learning_round.get_id())

        self.assertEqual(aggregate_model, model_data)

        client.delete_group(group.get_id())

    def test_pass_2(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        with open("tests/data/mnist_cnn_2.json", "r") as f:
            model_data_2 = json.load(f)

        group = client.create_group("sim_test_group")
        client.submit_group_initial_model(model_data, group.get_id())

        while not client.get_group(group.get_id()).is_initial_model_set():
            sleep(1)
        sleep(1)

        device = client.register_device(group.get_id())
        device_2 = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("2", "RANDOM"))
        client.submit_model_update(model_data, group.get_id(), learning_round.get_id(), device.get_id())
        client.submit_model_update(model_data_2, group.get_id(), learning_round.get_id(), device_2.get_id())

        # Need to wait for the submit model update to trigger the model_uploaded lambda function
        # And the aggregate models function
        while not client.get_round(group.get_id(), learning_round.get_id()).is_completed():
            sleep(1)
        sleep(1)

        aggregate_model = client.get_round_aggregate_model(group.get_id(), learning_round.get_id())

        self.assertTrue(
            torch.equal(tensor([-0.105678745, 0.03920024, 0.02667633, -0.05052743, 0.08841841]),
            tensor(aggregate_model["conv1.bias"])))

        client.delete_group(group.get_id())
