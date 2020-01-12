from ..abstract_serializer import AbstractSerializer

class PyTorchSerializer(AbstractSerializer):

    def serialize(self, state_dict):
        return {key : item.detach().numpy().tolist() for key, item in state_dict.items()}
