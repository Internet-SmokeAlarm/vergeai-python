from abc import abstractmethod

class AbstractDeserializer:

    @abstractmethod
    def deserialize(self, serialized_state_dict):
        """
        :param serialized_state_dict: dict(string : list)
            json returned from AbstractSerializer.serialize()
        """
        raise NotImplementedError("deserialize() not implemented")
