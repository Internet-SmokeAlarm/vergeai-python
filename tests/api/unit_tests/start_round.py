import unittest

from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_StartRoundTestCase(unittest.TestCase):

    def test_fail_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, None, "", RoundConfiguration(50, 0, DeviceSelectionStrategy.RANDOM, []))

    def test_fail_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, 12352, "", RoundConfiguration(50, 0, DeviceSelectionStrategy.RANDOM, []))

    def test_fail_invalid_round_config(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, "123123", "", None)

    def test_fail_invalid_round_config_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, "123123", "", 123123)

    def test_fail_invalid_previous_round_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, "None", 1231231, RoundConfiguration(50, 0, DeviceSelectionStrategy.RANDOM, []))

    def test_fail_invalid_previous_round_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.start_round, "12352", None, RoundConfiguration(50, 0, DeviceSelectionStrategy.RANDOM, []))
