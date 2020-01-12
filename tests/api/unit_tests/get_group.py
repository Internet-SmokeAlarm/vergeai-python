import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetGroupTestCase(unittest.TestCase):

    def test_invalid_group_id_1(self):
        client = FedLearnApi("DOES NOT MATTER")

        self.assertRaises(FedLearnApiException, client.get_group, 12344)

    def test_invalid_group_id_2(self):
        client = FedLearnApi("DOES NOT MATTER")

        self.assertRaises(FedLearnApiException, client.get_group, {})
