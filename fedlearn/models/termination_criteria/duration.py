from .termination_criteria import TerminationCriteria

class DurationTerminationCriteria(TerminationCriteria):

    def __init__(self, max_duration_sec, start_epoch_time):
        """
        :param max_duration_sec: int
        :param start_epoch_time: float
        """
        self.max_duration_sec = max_duration_sec
        self.start_epoch_time = start_epoch_time

    def get_max_duration_sec(self):
        return self.max_duration_sec

    def get_start_epoch_time(self):
        return self.start_epoch_time

    def to_json(self):
        return {
            "type" : DurationTerminationCriteria.__name__,
            "max_duration_sec" : str(self.max_duration_sec),
            "start_epoch_time" : str(self.start_epoch_time)
        }

    @staticmethod
    def from_json(json_data):
        return DurationTerminationCriteria(int(json_data["max_duration_sec"]),
                                           float(json_data["start_epoch_time"]))
