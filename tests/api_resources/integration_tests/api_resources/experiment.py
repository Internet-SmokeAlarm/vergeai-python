import json
import vergeai
from ..abstract_testcase import AbstractTestCase


class IT_ExperimentTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        response = vergeai.Experiment.create(project_id=project_id)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["ID"], response.data)

        experiments = vergeai.Project.get(project_id=project_id).data["experiments"]

        self.assertEqual(len(experiments), 1)

        vergeai.Project.delete(project_id=project_id)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]
        response = vergeai.Experiment.get(project_id=project_id, experiment_id=experiment_id)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'ID': experiment_id, 'jobs': [], 'hyperparameters': {}, 'current_job': 'NONE', 'start_model': {}, 'current_model': {}, 'is_active': False})

        vergeai.Project.delete(project_id=project_id)

    def test_submit_start_model_fail_already_submitted(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        experiment_id = vergeai.Experiment.create(project_id=project_id).data["ID"]

        device = vergeai.Device.create(project_id=project_id)

        vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        response = vergeai.Experiment.submit_start_model(
            project_id=project_id,
            experiment_id=experiment_id,
            model=model_data,
            block=True)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Project.delete(project_id=project_id)
