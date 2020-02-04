import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_CreateGroupTestCase(unittest.TestCase):

    def test_fail_invalid_name(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.create_group, None)

    def test_fail_invalid_name_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.create_group, 123445)
