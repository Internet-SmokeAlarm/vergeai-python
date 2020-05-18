import json

import vergeai

from ..abstract_testcase import AbstractTestCase

class IT_JobSequenceTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        response = vergeai.JobSequence.create(project_id=project_id, name="My Job Sequence")

        self.assertEqual(response.status_code, 200, response.data)
        self.assertIsNotNone(response.data["id"], response.data)

        job_sequences = vergeai.Project.get(project_id=project_id).data["job_sequences"]

        self.assertEqual(len(job_sequences), 1)

        vergeai.Project.delete(project_id=project_id)

    def test_delete_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        sequence_id = vergeai.JobSequence.create(project_id=project_id, name="Simple Job Sequence").data["id"]
        response = vergeai.JobSequence.delete(project_id=project_id, job_sequence_id=sequence_id)

        job_sequences = vergeai.Project.get(project_id=project_id).data["job_sequences"]

        self.assertEqual(len(job_sequences), 0)

        vergeai.Project.delete(project_id=project_id)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        sequence_id = vergeai.JobSequence.create(project_id=project_id, name="Simple Job Sequence").data["id"]
        response = vergeai.JobSequence.get(project_id=project_id, job_sequence_id=sequence_id)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("id" in response.data)
        self.assertTrue(len(response.data["jobs"]), 0)
        self.assertTrue("status" in response.data["status"])
        self.assertTrue("is_")

        vergeai.Project.delete(project_id=project_id)

    def test_submit_start_model(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        sequence_id = vergeai.JobSequence.create(project_id=project_id, name="Simple Job Sequence").data["id"]
        response = vergeai.JobSequence.get(project_id=project_id, job_sequence_id=sequence_id)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("id" in response.data)
        self.assertTrue(len(response.data["jobs"]), 0)
        # TODO! Add more assert statements

        vergeai.Project.delete(project_id=project_id)

    def test_submit_start_model_fail_complete(self):
        with open("tests/data/mnist_cnn.json", "r") as f:
            model_data = json.load(f)

        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]
        job_sequence_id = vergeai.JobSequence.create(project_id=project_id).data["job_sequence_id"]

        device = vergeai.Device.create(project_id=project_id)

        response = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            job_sequence_id=job_sequence_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[])
        job_id = response.data["job_id"]

        vergeai.JobSequence.submit_start_model(
            project_id=project_id,
            model=model_data,
            block=True)

        vergeai.Device.submit_model(
            api_key=device.data["device_api_key"],
            project_id=project_id,
            job_id=job_id,
            device_id=device.data["device_id"],
            model=model_data,
            block=True)

        response = vergeai.JobSequence.submit_start_model(
            project_id=project_id,
            model=model_data,
            block=True)

        self.assertEqual(response.status_code, 400, response.data)

        vergeai.Project.delete(project_id=project_id)

    def test_get_start_model_pass(self):
        # TODO
        self.assertTrue(False)
