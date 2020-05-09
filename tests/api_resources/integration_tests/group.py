import vergeai

from .abstract_testcase import AbstractTestCase

class GroupTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = self.api_key

        ret_group = vergeai.Group.create(group_name="my_name")

        print(ret_group)
