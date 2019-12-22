import unittest

from fedlearn.models import RoundStatus
from fedlearn.models import Round

class RoundTestCase(unittest.TestCase):

    def test_is_complete_pass(self):
        round = Round("123123", RoundStatus.COMPLETED)

        self.assertTrue(round.is_completed())

    def test_is_complete_pass_2(self):
        round = Round("123123", RoundStatus.CANCELLED)

        self.assertFalse(round.is_completed())
