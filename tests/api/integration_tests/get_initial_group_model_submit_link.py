import unittest

from fedlearn import FedLearnApi

class IT_GetInitialGroupModelSubmitLinkTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        response = client.get_initial_group_model_submit_link(group.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())