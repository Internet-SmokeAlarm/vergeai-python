import json

import vergeai

from ..abstract_testcase import AbstractTestCase

class IT_RoundTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["round_id"], response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_create_pass_hard(self):
        vergeai.api_key = self.api_key

        group = vergeai.Group.create(group_name="sim_test_group")
        group_id = group.data["group_id"]

        for i in range(10):
            vergeai.Device.create(group_id=group_id)

        rounds = [vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=4,
            num_buffer_devices=2,
            termination_criteria=[])]
        for i in range(1, 6):
            rounds.append(vergeai.Round.create(
                group_id=group_id,
                device_selection_strategy="RANDOM",
                previous_round_id=rounds[i - 1].data["round_id"],
                num_devices=4,
                num_buffer_devices=2,
                termination_criteria=[]))

        vergeai.Round.cancel(group_id=group_id, round_id=rounds[0].data["round_id"])

        for i in range(len(rounds)):
            response = vergeai.Round.get(group_id=group_id, round_id=rounds[i].data["round_id"])

            self.assertEqual(response.status_code, 200, response.data)

        response_2 = vergeai.Round.get(group_id=group_id, round_id=rounds[1].data["round_id"])
        self.assertEqual(response_2.data["status"], "IN_PROGRESS", response_2.data)

        vergeai.Group.delete(group_id=group_id)

    def test_create_fail_not_enough_devices(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=10,
            num_buffer_devices=2,
            termination_criteria=[])

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_create_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Round.create(
            group_id="i_dont_exist",
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 403, response.data)

    def test_cancel_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        response = vergeai.Round.cancel(group_id=group_id, round_id=round_id)
        round_data = vergeai.Round.get(group_id=group_id, round_id=round_id).data

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(round_data["status"], "CANCELLED", response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_cancel_fail_complete(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        device = vergeai.Device.create(group_id=group_id)
        device_id = device.data["device_id"]

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.Round.submit_start_model(
            group_id=group_id,
            round_id=round_id,
            model=model_data,
            block=True)

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            group_id=group_id,
            round_id=round_id,
            device_id=device_id,
            model=model_data,
            block=True)

        vergeai.Round.wait_for_aggregation(group_id=group_id, round_id=round_id)

        response = vergeai.Round.cancel(round_id=round_id)
        round_data = vergeai.Round.get(group_id=group_id, round_id=round_id)

        self.assertEqual(response.status_code, 400, response.data)
        self.assertEqual(round_data.data["status"], "COMPLETED", response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_get_aggregate_model_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        device = vergeai.Device.create(group_id=group_id)
        device_id = device.data["device_id"]

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.Round.submit_start_model(
            group_id=group_id,
            round_id=round_id,
            model=model_data,
            block=True)

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            group_id=group_id,
            round_id=round_id,
            device_id=device_id,
            model=model_data,
            block=True)

        vergeai.Round.wait_for_aggregation(group_id=group_id, round_id=round_id)

        response = vergeai.Round.get_aggregate_model(group_id=group_id, round_id=round_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Group.delete(group_id=group_id)

    def test_get_aggregate_model_fail_not_complete(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        device = vergeai.Device.create(group_id=group_id)
        device_id = device.data["device_id"]

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.Round.submit_start_model(
            group_id=group_id,
            round_id=round_id,
            model=model_data,
            block=True)

        response = vergeai.Round.get_aggregate_model(group_id=group_id, round_id=round_id)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_get_aggregate_model_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Round.get_aggregate_model(group_id="i_dont_exist", round_id="i_dont_exist")

        self.assertEqual(response.status_code, 403)

    def test_submit_get_start_model_pass(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        vergeai.Round.submit_start_model(
            group_id=group_id,
            round_id=round_id,
            model=model_data,
            block=True)

        response = vergeai.Round.get_start_model(group_id=group_id, round_id=round_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Group.delete(group_id=group_id)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        response = vergeai.Round.get(group_id=group_id, round_id=round_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(len(response.data["devices"]), 1, response.data)
        self.assertEqual(response.data["configuration"]["device_selection_strategy"], "RANDOM", response.data)
        self.assertEqual(response.data["configuration"]["termination_criteria"], [], response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_get_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Round.get(group_id="i_dont_exist",round_id="i_dont_exist")

        self.assertEqual(response.status_code, 403, response.data)

    def test_submit_start_model_fail_complete(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        device = vergeai.Device.create(group_id=group_id)

        response = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        round_id = response.data["round_id"]

        vergeai.Round.submit_start_model(
            group_id=group_id,
            round_id=round_id,
            model=model_data,
            block=True)

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            group_id=group_id,
            round_id=round_id,
            device_id=device.data["device_id"],
            model=model_data,
            block=True)

        response = vergeai.Round.submit_start_model(
            round_id=round_id,
            model=model_data)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Group.delete(group_id=group_id)
