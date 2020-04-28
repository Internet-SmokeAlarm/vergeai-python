from .base import BaseTest
from fedlearn.exceptions import FedLearnApiException

class IT_DeleteGroupTestCase(BaseTest):

    def test_fail_nonexistant_group(self):
        self.assertRaises(FedLearnApiException, self.client.delete_group, "i_dont_exist_woo_hoo")
