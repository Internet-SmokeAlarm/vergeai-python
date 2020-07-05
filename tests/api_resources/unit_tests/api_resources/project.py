import unittest
import vergeai
from vergeai.clients import DummyClient


class UT_ProjectTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Project.create(project_name="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'post'!\"})", str(resp))

    def test_delete_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Project.delete(project_id="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'post'!\"})", str(resp))

    def test_active_jobs_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Project.active_jobs(project_id="test_group")

        self.assertEqual("APIResponse(status_code=200, data={'object_name': \"you called 'get'!\"})", str(resp))
