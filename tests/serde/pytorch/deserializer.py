import unittest
import torch

from fedlearn.serde.pytorch import PyTorchSerializer
from fedlearn.serde.pytorch import PyTorchDeserializer
from .dummy_nn import DummyNN

class PyTorchDeserializerTestCase(unittest.TestCase):

    def test_serialize_pass(self):
        state_dict = torch.load("tests/data/dummy_nn_state_dict.pt")
        serialized_state_dict = PyTorchSerializer().serialize(state_dict)

        self.assertTrue(torch.allclose(torch.tensor([0.02175926, -0.00186708, -0.00044867, -0.00553828, -0.0220173, 0.01935874,
  0.01540505, -0.02033835, 0.01145709, -0.01852781]), PyTorchDeserializer().deserialize(serialized_state_dict)["fc.bias"]))
