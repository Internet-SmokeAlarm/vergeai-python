import unittest

import vergeai
from vergeai.clients import DummyClient


class UT_ExperimentTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Experiment.create(project_id="12312312132")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))

    def test_delete_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Experiment.delete(project_id="12312312132", experiment_id="12312312312313")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))

    def test_submit_start_model_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Experiment.create(project_id="12312312132")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))
