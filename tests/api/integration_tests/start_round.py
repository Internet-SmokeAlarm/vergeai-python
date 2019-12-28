import unittest

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class IT_StartRoundTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")
        device = client.register_device(group.get_id())

        learning_round = client.start_round(group.get_id(), RoundConfiguration("1", "RANDOM"))

        self.assertIsNotNone(learning_round.get_id())

        client.delete_group(group.get_id())
