import unittest

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class IT_GetGroupInitialModelSubmitLinkTestCase(unittest.TestCase):

    def test_pass(self):
        cloud_gateway_url, api_key = load_env_vars()
        client = FedLearnApi(cloud_gateway_url, api_key)

        group = client.create_group("sim_test_group")

        response = client.get_group_initial_model_submit_link(group.get_id())

        self.assertTrue("model_url" in response)
        self.assertTrue(group.get_id() in response["model_url"]["fields"]["key"])

        client.delete_group(group.get_id())
