import unittest

from fedlearn import FedLearnApi

from fedlearn.exceptions import FedLearnApiException

class UT_GetModelUpdateSubmitLinkTestCase(unittest.TestCase):

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, "!2323434", None, "!232523")

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, "!2323434", 123523, "!232523")

    def test_fail_invalid_device_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, "2335345", "313432", None)

    def test_fail_invalid_device_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, "2335345", "313432", 1231241)

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, None, "123123", "2342131")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_model_update_submit_link, 121231, "123123", "2342131")
