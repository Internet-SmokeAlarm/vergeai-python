import vergeai

from ..abstract_testcase import AbstractTestCase

class IT_GroupTestCase(AbstractTestCase):

    def test_create_delete_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Group.create(group_name="my_name")

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data["group_id"])

        response_2 = vergeai.Group.delete(group_id=response.data["group_id"])

        self.assertEqual(response_2.status_code, 200, response.data)
