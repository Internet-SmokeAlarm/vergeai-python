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

    def test_get_pass(self):
        vergeai.api_key = self.api_key

        response = vergeai.Group.create(group_name="sim_test_group")
        group_id = response.data["group_id"]

        returned_group = vergeai.Group.get(group_id=group_id)
        self.assertEqual(returned_group.data["ID"], group_id)

        vergeai.Group.delete(group_id=group_id)

    def test_get_active_rounds_pass(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        round_id = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["round_id"]

        response = vergeai.Group.active_rounds(group_id=group_id)
        active_rounds = response.data["round_ids"]

        self.assertTrue(round_id in active_rounds)
        self.assertEqual(len(active_rounds), 1)

        vergeai.Group.delete(group_id)

    def test_get_active_rounds_pass_2(self):
        vergeai.api_key = self.api_key

        group_id = vergeai.Group.create(group_name="my_name").data["group_id"]

        vergeai.Device.create(group_id=group_id)

        round_id = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["round_id"]

        round_id_2 = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id=round_id,
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["round_id"]

        round_id_3 = vergeai.Round.create(
            group_id=group_id,
            device_selection_strategy="RANDOM",
            previous_round_id="",
            num_devices=1,
            num_buffer_devices=0,
            termination_criteria=[]).data["round_id"]

        response = vergeai.Group.active_rounds(group_id=group_id)
        active_rounds = response.data["round_ids"]

        self.assertTrue(round_id in active_rounds)
        self.assertTrue(round_id_3 in active_rounds)
        self.assertFalse(round_id_2 in active_rounds)
        self.assertEqual(len(active_rounds), 2)

        vergeai.Group.delete(group_id)

    def test_get_active_rounds_pass_3(self):
        vergeai.api_key = self.api_key

        response = vergeai.Group.create(group_name="sim_test_group")
        group_id = response.data["group_id"]

        response = vergeai.Group.active_rounds(group_id=group_id)
        active_rounds = response.data["round_ids"]

        self.assertEqual(len(active_rounds), 0)

        vergeai.Group.delete(group_id=group_id)
