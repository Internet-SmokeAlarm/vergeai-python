import unittest

from fedlearn.models import RoundConfiguration
from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class UT_FedLearnApiTestCase(unittest.TestCase):

    def test_validate_string_parameter_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_string_parameter("my parameter!", "param_name")

    def test_validate_string_parameter_invalid_string(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_string_parameter, None, "param_name")

    def test_validate_string_parameter_invalid_string_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_string_parameter, 12351, "param_name")

    def test_validate_string_parameter_invalid_string_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_string_parameter, {}, "param_name")

    def test_validate_group_name_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_group_name("None")

    def test_validate_group_name_fail_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_name, None)

    def test_validate_group_name_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_name, 1234)

    def test_validate_group_name_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_name, {})

    def test_validate_group_id_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_group_id("None")

    def test_validate_group_id_fail_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_id, None)

    def test_validate_group_id_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_id, 1234)

    def test_validate_group_id_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_group_id, {})

    def test_validate_round_id_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_round_id("None")

    def test_validate_round_id_fail_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_id, None)

    def test_validate_round_id_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_id, 1234)

    def test_validate_round_id_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_id, {})

    def test_validate_device_id_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_device_id("None")

    def test_validate_device_id_fail_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_device_id, None)

    def test_validate_device_id_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_device_id, 1234)

    def test_validate_device_id_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_device_id, {})

    def test_validate_model_json_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_model_json({})

    def test_validate_model_json_fail_1(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_model_json, None)

    def test_validate_model_json_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_model_json, 1234)

    def test_validate_model_json_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_model_json, "1231231")

    def test_validate_round_configuration_pass(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        client._validate_round_configuration(RoundConfiguration("50", "RANDOM"))

    def test_validate_round_configuration_fail(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_configuration, RoundConfiguration(None, "RANDOM"))

    def test_validate_round_configuration_fail_2(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_configuration, RoundConfiguration(12131, "RANDOM"))

    def test_validate_round_configuration_fail_3(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_configuration, RoundConfiguration("50", None))

    def test_validate_round_configuration_fail_4(self):
        client = FedLearnApi("gateway_url", "uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client._validate_round_configuration, RoundConfiguration("50", {}))
