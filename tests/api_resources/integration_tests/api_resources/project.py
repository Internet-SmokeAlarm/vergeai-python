import vergeai

from ..abstract_testcase import AbstractTestCase

class IT_ProjectTestCase(AbstractTestCase):

    def test_create_delete_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="my_name")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["project_id"])

        response_2 = vergeai.Project.delete(project_id=response.data["project_id"])

        self.assertEqual(response_2.status_code, 200, response.data)

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="sim_test_group")
        project_id = response.data["project_id"]

        returned_group = vergeai.Project.get(project_id=project_id)
        self.assertEqual(returned_group.data["ID"], project_id)

        vergeai.Project.delete(project_id=project_id)

    def test_get_active_jobs_pass(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]

        vergeai.Device.create(project_id=project_id)

        job_id = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            job_sequence_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["job_id"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertTrue(job_id in active_jobs)
        self.assertEqual(len(active_jobs), 1)

        vergeai.Project.delete(project_id)

    def test_get_active_jobs_pass_2(self):
        vergeai.api_key = self.api_key

        project_id = vergeai.Project.create(project_name="my_name").data["project_id"]

        vergeai.Device.create(project_id=project_id)

        job_id = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            job_sequence_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["job_id"]

        job_id_2 = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            job_sequence_id=job_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["job_id"]

        job_id_3 = vergeai.Job.create(
            project_id=project_id,
            device_selection_strategy="RANDOM",
            job_sequence_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["job_id"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertTrue(job_id in active_jobs)
        self.assertTrue(job_id_3 in active_jobs)
        self.assertFalse(job_id_2 in active_jobs)
        self.assertEqual(len(active_jobs), 2)

        vergeai.Project.delete(project_id)

    def test_get_active_jobs_pass_3(self):
        vergeai.api_key = self.api_key

        response = vergeai.Project.create(project_name="sim_test_group")
        project_id = response.data["project_id"]

        response = vergeai.Project.active_jobs(project_id=project_id)
        active_jobs = response.data["job_ids"]

        self.assertEqual(len(active_jobs), 0)

        vergeai.Project.delete(project_id=project_id)
