from .models import RoundConfiguration
from .api_client import ApiClient
from .exceptions import FedLearnApiException

class FedLearnApi:

    def __init__(self, api_key):
        self.api_client = ApiClient(api_key)

    def get_model_update_submit_link(self, group_id, round_id, device_id):
        """
        Get the link to submit a device model update.

        :param group_id: string. ID of group
        :param round_id: string. ID of learning round
        :param device_id: string. ID of device submitting update
        :return: URL JSON
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

    def get_initial_group_model_submit_link(self, group_id):
        """
        Get the link information to submit the initial model for a Federated Learning group.

        :param group_id: string. ID of group
        :return: URL JSON
        """
        self._validate_group_id(group_id)

        return self.api_client.get_initial_group_model_submit_link(group_id)

    def submit_initial_group_model(self, model_json, group_id):
        """
        Submit the initial model for a Federated Learning group.

        :param model_json: json. Should conform to the model json data standard, must be serializable
        :param group_id: string. ID of group
        :return: boolean. True if successful
        """
        self._validate_model_json(model_json)
        self._validate_group_id(group_id)

        if model_json is None:
            raise FedLearnApiException("model_json must not be none")
        elif type(model_json) is not type({}):
            raise FedLearnApiException("model_json must be of type dict")

        return self.api_client.submit_initial_group_model(model_json, group_id)

    def get_initial_group_model_download_link(self, group_id):
        """
        Get the download link for the initial group model.

        :param group_id: string. ID of group
        :return: URL JSON
        """
        self._validate_group_id(group_id)

        return self.api_client.get_initial_group_model_download_link(group_id)

    def get_initial_group_model(self, group_id):
        """
        Run the get_initial_group_model() function, then download the initial model.

        :param group_id: string. ID of group
        :return: json
        """
        self._validate_group_id(group_id)

        return self.api_client.get_initial_group_model(group_id)

    def create_group(self, group_name):
        """
        Create a Federated Learning group.

        :param group_name: string. Will be the name of the group
        :returns: A Group
        """
        self._validate_group_name(group_name)

        return self.api_client.create_group(group_name)

    def get_round_state(self, group_id, round_id):
        """
        Gets the information associated with a learning round.

        :param group_id: string. Group ID
        :param round_id: string. Round ID
        :return: A Round
        """
        self._validate_group_id(group_id)
        self._validate_round_id(round_id)

        return self.api_client.get_round_state(group_id, round_id)

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

    def start_round(self, group_id, round_configuration):
        """
        Start a new learning round. Requires round settings to be passed.

        :param group_id: string. Group ID
        :param round_configuration: RoundConfiguration
        :returns: A Round
        """
        self._validate_group_id(group_id)
        self._validate_round_configuration(round_configuration)

        return self.api_client.start_round(group_id, round_configuration)

    def is_device_active(self, group_id, device_id):
        """
        Check whether a device is currently active. If a device is active, this means
        that it is a part of a round that is active.

        :param group_id: string
        :param device_id: string
        :return: boolean. True if the device is active
        """
        self._validate_group_id(group_id)
        self._validate_device_id(device_id)

        return self.api_client.is_device_active(group_id, device_id)

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
        else:
            self._validate_string_parameter(round_configuration.get_num_devices(), "num devices")
            self._validate_string_parameter(round_configuration.get_device_selection_strategy(), "device selection strategy")

    def _validate_model_json(self, model_json):
        """
        :param model_json: dict
        """
        if model_json is None:
            raise FedLearnApiException("model_json must not be none")
        elif type(model_json) is not type({}):
            raise FedLearnApiException("model_json must be of type dict")
