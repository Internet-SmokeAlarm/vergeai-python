import unittest

from fedlearn import FedLearnApi

class IT_DeleteGroupTestCase(unittest.TestCase):

    def test_pass_nonexistant_group(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")

        self.assertTrue(client.delete_group("i_dont_exist_woo_hoo"))
