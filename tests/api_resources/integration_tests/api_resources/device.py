import json
import vergeai

from ..abstract_testcase import AbstractTestCase

class IT_DeviceTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        response = vergeai.Device.create(group_id=group_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["device_id"], response.data)
        self.assertIsNotNone(response.data["device_api_key"], response.data)

        vergeai.Group.delete(group_id=group_id)

    def test_create_fail_nonexistant(self):
        self.assertTrue(False)
        vergeai.api_key = self.api_key

        response = vergeai.Device.create(group_id="i_dont_exist")

        self.assertEqual(response.status_code, 200, response.data)

    def test_submit_model_pass(self):
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
            round_id=round_id,
            model=model_data)

        response = vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            group_id=group_id,
            round_id=round_id,
            device_id=device.data["device_id"],
            model=model_data)

        self.assertEqual(response.status_code, 200, response.data)

        vergeai.Group.delete(group_id=group_id)
