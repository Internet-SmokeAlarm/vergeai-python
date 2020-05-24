import unittest

import vergeai
from vergeai.clients import DummyClient

class UT_JobSequenceTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.JobSequence.create(project_id="test_group", name="My Job Sequence!")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))

    def test_delete_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.JobSequence.delete(job_sequence_id="12312312312313")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))

    def test_submit_start_model_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.JobSequence.submit_start_model(weights={}, job_sequence_id="12312312312313")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))
