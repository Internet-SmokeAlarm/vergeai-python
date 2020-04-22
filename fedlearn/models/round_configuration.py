from .termination_criteria import get_termination_criteria_from_json

class RoundConfiguration:

    def __init__(self,
                 num_devices,
                 num_buffer_devices,
                 device_selection_strategy,
                 termination_criteria):
        """
        :param num_devices: int. Number of devices that must submit models for round completion.
        :param num_buffer_devices: int. Number of additional devices to make active in case of failure to submit.
        :param device_selection_strategy: string. Device selection strategy. Can be one of:
            - RANDOM
        :param termination_criteria: list(TerminationCriteria). Details the termination criteria for this round.
        """
        self.num_devices = num_devices
        self.num_buffer_devices = num_buffer_devices
        self.device_selection_strategy = device_selection_strategy
        self.termination_criteria = termination_criteria

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
            "device_selection_strategy" : self.device_selection_strategy,
            "termination_criteria" : RoundConfiguration._convert_termination_criteria_to_json(self.termination_criteria)
        }

    @staticmethod
    def from_json(json_data):
        """
        :param json_data: dict
        """
        return RoundConfiguration(int(json_data["num_devices"]),
                                  int(json_data["num_buffer_devices"]),
                                  json_data["device_selection_strategy"],
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
