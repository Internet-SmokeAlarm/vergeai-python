import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetGroupCurrentRoundIdsTestCase(unittest.TestCase):

    def test_fail_invalid_group_ids_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_group_current_round_ids, {})

    def test_fail_invalid_group_ids_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_group_current_round_ids, 12312342)
