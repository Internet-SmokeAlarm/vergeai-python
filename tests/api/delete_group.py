import unittest

from fedlearn import FedLearnApi
from fedlearn.exceptions import FedLearnApiException

class DeleteGroupTestCase(unittest.TestCase):

    def test_delete_group_pass_nonexistant_group(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertTrue(client.delete_group("i_dont_exist_woo_hoo"))

    def test_delete_group_fail_invalid_name(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertRaises(FedLearnApiException, client.delete_group, None)
