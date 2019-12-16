from .api_client import ApiClient

class FedLearnApi:

    def __init__(self, api_key):
        self.api_key = api_key

        self.api_client = ApiClient(api_key)

    def create_group(self, group_name):
        """
        Create a Federated Learning group.

        :param group_name: string. Will be the name of the group
        :returns: A Group
        """
        return self.api_client.create_group(group_name)

    def delete_group(self, group_id):
        """
        Delete a Federated Learning group.

        :param group_id: string. ID of the group to remove
        :returns: Success/Failure Boolean
        """
        return self.api_client.delete_group(group_id)
