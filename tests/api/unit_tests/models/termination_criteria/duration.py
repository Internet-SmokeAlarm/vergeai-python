import unittest

from fedlearn.models.termination_criteria import DurationTerminationCriteria

class DurationTerminationCriteriaTestCase(unittest.TestCase):

    def test_construction_fail_1(self):
        self.assertRaises(ValueError, DurationTerminationCriteria, -1)

    def test_construction_fail_2(self):
        self.assertRaises(ValueError, DurationTerminationCriteria, 0)

    def test_construction_fail_3(self):
        self.assertRaises(ValueError, DurationTerminationCriteria, None)

    def test_construction_fail_4(self):
        self.assertRaises(ValueError, DurationTerminationCriteria, "hello world")

    def test_from_json_pass(self):
        criteria_json = {
            "type" : "DurationTerminationCriteria",
            "max_duration_sec" : 100
        }
        criteria = DurationTerminationCriteria.from_json(criteria_json)

        self.assertEqual(criteria.get_max_duration_sec(), 100)

    def test_to_json_pass(self):
        criteria = DurationTerminationCriteria(100)
        criteria_json = {
            "type" : "DurationTerminationCriteria",
            "max_duration_sec" : 100
        }

        self.assertEqual(criteria.to_json(), criteria_json)
