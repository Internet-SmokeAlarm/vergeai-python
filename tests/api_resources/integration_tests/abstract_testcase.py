import unittest

from .get_env_vars import load_env_vars

class AbstractTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cloud_gateway_url, cls.api_key = load_env_vars()
