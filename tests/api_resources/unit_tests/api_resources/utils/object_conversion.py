import unittest

from vergeai.api_resources.utils import convert_to_vergeai_object

class UT_ObjectConversionTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO
        converted_obj = convert_to_vergeai_object(None, None, None, None)

        self.assertEqual("TODO", converted_obj)
