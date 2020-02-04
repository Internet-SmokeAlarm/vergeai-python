import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_GetRoundAggregateModelDownloadLinkTestCase(unittest.TestCase):

    def test_invalid_group_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, None, "1234124")

    def test_invalid_group_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, {}, "1234124")

    def test_invalid_round_id(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, "1234124", None)

    def test_invalid_round_id_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.get_round_aggregate_model_download_link, "1234124", {})
