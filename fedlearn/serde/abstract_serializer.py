from abc import abstractmethod

class AbstractSerializer:

    @abstractmethod
    def serialize(self, state_dict):
        """
        :param state_dict: dict(string : Tensor)
            nn.Module.state_dict()
        """
        raise NotImplementedError("serialize() not implemented")
