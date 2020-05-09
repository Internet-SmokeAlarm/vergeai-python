import unittest

from vergeai.api_resources.utils import convert_to_vergeai_object

class UT_ObjectConversionTestCase(unittest.TestCase):

    def test_pass(self):
        converted_obj = convert_to_vergeai_object(200, {"object_name" : "woo hoo"})

        self.assertEqual(converted_obj.status_code, 200)
        self.assertEqual(converted_obj.data, {"object_name" : "woo hoo"})
        self.assertEqual(converted_obj.json, {
            "status_code" : 200,
            "data" : {"object_name" : "woo hoo"}
        })
