import unittest

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi

class IT_GetModelUpdateSubmitLinkTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())
        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        response = client.get_model_update_submit_link(group.get_id(), learning_round.get_id(), device.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(learning_round.get_id() in response["model_url"]["fields"]["key"])
        self.assertTrue(device.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())
