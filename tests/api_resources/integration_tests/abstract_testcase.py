import unittest
import vergeai


class AbstractTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # NOTE: This key is for demonstration purpuses and is intentionally left in the source code.
        #   You should NOT use this key in production implementations of the system.
        cls.api_key = "Pr9FDAEvCYY68XDZX5hH-V4DlDXx0oXx5vz0ndtuGUbjnuX4-U1ISNr3a_sgz9wWovd1Ujkks1xgt4JlQQxKIQ"

        vergeai.initialize_logger("DEBUG")
