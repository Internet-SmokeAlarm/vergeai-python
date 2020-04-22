import unittest

from fedlearn import FedLearnApi

from fedlearn.exceptions import FedLearnApiException

class UT_GetRoundStartModelSubmitLinkTestCase(unittest.TestCase):

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_start_model_submit_link, "!2323434", None)

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_start_model_submit_link, "!2323434", 123523)

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_start_model_submit_link, None, "123123")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_start_model_submit_link, 121231, "123123")
