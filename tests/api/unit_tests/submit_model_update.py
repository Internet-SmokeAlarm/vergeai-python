import unittest
import json

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_SubmitModelUpdateTestCase(unittest.TestCase):

    def test_fail_invalid_model_json(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, None, "1234", "1234", "1234")

    def test_fail_invalid_model_json_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, "1234", "1234", "1234", "1234")

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, 11234, "1234", "1234")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, None, "1234", "1234")

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, "11234", None, "1234")

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, "11234", 1234, "1234")

    def test_fail_invalid_device_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, "11234", "1234", 1234)

    def test_fail_invalid_device_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.submit_model_update, {}, "11234", "1234", None)
