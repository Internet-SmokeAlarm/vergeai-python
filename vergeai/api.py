from .models import RoundConfiguration
from .api_client import ApiClient
from .exceptions import FedLearnApiException

class FedLearnApi:

    def __init__(self, cloud_gateway_url, api_key):
        """
        :param cloud_gateway_url: string. Full URL (including ending backslash) of backing FedLearn infrastructure.
        :param api_key: string. API Key to use for authentication.
        """
        self.api_client = ApiClient(cloud_gateway_url, api_key)

    def get_model_update_submit_link(self, group_id, round_id, device_id):
        """
        Get the link to submit a device model update.

        :param group_id: string. ID of group
        :param round_id: string. ID of learning round
        :param device_id: string. ID of device submitting update
        :return: dict. URL data
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)
        self._validate_device_id(device_id)

        return self.api_client.get_model_update_submit_link(group_id, round_id, device_id)

    def submit_model_update(self, model_json, group_id, round_id, device_id):
        """
        Submit device model update. This will both grab the link for submission, as well as
        upload the model to the cloud. Note: Because this must upload a file to the internet,
        it may take a significant amount of time to execute.

        :param model_json: json. Should conform to the model json data standard, must be serializable
        :param group_id: string. ID of group
        :param round_id: string. ID of learning round
        :param device_id: string. ID of device submitting update
        :return: boolean. True if successful
        """
        self._validate_model_json(model_json)
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)
        self._validate_device_id(device_id)

        return self.api_client.submit_model_update(model_json, group_id, round_id, device_id)

    def get_round_start_model_submit_link(self, group_id, round_id):
        """
        Get the link information to submit the start model for a Federated Learning round.

        :param group_id: string. ID of group
        :param round_id: string. ID of round
        :return: dict. URL data
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_start_model_submit_link(group_id, round_id)

    def submit_round_start_model(self, model_json, group_id, round_id):
        """
        Submit the start model for a Federated Learning round.

        :param model_json: json. Should conform to the model json data standard, must be serializable
        :param group_id: string. ID of group
        :param round_id: string. ID of the round. Note: this round must not have a previous round.
        :return: boolean. True if successful
        """
        self._validate_model_json(model_json)
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)
        self._validate_model_json(model_json)

        return self.api_client.submit_round_start_model(model_json, group_id, round_id)

    def get_round_start_model_download_link(self, group_id, round_id):
        """
        Get the download link for the start model for a round.

        :param group_id: string. Group ID
        :param round_id: string. Round ID
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_start_model_download_link(group_id, round_id)

    def get_round_start_model(self, group_id, round_id):
        """
        Get the download link for the round start model, then download it.

        :param group_id: string. Group ID
        :param round_id: string. Round ID
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_start_model(group_id, round_id)

    def create_group(self, group_name):
        """
        Create a Federated Learning group.

        :param group_name: string. Will be the name of the group
        :returns: A Group
        """
        self._validate_group_name(group_name)

        return self.api_client.create_group(group_name)

    def get_group(self, group_id):
        """
        Get a group.

        :param group_id: string. Group ID
        """
        self._validate_group_id(group_id)

        return self.api_client.get_group(group_id)

    def get_round(self, group_id, round_id):
        """
        Gets a learning round.

        :param group_id: string. Group ID
        :param round_id: string. Round ID
        :return: A Round
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round(group_id, round_id)

    def register_device(self, group_id):
        """
        Register a new device with a Federated Learning group.

        :param group_id: string. ID of group to register new device with
        :return: A Device
        """
        self._validate_group_id(group_id)

        return self.api_client.register_device(group_id)

    def delete_group(self, group_id):
        """
        Delete a Federated Learning group.

        :param group_id: string. ID of the group to remove
        :return: Success/Failure Boolean
        """
        self._validate_group_id(group_id)

        return self.api_client.delete_group(group_id)

    def get_group_current_round_ids(self, group_id):
        """
        Gets the current round IDs associated with a Federated Learning group.

        :param group_id: string. ID of the group
        :return: list(string)
        """
        self._validate_group_id(group_id)

        return self.api_client.get_group_current_round_ids(group_id)

    def start_round(self, group_id, previous_round_id, round_configuration):
        """
        Start a new learning round. Requires round settings to be passed.

        :param group_id: string. Group ID
        :param previous_round_id: string. Previous round ID. Should be None if starting a new path.
        :param round_configuration: RoundConfiguration
        :returns: string. Round ID
        """
        self._validate_group_id(group_id)
        self._validate_string_parameter(previous_round_id, "previous_round_id")
        self._validate_round_configuration(round_configuration)

        return self.api_client.start_round(group_id, previous_round_id, round_configuration)

    def is_device_active(self, group_id, round_id, device_id):
        """
        Check whether a device is currently active. If a device is active, this means
        that it is a part of a round that is active.

        :param group_id: string
        :param round_id: string
        :param device_id: string
        :return: boolean. True if the device is active
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)
        self._validate_device_id(device_id)

        return self.api_client.is_device_active(group_id, round_id, device_id)

    def get_round_aggregate_model_download_link(self, group_id, round_id):
        """
        Get the link to download the round aggregate model.

        :param group_id: string
        :param round_id: string
        :return: dict. Model data
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_aggregate_model_download_link(group_id, round_id)

    def get_round_aggregate_model(self, group_id, round_id):
        """
        Get the link to download the round aggregate model, then download it.

        :param group_id: string
        :param round_id: string
        :return: dict. Model data
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_aggregate_model(group_id, round_id)

    def create_api_key(self):
        """
        Will create an API key for the existing user.

        :return: string. Key plaintext value
        """
        return self.api_client.create_api_key()

    def cancel_round(self, round_id):
        """
        Cancels the specified learning round, regardless of current state.

        :param round_id: string
        :return: boolean
        """
        self._validate_round_id(round_id)

        return self.api_client.cancel_round(round_id)

    def _validate_round_id(self, round_id):
        """
        :param round_id: string
        """
        self._validate_string_parameter(round_id, "round_id")

    def _validate_group_id(self, group_id):
        """
        :param group_id: string
        """
        self._validate_string_parameter(group_id, "group_id")

    def _validate_group_name(self, group_name):
        """
        :param group_name: string
        """
        self._validate_string_parameter(group_name, "group_name")

    def _validate_device_id(self, device_id):
        """
        :param device_id: string
        """
        self._validate_string_parameter(device_id, "device_id")

    def _validate_string_parameter(self, parameter, parameter_name):
        """
        :param parameter: string
        :param parameter_name: string
        """
        if parameter is None or type(parameter) is not type("str"):
            raise FedLearnApiException("{} must not be none, and be type string".format(parameter_name))

    def _validate_round_configuration(self, round_configuration):
        """
        :param round_configuration: RoundConfiguration
        """
        if round_configuration is None or type(round_configuration) is not RoundConfiguration:
            raise FedLearnApiException("round configuration must be type RoundConfiguration")

    def _validate_model_json(self, model_json):
        """
        :param model_json: dict
        """
        if model_json is None:
            raise FedLearnApiException("model_json must not be none")
        elif type(model_json) is not type({}):
            raise FedLearnApiException("model_json must be of type dict")