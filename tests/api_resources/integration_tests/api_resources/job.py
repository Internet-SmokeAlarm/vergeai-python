import json
import vergeai
from ..abstract_testcase import AbstractTestCase


class IT_JobTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        vergeai.Device.create(project_id=project_id)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["ID"], response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_pass_hard(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="sim_test_project").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        for i in range(10):
            vergeai.Device.create(project_id=project_id)

        jobs = []
        for i in range(6):
            jobs.append(vergeai.Job.create(
                project_id=project_id,
                device_selection_strategy="RANDOM",
                experiment_id=experiment_id,
                num_devices=4,
                num_buffer_devices=2,
                termination_criteria=[]))

        vergeai.Job.cancel(project_id=project_id, job_id=jobs[0].data["ID"])

        for i in range(len(jobs)):
            response = vergeai.Job.get(project_id=project_id, job_id=jobs[i].data["ID"])

            self.assertEqual(response.status_code, 200, response.data)

        response_2 = vergeai.Job.get(project_id=project_id, job_id=jobs[1].data["ID"])
        self.assertEqual(response_2.data["status"], "IN_PROGRESS", response_2.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_fail_not_enough_devices(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=10,
            num_buffer_devices=2,
            termination_criteria=[])

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Job.create(
            project_id="i_dont_exist",
            device_selection_strategy="RANDOM",
            experiment_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 400, response.data)

    def test_cancel_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        vergeai.Device.create(project_id=project_id)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        response = vergeai.Job.cancel(project_id=project_id, job_id=job_id)
        job_data = vergeai.Job.get(project_id=project_id, job_id=job_id).data

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(job_data["status"], "CANCELLED", response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_cancel_fail_complete(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        device = vergeai.Device.create(project_id=project_id)
        device_id = device.data["device_id"]

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            project_id=project_id,
            job_id=job_id,
            device_id=device_id,
            model=model_data,
            block=True)

        vergeai.Job.wait_for_completion(project_id=project_id, job_id=job_id)

        response = vergeai.Job.cancel(job_id=job_id)
        job_data = vergeai.Job.get(project_id=project_id, job_id=job_id)

        self.assertEqual(response.status_code, 400, response.data)
        self.assertEqual(job_data.data["status"], "COMPLETED", response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        device = vergeai.Device.create(project_id=project_id)
        device_id = device.data["device_id"]

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            project_id=project_id,
            job_id=job_id,
            device_id=device_id,
            model=model_data,
            block=True)

        vergeai.Job.wait_for_completion(project_id=project_id, job_id=job_id)

        response = vergeai.Job.get_aggregate_model(project_id=project_id, job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_fail_not_complete(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        device = vergeai.Device.create(project_id=project_id)
        device_id = device.data["device_id"]

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        response = vergeai.Job.get_aggregate_model(project_id=project_id, job_id=job_id)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Job.get_aggregate_model(project_id="i_dont_exist", job_id="i_dont_exist")

        self.assertEqual(response.status_code, 400)

    def test_get_start_model_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        vergeai.Device.create(project_id=project_id)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        response = vergeai.Job.get_start_model(project_id=project_id, job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        vergeai.Device.create(project_id=project_id)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["ID"]

        response = vergeai.Job.get(project_id=project_id, job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(len(response.data["devices"]), 1, response.data)
        self.assertEqual(response.data["configuration"]["device_selection_strategy"], "RANDOM", response.data)
        self.assertEqual(response.data["configuration"]["termination_criteria"], [], response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Job.get(project_id="i_dont_exist",job_id="i_dont_exist")

        self.assertEqual(response.status_code, 400, response.data)
