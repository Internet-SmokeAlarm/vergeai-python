from .termination_criteria import TerminationCriteria

class DurationTerminationCriteria(TerminationCriteria):

    def __init__(self, max_duration_sec):
        """
        :param max_duration_sec: int
        """
        self.max_duration_sec = max_duration_sec

    def get_max_duration_sec(self):
        return self.max_duration_sec

    def to_json(self):
        return {
            "type" : DurationTerminationCriteria.__name__,
            "max_duration_sec" : self.max_duration_sec
        }

    @staticmethod
    def from_json(json_data):
        return DurationTerminationCriteria(int(json_data["max_duration_sec"]))
