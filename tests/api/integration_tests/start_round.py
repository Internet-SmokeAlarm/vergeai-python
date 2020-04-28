from .base import BaseTest
from time import sleep

from fedlearn.models import RoundConfiguration
from fedlearn.models import DeviceSelectionStrategy
from fedlearn.models.termination_criteria import DurationTerminationCriteria
from fedlearn.exceptions import FedLearnApiException

class IT_StartRoundTestCase(BaseTest):

    def test_pass_simple(self):
        group = self.client.create_group("sim_test_group")

        device = self.client.register_device(group.get_id())
        learning_round_id = self.client.start_round(group.get_id(), "", RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))

        self.assertIsNotNone(learning_round_id)

        self.client.delete_group(group.get_id())

    def test_pass_complex(self):
        group = self.client.create_group("sim_test_group")

        device = self.client.register_device(group.get_id())
        learning_round_id = self.client.start_round(group.get_id(),
                                                    "",
                                                    RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, []))
        learning_round_id_2 = self.client.start_round(group.get_id(),
                                                      learning_round_id,
                                                      RoundConfiguration(1, 0, DeviceSelectionStrategy.RANDOM, [
                                                            DurationTerminationCriteria(100),
                                                            DurationTerminationCriteria(250)
                                                      ]))

        self.assertIsNotNone(learning_round_id)
        self.assertIsNotNone(learning_round_id_2)

        self.client.delete_group(group.get_id())
