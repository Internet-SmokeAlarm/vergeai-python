import unittest

from fedlearn.models import GroupBuilder

class GroupBuilderTestCase(unittest.TestCase):

    def test_validate_parameters_pass(self):
        builder = GroupBuilder()
        builder.set_id("test_ID")
        builder.set_name("test_name")

        builder._validate_parameters()

    def test_validate_parameters_fail(self):
        builder = GroupBuilder()
        builder.set_name("test_name")

        self.assertRaises(ValueError, builder._validate_parameters)

    def test_validate_parameters_fail_2(self):
        builder = GroupBuilder()
        builder.set_id("test_ID")

        self.assertRaises(ValueError, builder._validate_parameters)

    def test_build(self):
        builder = GroupBuilder()
        builder.set_name("test_name")
        builder.set_id("test_id")

        group = builder.build()

        self.assertEqual(group.get_id(), "test_id")
        self.assertEqual(group.get_name(), "test_name")
