import unittest

from fedlearn import FedLearnApi

from fedlearn.exceptions import FedLearnException
from fedlearn.exceptions import FedLearnApiException

class GetModelUpdateSubmitLinkTestCase(unittest.TestCase):

    def test_get_model_update_submit_link_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        learning_round = client.start_round(group.get_id())
        device = client.register_device(group.get_id())

        response = client.get_model_update_submit_link(group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(learning_round.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(device.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())

    def test_get_model_update_submit_link_fail(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, group.get_id(), None, device.get_id())

        client.delete_group(group.get_id())

    def test_get_model_update_submit_link_fail_2(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        learning_round = client.start_round(group.get_id())

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, group.get_id(), learning_round.get_id(), None)

        client.delete_group(group.get_id())

    def test_get_model_update_submit_link_fail_3(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        learning_round = client.start_round(group.get_id())
        device = client.register_device(group.get_id())

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, None, learning_round.get_id(), device.get_id())

        client.delete_group(group.get_id())
