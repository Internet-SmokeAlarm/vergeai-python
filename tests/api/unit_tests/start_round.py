import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_StartRoundTestCase(unittest.TestCase):

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, None)

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, 12352)
