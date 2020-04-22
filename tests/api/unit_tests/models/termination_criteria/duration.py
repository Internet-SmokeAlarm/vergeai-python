import unittest

from fedlearn.models.termination_criteria import DurationTerminationCriteria

class DurationTerminationCriteriaTestCase(unittest.TestCase):

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
