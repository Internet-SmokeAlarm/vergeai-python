from .base import BaseTest

class IT_CreateGroupTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")
        self.assertIsNotNone(group.get_id())
        self.client.delete_group(group.get_id())
