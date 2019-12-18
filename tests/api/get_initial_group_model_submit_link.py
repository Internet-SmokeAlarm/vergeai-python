import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class GetInitialGroupModelSubmitLinkTestCase(unittest.TestCase):

    def test_get_initial_group_model_submit_link_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        response = client.get_initial_group_model_submit_link(group.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())

    def test_get_initial_group_model_submit_link_fail(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.get_initial_group_model_submit_link, None)

        client.delete_group(group.get_id())
