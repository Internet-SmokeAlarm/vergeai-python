import unittest

from fedlearn.models import RoundConfiguration
from fedlearn.models.termination_criteria import DurationTerminationCriteria

class RoundConfigurationTestCase(unittest.TestCase):

    def test_to_json_pass(self):
        config = RoundConfiguration(5, 0, "RANDOM", [DurationTerminationCriteria(100, 1231231.2342)])

        json_data = {
            'num_devices': '5',
            'num_buffer_devices': '0',
            'device_selection_strategy': 'RANDOM',
            'termination_criteria': [
                {
                    'max_duration_sec': '100',
                    'start_epoch_time': '1231231.2342',
                    'type': 'DurationTerminationCriteria'
                }
            ]
        }

        self.assertEqual(config.to_json(), json_data)

    def test_from_json_pass(self):
        json_data = {
            'num_devices': '5',
            'num_buffer_devices': '0',
            'device_selection_strategy': 'RANDOM',
            'termination_criteria': [
                {
                    'max_duration_sec': '100',
                    'start_epoch_time': '1231231.2342',
                    'type': 'DurationTerminationCriteria'
                }
            ]
        }

        config = RoundConfiguration.from_json(json_data)

        self.assertEqual(config.get_num_devices(), 5)
        self.assertEqual(config.get_num_buffer_devices(), 0)
        self.assertEqual(config.get_termination_criteria()[0].get_max_duration_sec(), 100)
        self.assertEqual(config.get_termination_criteria()[0].get_start_epoch_time(), 1231231.2342)
        self.assertEqual(len(config.get_termination_criteria()), 1)

    def test_convert_termination_criteria_to_json_pass(self):
        termination_criteria = [
            DurationTerminationCriteria(10, 1231231.123),
            DurationTerminationCriteria(54, 34532323.23)
        ]

        converted_json = RoundConfiguration._convert_termination_criteria_to_json(termination_criteria)

        correct_json_1 = {
            "max_duration_sec" : '10',
            "start_epoch_time" : '1231231.123',
            "type" : "DurationTerminationCriteria"
        }
        correct_json_2 = {
            "max_duration_sec" : '54',
            "start_epoch_time" : '34532323.23',
            "type" : "DurationTerminationCriteria"
        }

        self.assertEqual(len(converted_json), 2)
        self.assertEqual(converted_json[0], correct_json_1)
        self.assertEqual(converted_json[1], correct_json_2)

    def test_load_termination_criteria_from_json_pass(self):
        termination_criteria_json = [
            {
                'max_duration_sec': '123',
                'start_epoch_time': '1231231.23342',
                'type': 'DurationTerminationCriteria'
            }
        ]

        converted_criteria = RoundConfiguration._load_termination_criteria_from_json(termination_criteria_json)

        self.assertEqual(len(converted_criteria), 1)
        self.assertEqual(converted_criteria[0].get_max_duration_sec(), 123)
        self.assertEqual(converted_criteria[0].get_start_epoch_time(), 1231231.23342)
