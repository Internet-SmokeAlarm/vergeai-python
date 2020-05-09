import unittest

from vergeai.api_resources.utils import url_builder

class UT_UrlBuilderTestCase(unittest.TestCase):

    def test_pass(self):
        gateway = "https://api.verge.ai"
        version = "v1"
        url = "group"
        action = "delete"
        parameters = {}

        url = url_builder(gateway, version, url, action, parameters)

        self.assertEqual("https://api.verge.ai/v1/group/delete", url)

    def test_pass_parameters_1(self):
        gateway = "https://api.verge.ai"
        version = "v1"
        url = "group"
        action = "delete"
        parameters = {"group_id" : "123123132"}

        url = url_builder(gateway, version, url, action, parameters)

        self.assertEqual("https://api.verge.ai/v1/group/delete/123123132", url)

    def test_pass_parameters_2(self):
        gateway = "https://api.verge.ai"
        version = "v1"
        url = "group"
        action = "delete"
        parameters = {"group_id" : "123123132", "round_id": "452343553"}

        url = url_builder(gateway, version, url, action, parameters)

        self.assertEqual("https://api.verge.ai/v1/group/delete/123123132/452343553", url)

    def test_pass_parameters(self):
        gateway = "https://api.verge.ai"
        version = "v1"
        url = "group"
        action = "delete"
        parameters = {"group_id" : "123123132", "round_id": "452343553", "device_id" : "24237345735"}

        url = url_builder(gateway, version, url, action, parameters)

        self.assertEqual("https://api.verge.ai/v1/group/delete/123123132/452343553/24237345735", url)
