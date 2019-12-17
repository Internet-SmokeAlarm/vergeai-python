import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class GroupManagementTestCase(unittest.TestCase):

    def test_create_delete_use_case_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")

        self.assertIsNotNone(group.get_id())

        result = client.delete_group(group.get_id())

        self.assertTrue(result)

    def test_create_group_fail_invalid_name(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.create_group, None)

    def test_delete_group_pass_nonexistant_group(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertTrue(client.delete_group("i_dont_exist_woo_hoo"))

    def test_delete_group_fail_invalid_name(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.delete_group, None)

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
