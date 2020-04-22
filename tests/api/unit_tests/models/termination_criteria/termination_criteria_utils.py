import unittest

from fedlearn.models.termination_criteria import get_termination_criteria_from_json
from fedlearn.models.termination_criteria import DurationTerminationCriteria

class TerminationCriteriaUtilsTestCase(unittest.TestCase):

    def test_get_termination_criteria_from_json_pass_1(self):
        criteria_json = {
            "type" : "DurationTerminationCriteria",
            "max_duration_sec" : "100"
        }

        criteria = get_termination_criteria_from_json(criteria_json)

        self.assertEqual(criteria.__class__, DurationTerminationCriteria)
        self.assertEqual(criteria.get_max_duration_sec(), 100)

    def test_get_termination_criteria_from_json_fail_1(self):
        criteria_json = {
            "type" : "NonexistantCriteriaClassName",
            "max_duration_sec" : "100"
        }

        self.assertRaises(ValueError, get_termination_criteria_from_json, criteria_json)
