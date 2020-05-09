import unittest

import vergeai
from vergeai.clients import DummyClient

class UT_GroupTestCase(unittest.TestCase):

    def test_create_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Group.create(group_name="test_group")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"}), (json: {'status_code': 200, 'data': {'object_name': \"you called 'post'!\"}})]", str(resp))

    def test_delete_pass(self):
        vergeai.client = DummyClient
        resp = vergeai.Group.delete(group_id="test_group")

        self.assertEqual("[APIResponse (status_code: 200), (data: {'object_name': \"you called 'post'!\"}), (json: {'status_code': 200, 'data': {'object_name': \"you called 'post'!\"}})]", str(resp))
