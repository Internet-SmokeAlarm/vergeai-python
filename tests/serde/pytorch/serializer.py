import unittest
import torch

from fedlearn.serde.pytorch import PyTorchSerializer
from .dummy_nn import DummyNN

class PyTorchSerializerTestCase(unittest.TestCase):

    def test_serialize_pass(self):
        state_dict = torch.load("tests/data/dummy_nn_state_dict.pt")

        self.assertEqual([0.021759260445833206, -0.0018670838326215744, -0.00044866837561130524, -0.005538277328014374, -0.02201729640364647, 0.019358739256858826, 0.015405051410198212, -0.020338349044322968, 0.011457093060016632, -0.018527811393141747], PyTorchSerializer().serialize(state_dict)["fc.bias"])
