from .api_client import ApiClient

class FedLearnApi:

    def __init__(self, api_key):
        self.api_key = api_key

        self.api_client = ApiClient(api_key)

    def submit_model_update(self, group_id, round_id, device_id):
        """
        Submit device model update.

        :param group_id: string. ID of group
        :param round_id: string. ID of learning round
        :param device_id: string. ID of device submitting update
        """
        return self.api_client.submit_model_update(group_id, round_id, device_id)

    def submit_initial_group_model(self, group_id):
        """
        Submit the initial model for a Federated Learning group.

        :param group_id: string. ID of group
        """
        return self.api_client.submit_initial_group_model(group_id)

    def create_group(self, group_name):
        """
        Create a Federated Learning group.

        :param group_name: string. Will be the name of the group
        :returns: A Group
        """
        return self.api_client.create_group(group_name)

    def register_device(self, group_id):
        """
        Register a new device with a Federated Learning group.

        :param group_id: string. ID of group to register new device with
        :return: A Device
        """
        return self.api_client.register_device(group_id)

    def delete_group(self, group_id):
        """
        Delete a Federated Learning group.

        :param group_id: string. ID of the group to remove
        :return: Success/Failure Boolean
        """
        return self.api_client.delete_group(group_id)

    def start_round(self, group_id):
        """
        Start a new learning round.

        :param group_id: string. Group ID
        :returns: A LearningRound
        """
        return self.api_client.start_round(group_id)
