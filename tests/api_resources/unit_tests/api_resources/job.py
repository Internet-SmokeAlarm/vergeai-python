import unittest

import vergeai
from vergeai.clients import DummyClient

class UT_JobTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Job.create(project_id="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'post'!\"})", str(resp))

    def test_cancel_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Job.cancel(job_id="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'post'!\"})", str(resp))

    def test_get_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Job.get(job_id="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'get'!\"})", str(resp))
