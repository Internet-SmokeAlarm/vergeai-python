from .termination_criteria import get_termination_criteria_from_json
from .termination_criteria import TerminationCriteria
from .device_selection_strategy import DeviceSelectionStrategy

from ..exceptions import FedLearnApiException

class RoundConfiguration:

    def __init__(self,
                 num_devices,
                 num_buffer_devices,
                 device_selection_strategy,
                 termination_criteria):
        """
        :param num_devices: int. Number of devices that must submit models for round completion.
        :param num_buffer_devices: int. Number of additional devices to make active in case of failure to submit.
        :param device_selection_strategy: DeviceSelectionStrategy. Device selection strategy when running round.
        :param termination_criteria: list(TerminationCriteria). Details the termination criteria for this round.
        """
        self.num_devices = num_devices
        self.num_buffer_devices = num_buffer_devices
        self.device_selection_strategy = device_selection_strategy
        self.termination_criteria = termination_criteria

        self._validate_parameters()

    def get_num_devices(self):
        """
        :return: int
        """
        return self.num_devices

    def get_num_buffer_devices(self):
        """
        :return: int
        """
        return self.num_buffer_devices

    def get_total_num_devices(self):
        """
        Total number of devices to activate for this learning round.

        :return: int
        """
        return self.num_devices + self.num_buffer_devices

    def get_device_selection_strategy(self):
        """
        :return: string
        """
        return self.device_selection_strategy

    def get_termination_criteria(self):
        """
        :return: list(TerminationCriteria)
        """
        return self.termination_criteria

    def add_termination_criteria(self, termination_criteria):
        """
        :param termination_criteria: TerminationCriteria
        """
        self.termination_criteria.append(termination_criteria)

    def set_termination_criteria(self, termination_criteria):
        """
        :param termination_criteria: list(TerminationCriteria)
        """
        self.termination_criteria = termination_criteria

    def to_json(self):
        return {
            "num_devices" : str(self.num_devices),
            "num_buffer_devices" : str(self.num_buffer_devices),
            "device_selection_strategy" : self.device_selection_strategy.value,
            "termination_criteria" : RoundConfiguration._convert_termination_criteria_to_json(self.termination_criteria)
        }

    def _validate_parameters(self):
        if type(self.num_devices) != type(5) or self.num_devices <= 0:
            raise FedLearnApiException("num_devices must be of type int and be > 0.")

        if type(self.num_buffer_devices) != type(5) or self.num_buffer_devices < 0:
            raise FedLearnApiException("num_buffer_devices must be of type int and be >= 0.")

        if type(self.termination_criteria) != type([]):
            raise FedLearnApiException("termination_criteria must be an empty list or a list(TerminationCriteria).")
        else:
            for criteria in self.termination_criteria:
                if not issubclass(criteria.__class__, TerminationCriteria):
                    raise FedLearnApiException("each termination_criteria element must be of type TerminationCriteria.")

        if type(self.device_selection_strategy) != DeviceSelectionStrategy:
            raise FedLearnApiException("device_selection_strategy must be of type DeviceSelectionStrategy.")

    @staticmethod
    def from_json(json_data):
        """
        :param json_data: dict
        """
        return RoundConfiguration(int(json_data["num_devices"]),
                                  int(json_data["num_buffer_devices"]),
                                  DeviceSelectionStrategy(json_data["device_selection_strategy"]),
                                  RoundConfiguration._load_termination_criteria_from_json(json_data["termination_criteria"]))

    @staticmethod
    def _load_termination_criteria_from_json(termination_criteria):
        """
        :param json_data: list(dict)
        :return: list(TerminationCriteria)
        """
        loaded_criteria = []
        for criteria in termination_criteria:
            loaded_criteria.append(get_termination_criteria_from_json(criteria))

        return loaded_criteria

    @staticmethod
    def _convert_termination_criteria_to_json(termination_criteria):
        """
        :return: list(dict)
        """
        dict_term_criteria = []
        for criteria in termination_criteria:
            dict_term_criteria.append(criteria.to_json())

        return dict_term_criteria
