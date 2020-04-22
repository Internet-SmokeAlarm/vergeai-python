from abc import abstractmethod

class TerminationCriteria:

    @abstractmethod
    def to_json(self):
        raise NotImplementedError("to_json() not implemented")
