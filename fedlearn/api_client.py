import requests

from .config import FedLearnEndpointConfig
from .exceptions import FedLearnApiException
from .exceptions import FedLearnException

from .models import GroupBuilder
from .models import Round
from .models import Device
from .models import RoundStatus

from .utils import upload_data_to_s3_helper
from .utils import download_model_from_s3_helper

class ApiClient:
    """
    Will NOT validate parameter data. Please use the FedLearnApi class
    to access the Federated Learning system.
    """

    def __init__(self, api_key):
        """
        :param api_key: string
        """
        self.api_key = api_key

    def register_device(self, group_id):
        """
        :param group_id: string
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnEndpointConfig.REGISTER_DEVICE, data)

        self._validate_response(response)

        device_id = response.json()["device_id"]
        device_api_key = response.json()["device_api_key"]

        return Device(device_id, device_api_key)

    def get_model_update_submit_link(self, group_id, round_id, device_id):
        """
        :param group_id: string
        :param round_id: string
        :param device_id: string
        :return: json. Dictionary that contains information necessary to submit model
        """
        data = {"group_id" : group_id, "round_id" : round_id, "device_id" : device_id}
        response = self._post(FedLearnEndpointConfig.SUBMIT_MODEL_UPDATE, data)

        self._validate_response(response)

        return response.json()

    def submit_model_update(self, model_json, group_id, round_id, device_id):
        """
        :param model_json: json
        :param group_id: string
        :param round_id: string
        :param device_id: string
        """
        upload_link_info = self.get_model_update_submit_link(group_id, round_id, device_id)

        response = upload_data_to_s3_helper(model_json, upload_link_info)

        self._validate_response(response)

        return True

    def get_group_initial_model_submit_link(self, group_id):
        """
        :param group_id: string
        :return: json. Dictionary that contains information necessary to submit model
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnEndpointConfig.SUBMIT_GROUP_INITIAL_MODEL, data)

        self._validate_response(response)

        return response.json()

    def submit_group_initial_model(self, model_json, group_id):
        """
        :param model_json: json
        :param group_id: string
        """
        upload_link_info = self.get_group_initial_model_submit_link(group_id)

        response = upload_data_to_s3_helper(model_json, upload_link_info)

        self._validate_response(response)

        return True

    def get_group_initial_model_download_link(self, group_id):
        """
        :param group_id: string
        """
        data = {"GROUP_ID" : group_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_GROUP_INITIAL_MODEL, data)

        response = self._get(url)

        self._validate_response(response)

        return response.json()

    def get_group_initial_model(self, group_id):
        """
        :param group_id: string
        """
        url_info = self.get_group_initial_model_download_link(group_id)

        response = download_model_from_s3_helper(url_info)

        self._validate_response(response)

        return response.json()

    def get_round(self, group_id, round_id):
        """
        :param group_id: string
        :param round_id: string
        """
        data = {"GROUP_ID" : group_id, "ROUND_ID" : round_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_ROUND, data)
        response = self._get(url)

        self._validate_response(response)

        id = response.json()["ID"]
        status = RoundStatus(response.json()["status"])
        previous_round_id = response.json()["previous_round_id"]

        return Round(id, status, previous_round_id)

    def create_group(self, group_name):
        """
        :param group_name: string
        :return: Group
        """
        data = {"group_name" : group_name}
        response = self._post(FedLearnEndpointConfig.CREATE_GROUP, data)

        self._validate_response(response)

        json_data = response.json()
        builder = GroupBuilder()
        builder.set_id(json_data["group_id"])
        builder.set_name(group_name)

        return builder.build()

    def get_group(self, group_id):
        """
        :param group_id: string
        """
        data = {"GROUP_ID" : group_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_GROUP, data)
        response = self._get(url)

        self._validate_response(response)

        json_data = response.json()
        builder = GroupBuilder()
        builder.set_id(json_data["ID"])
        builder.set_name(json_data["name"])
        builder.set_devices(json_data["devices"])
        builder.set_current_round_id(json_data["current_round_id"])
        builder.set_is_initial_model_set(json_data["is_initial_model_set"])
        builder.set_rounds(json_data["rounds"])

        return builder.build()

    def delete_group(self, group_id):
        """
        :param group_id: string
        :return: boolean
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnEndpointConfig.DELETE_GROUP, data)

        self._validate_response(response)

        return response.json()["success"]

    def start_round(self, group_id, round_configuration):
        """
        :param group_id: string
        :param round_configuration: RoundConfiguration
        :return: Round
        """
        data = {
            "group_id" : group_id,
            "num_devices" : round_configuration.get_num_devices(),
            "device_selection_strategy" : round_configuration.get_device_selection_strategy()
        }
        response = self._post(FedLearnEndpointConfig.START_ROUND, data)

        self._validate_response(response)

        return Round(response.json()["round_id"], RoundStatus.IN_PROGRESS, None)

    def is_device_active(self, group_id, round_id, device_id):
        """
        :param group_id: string
        :param round_id: string
        :param device_id: string
        :return: boolean
        """
        data = {"GROUP_ID" : group_id, "ROUND_ID" : round_id, "DEVICE_ID" : device_id}
        url = self._assemble_url(FedLearnEndpointConfig.IS_DEVICE_ACTIVE, data)
        response = self._get(url)

        self._validate_response(response)

        return response.json()["is_device_active"]

    def get_round_start_model_download_link(self, group_id, round_id):
        """
        :param group_id: string
        :param round_id: string
        """
        data = {"GROUP_ID" : group_id, "ROUND_ID" : round_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_ROUND_START_MODEL, data)
        response = self._get(url)

        self._validate_response(response)

        return response.json()

    def get_round_start_model(self, group_id, round_id):
        """
        :param group_id: string
        :param round_id: string
        """
        url_info = self.get_round_start_model_download_link(group_id, round_id)
        response = download_model_from_s3_helper(url_info)

        self._validate_response(response)

        return response.json()

    def get_group_current_round_id(self, group_id):
        """
        :param group_id: string
        :return: string
        """
        data = {"GROUP_ID" : group_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_CURRENT_ROUND_ID, data)
        response = self._get(url)

        self._validate_response(response)

        return response.json()["round_id"]

    def get_round_aggregate_model_download_link(self, group_id, round_id):
        """
        Get the link to download the round aggregate model.

        :param group_id: string
        :param round_id: string
        :return: dict. Model data
        """
        data = {"GROUP_ID" : group_id, "ROUND_ID" : round_id}
        url = self._assemble_url(FedLearnEndpointConfig.GET_ROUND_AGGREGATE_MODEL, data)
        response = self._get(url)

        self._validate_response(response)

        return response.json()

    def get_round_aggregate_model(self, group_id, round_id):
        """
        Get the link to download the round aggregate model, then download it.

        :param group_id: string
        :param round_id: string
        :return: dict. Model data
        """
        url_info = self.get_round_aggregate_model_download_link(group_id, round_id)

        response = download_model_from_s3_helper(url_info)

        self._validate_response(response)

        return response.json()

    def _post(self, url, json):
        """
        :param url: string
        :param json: json
        """
        return requests.post(url, json=json)

    def _get(self, url):
        """
        :param url: string
        """
        return requests.get(url)

    def _assemble_url(self, base_url, item_pairs):
        """
        :param base_url: string
        :param item_pairs: dict
        """
        for key, val in item_pairs.items():
            base_url = base_url.replace(key, val)

        return base_url

    def _validate_response(self, response):
        if response.status_code == 200 or response.status_code == 204:
            return
        elif response.status_code == 400 or response.status_code == 403:
            raise FedLearnApiException(response.text)
        else:
            raise FedLearnException(response.text)
