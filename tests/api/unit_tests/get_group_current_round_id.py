import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetGroupCurrentRoundIdTestCase(unittest.TestCase):

    def test_fail_invalid_group_id_1(self):
        client = FedLearnApi("doesnt_matter")

        self.assertRaises(FedLearnApiException, client.get_group_current_round_id, {})

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("doesnt_matter")

        self.assertRaises(FedLearnApiException, client.get_group_current_round_id, 12312342)
