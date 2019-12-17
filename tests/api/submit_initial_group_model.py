import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class SubmitInitialGroupModelTestCase(unittest.TestCase):

    def test_submit_initial_group_model_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        response = client.submit_initial_group_model(group.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())

    def test_submit_initial_group_model_fail(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertRaises(FedLearnApiException, client.submit_initial_group_model, None)

        client.delete_group(group.get_id())
