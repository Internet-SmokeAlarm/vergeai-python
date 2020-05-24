import unittest

import vergeai
from vergeai.clients import DummyClient

class UT_DeviceTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Device.register(project_id="test_group")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"})]", str(resp))

    def test_get_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Device.get(device_id="1231231231231")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'get'!\"})]", str(resp))

    def test_is_active_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Device.is_active(device_id="12312312312313")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'get'!\"})]", str(resp))
