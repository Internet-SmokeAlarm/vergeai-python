import vergeai
import json
from ..abstract_testcase import AbstractTestCase


class IT_ProjectTestCase(AbstractTestCase):

    def test_create_delete_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="my_name", project_description="my description")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["ID"])

        response_2 = vergeai.Project.delete(project_id=response.data["ID"])

        self.assertEqual(response_2.status_code, 200, response.data)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="sim_test_group", project_description="my description")
        project_id = response.data["ID"]

        returned_group = vergeai.Project.get(project_id=project_id)
        self.assertEqual(returned_group.data["ID"], project_id)

        vergeai.Project.delete(project_id=project_id)

    def test_get_active_jobs_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]

        vergeai.Device.create(project_id=project_id)

        experiment = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            experiment_description="test experiment description",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment["ID"],
            model=model_data,
            block=True)

        job_id = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment["ID"],
            num_devices=1,
            num_backup_devices=0,
            num_jobs=1,
            termination_criteria=[]).data[0]["ID"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertEqual(job_id, active_jobs[0]["job_id"])
        self.assertEqual(len(active_jobs), 1)

        vergeai.Project.delete(project_id=project_id)

    def test_get_active_jobs_pass_2(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name", project_description="my description").data["ID"]

        vergeai.Device.create(project_id=project_id)

        experiment = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data
        experiment_2 = vergeai.Experiment.create(
            project_id=project_id,
            experiment_name="test experiment",
            runtime="CUSTOM",
            initialization_strategy="CUSTOMER_PROVIDED",
            data_collection="MINIMAL_RETAIN",
            aggregation_strategy="AVERAGE",
            ml_type="NN",
            code="print(\"Hello world!\")",
            learning_parameters=dict()).data

        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)
        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment["ID"],
            model=model_data,
            block=True)

        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_2["ID"],
            model=model_data,
            block=True)

        job_id = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment["ID"],
            num_devices=1,
            num_backup_devices=0,
            num_jobs=1,
            termination_criteria=[]).data[0]["ID"]

        job_id_2 = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment_2["ID"],
            num_devices=1,
            num_backup_devices=0,
            num_jobs=1,
            termination_criteria=[]).data[0]["ID"]

        job_id_3 = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            experiment_id=experiment["ID"],
            num_devices=1,
            num_backup_devices=0,
            num_jobs=1,
            termination_criteria=[]).data[0]["ID"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertTrue(job_id in [job["job_id"] for job in active_jobs])
        self.assertFalse(job_id_3 in [job["job_id"] for job in active_jobs])
        self.assertTrue(job_id_2 in [job["job_id"] for job in active_jobs])
        self.assertEqual(len(active_jobs), 2)

        vergeai.Project.delete(project_id=project_id)

    def test_get_active_jobs_pass_3(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="sim_test_group", project_description="my description")
        project_id = response.data["ID"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertEqual(len(active_jobs), 0)

        vergeai.Project.delete(project_id=project_id)
