import json
import vergeai
from ..abstract_testcase import AbstractTestCase


class IT_JobTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data[0]["ID"], response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_pass_hard(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="sim_test_project", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        for i in range(10):
            vergeai.Device.create(project_id=project_id)

        jobs = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=4,
            num_backup_devices=2,
            num_jobs=6,
            termination_criteria=[])

        vergeai.Job.cancel(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=jobs.data[0]["ID"])

        for i in range(len(jobs.data)):
            response = vergeai.Job.get(
                project_id=project_id,
                experiment_id=experiment_id,
                job_id=jobs.data[i]["ID"])

            self.assertEqual(response.status_code, 200, response.data)

        response_2 = vergeai.Job.get(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=jobs.data[1]["ID"])
        self.assertEqual(response_2.data["status"], "IN_PROGRESS", response_2.data)

        vergeai.Project.delete(project_id=project_id)

    def test_create_fail_not_enough_devices(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=2,
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
            num_backup_devices=0,
            termination_criteria=[])

        self.assertEqual(response.status_code, 400, response.data)

    def test_cancel_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        response = vergeai.Job.cancel(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)
        job_data = vergeai.Job.get(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id).data

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(job_data["status"], "CANCELLED", response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_cancel_fail_complete(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        device = vergeai.Device.create(project_id=project_id)
        device_id = device.data["devices"][0][0]

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        vergeai.Device.submit_model(
            api_key=device.data["devices"][0][1],
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id,
            device_id=device_id,
            model=model_data)

        vergeai.Job.wait_for_completion(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        response = vergeai.Job.cancel(job_id=job_id)
        job_data = vergeai.Job.get(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        self.assertEqual(response.status_code, 400, response.data)
        self.assertEqual(job_data.data["status"], "COMPLETED", response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        device = vergeai.Device.create(project_id=project_id)
        device_id = device.data["devices"][0][0]

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_id,
            num_devices=1,
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        vergeai.Device.submit_model(
            api_key=device.data["devices"][0][1],
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id,
            device_id=device_id,
            model=model_data)

        vergeai.Job.wait_for_completion(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        response = vergeai.Job.get_aggregate_model(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_fail_not_complete(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        response = vergeai.Job.get_aggregate_model(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_aggregate_model_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Job.get_aggregate_model(
            project_id="i_dont_exist",
            experiment_id="i dont exist",
            job_id="i_dont_exist")

        self.assertEqual(response.status_code, 400)

    def test_get_start_model_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        response = vergeai.Job.get_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data, model_data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]
        experiment_id = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data["ID"]

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
            num_backup_devices=0,
            termination_criteria=[])
        job_id = response.data[0]["ID"]

        response = vergeai.Job.get(
            project_id=project_id,
            experiment_id=experiment_id,
            job_id=job_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(len(response.data["devices"]), 1, response.data)
        self.assertEqual(response.data["configuration"]["device_selection_strategy"], "RANDOM", response.data)
        self.assertEqual(response.data["configuration"]["termination_criteria"], [], response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_fail_nonexistant(self):
        vergeai.api_key = self.api_key

        response = vergeai.Job.get(
            project_id="i_dont_exist",
            experiment_id="experiment_id",
            job_id="i_dont_exist")

        self.assertEqual(response.status_code, 400, response.data)
