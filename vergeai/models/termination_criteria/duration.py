from .termination_criteria import TerminationCriteria

class DurationTerminationCriteria(TerminationCriteria):

    def __init__(self, max_duration_sec):
        """
        :param max_duration_sec: int. Must be > 0
        """
        self.max_duration_sec = max_duration_sec

        self._validate()

    def get_max_duration_sec(self):
        return self.max_duration_sec

    def to_json(self):
        return {
            "type" : DurationTerminationCriteria.__name__,
            "max_duration_sec" : self.max_duration_sec
        }

    def _validate(self):
        if type(self.max_duration_sec) != type(5) or self.max_duration_sec <= 0:
            raise ValueError("max_duration_sec must be of type int and > 0.")

    @staticmethod
    def from_json(json_data):
        return DurationTerminationCriteria(int(json_data["max_duration_sec"]))
