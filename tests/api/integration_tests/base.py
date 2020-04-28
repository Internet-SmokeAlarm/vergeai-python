import unittest

from fedlearn import FedLearnApi

from .get_env_vars import load_env_vars

class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cloud_gateway_url, cls.api_key = load_env_vars()
        cls.client = FedLearnApi(cls.cloud_gateway_url, cls.api_key)
