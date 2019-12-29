import unittest
import json

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetGroupInitialModelTestCase(unittest.TestCase):

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_group_initial_model, None)

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_group_initial_model, 1235523)
