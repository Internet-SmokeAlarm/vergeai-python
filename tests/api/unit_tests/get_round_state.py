import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetRoundStateTestCase(unittest.TestCase):

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_state, None, "3123123")

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_state, 12314, "1231132")

    def test_fail_invalid_round_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_state, "123123121", None)

    def test_fail_invalid_round_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_state, "23123121", 123523)
