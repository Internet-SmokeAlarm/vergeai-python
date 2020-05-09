import vergeai

from .abstract_testcase import AbstractTestCase

class RoundTestCase(AbstractTestCase):

    def test_create_pass(self):
        vergeai.api_key = "TEST_API_KEY"
        vergeai.api_version = "v1"

        ret_round = vergeai.Round.create(
            round_sequence_id="my_name",
            num_devices=10,
            num_buffer_devices=5,
            termination_criteria=[])#[DurationTerminationCriteria(10)])

    def test_list_pass(self):
        return

        """
        vergeai.api_key = "TEST_API_KEY"
        vergeai.api_version = "v1"

        group = vergeai.Group.create(name="sim_test_group")

        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)
        vergeai.Device.create(group_id=group.id)

        ret_round_sequence = vergeai.RoundSequence.create(
            name="temp sequence",
            learning_parameters={},
            metadata={},
            starting_parameters={})

        ret_round_1 = vergeai.Round.create(
            round_sequence_id=ret_round_sequence.id,
            5,
            1,
            DeviceSelectionStrategy.RANDOM,
            [DurationTerminationCriteria(10)])
        ret_round_ = vergeai.Round.create(
            round_sequence_id=ret_round_sequence.id,
            5,
            1,
            [DurationTerminationCriteria(10)])
        ret_round = vergeai.Round.create(
            round_sequence_id=ret_round_sequence.id,
            5,
            1,
            [DurationTerminationCriteria(10)])

        ret_rounds = vergeai.Round.list(round_sequence_id="my_name")
        """
