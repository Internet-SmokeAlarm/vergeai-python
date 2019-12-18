from .api_client import ApiClient

from .exceptions import FedLearnApiException

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

    def auto_submit_model_update(self, model_json, group_id, round_id, device_id):
        """
        Submit device model update. This will both grab the link for submission, as well as
        upload the model to the cloud. Note: Because this must upload a file to the internet,
        it may take a significant amount of time to execute.

        :param model_json: string. Should conform to the model json data standard, must be serializable
        :param group_id: string. ID of group
        :param round_id: string. ID of learning round
        :param device_id: string. ID of device submitting update
        """
        if model_json is None:
            raise FedLearnApiException("model_json must not be none")

        return self.api_client.auto_submit_model_update(model_json, group_id, round_id, device_id)

    def submit_initial_group_model(self, group_id):
        """
        Submit the initial model for a Federated Learning group.

        :param group_id: string. ID of group
        """
        return self.api_client.submit_initial_group_model(group_id)

    def auto_submit_initial_group_model(self, model_json, group_id):
        """
        Submit the initial model for a Federated Learning group.

        :param model_json: string. Should conform to the model json data standard, must be serializable
        :param group_id: string. ID of group
        """
        if model_json is None:
            raise FedLearnApiException("model_json must not be none")

        return self.api_client.auto_submit_initial_group_model(model_json, group_id)

    def create_group(self, group_name):
        """
        Create a Federated Learning group.

        :param group_name: string. Will be the name of the group
        :returns: A Group
        """
        return self.api_client.create_group(group_name)

    def get_round_state(self, group_id, round_id):
        """
        Gets the information associated with a learning round.

        :param group_id: string. Group ID
        :param round_id: string. Learning round ID
        """
        return self.api_client.get_round_state(group_id, round_id)

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
