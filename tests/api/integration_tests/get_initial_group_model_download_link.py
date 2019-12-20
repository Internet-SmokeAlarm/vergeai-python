import unittest

from fedlearn import FedLearnApi

class IT_GetInitialGroupModelDownloadLinkTestCase(unittest.TestCase):

    def test_pass(self):
        # TODO : Add test key below
        #   NOTE: Test key should only work on a SANDBOX implementation in the cloud
        client = FedLearnApi("uh_idk_what_to_put_here_yet")
        group = client.create_group("sim_test_group")

        url_json = client.get_initial_group_model_download_link(group.get_id())

        self.assertIsNotNone(url_json)
        self.assertTrue(group.get_id() in url_json["model_url"])

        client.delete_group(group.get_id())
