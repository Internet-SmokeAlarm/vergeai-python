import unittest

from fedlearn.models import Group
from fedlearn.models import GroupBuilder

class GroupTestCase(unittest.TestCase):

    def test_from_json_pass(self):
        builder = GroupBuilder()
        builder.set_id("test_id")
        builder.set_name("test_name")
        group = builder.build()

        group_json = group.to_json()

        group2 = Group.from_json(group_json)

        self.assertEqual(group2.get_id(), group_json["ID"])
        self.assertEqual(group2.get_name(), group_json["name"])

    def test_to_json_pass(self):
        builder = GroupBuilder()
        builder.set_id("test_id")
        builder.set_name("test_name")
        group = builder.build()

        group_json = group.to_json()

        self.assertEqual("test_id", group_json["ID"])
        self.assertEqual("test_name", group_json["name"])
