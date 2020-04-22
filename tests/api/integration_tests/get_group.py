from .base import BaseTest

from fedlearn.exceptions import FedLearnApiException

class IT_GetGroupTestCase(BaseTest):

    def test_pass(self):
        group = self.client.create_group("sim_test_group")

        returned_group = self.client.get_group(group.get_id())
        self.assertEqual(returned_group.get_id(), group.get_id())

        self.client.delete_group(group.get_id())
