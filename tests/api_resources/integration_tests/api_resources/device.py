import json
import vergeai
from ..abstract_testcase import AbstractTestCase


class IT_DeviceTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]

        response = vergeai.Device.create(project_id=project_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["device_id"], response.data)
        self.assertIsNotNone(response.data["device_api_key"], response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Device.create(project_id="i_dont_exist")

        self.assertEqual(response.status_code, 400, response.data)

    def test_submit_model_pass(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]

        device = vergeai.Device.create(project_id=project_id)

        experiment = vergeai.Experiment.create(project_id=project_id).data

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment["ID"],
            model=model_data,
            block=True)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment["ID"],
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        response = vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            project_id=project_id,
            job_id=job_id,
            device_id=device.data["device_id"],
            model=model_data)

        self.assertEqual(response.status_code, 204, response.data)

        vergeai.Project.delete(project_id=project_id)
