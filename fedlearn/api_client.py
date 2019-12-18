import requests
from .config import FedLearnConfig
from .exceptions import FedLearnApiException
from .exceptions import FedLearnException

from .models import Group
from .models import Round
from .models import Device

from .utils import upload_data_to_s3_helper

class ApiClient:

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
        response = self._post(FedLearnConfig.REGISTER_DEVICE_PATH, data)

        self._validate_response(response)

        device_id = response.json()["device_id"]
        device_api_key = response.json()["device_api_key"]

        return Device(device_id, device_api_key)

    def submit_model_update(self, group_id, round_id, device_id):
        """
        :param group_id: string
        :param round_id: string
        :param device_id: string
        :return: json. Dictionary that contains information necessary to submit model
        """
        data = {"group_id" : group_id, "round_id" : round_id, "device_id" : device_id}
        response = self._post(FedLearnConfig.SUBMIT_MODEL_UPDATE_PATH, data)

        self._validate_response(response)

        return response.json()

    def auto_submit_model_update(self, model_json, group_id, round_id, device_id):
        """
        :param model_json: json
        :param group_id: string
        :param round_id: string
        :param device_id: string
        """
        upload_link_info = self.submit_model_update(group_id, round_id, device_id)

        response = upload_data_to_s3_helper(model_json, upload_link_info)

        self._validate_response(response)

        return True

    def submit_initial_group_model(self, group_id):
        """
        :param group_id: string
        :return: json. Dictionary that contains information necessary to submit model
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnConfig.SUBMIT_INITIAL_GROUP_MODEL_PATH, data)

        self._validate_response(response)

        return response.json()

    def auto_submit_initial_group_model(self, model_json, group_id):
        """
        :param model_json: json
        :param group_id: string
        """
        upload_link_info = self.submit_initial_group_model(group_id)

        response = upload_data_to_s3_helper(model_json, upload_link_info)

        self._validate_response(response)

        return True

    def get_initial_group_model(self, group_id):
        """
        :param group_id: string
        """
        data = {"group_id" : group_id}
        response = self._get(FedLearnConfig.GET_INITIAL_GROUP_MODEL_PATH, data)

        self._validate_response(response)

        return response.json()

    def get_round_state(self, group_id, round_id):
        """
        :param group_id: string
        :param round_id: string
        """
        data = {"group_id" : group_id, "round_id" : round_id}

        response = self._get(FedLearnConfig.GET_ROUND_STATE_PATH, data)

        self._validate_response(response)

        id = response.json()["round"]["id"]
        models = response.json()["round"]["models"]

        return Round(id, models)

    def create_group(self, group_name):
        """
        :param group_name: string
        :return: Group
        """
        data = {"group_name" : group_name}
        response = self._post(FedLearnConfig.CREATE_GROUP_PATH, data)

        self._validate_response(response)

        return Group(response.json()["group_id"])

    def delete_group(self, group_id):
        """
        :param group_id: string
        :return: boolean
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnConfig.DELETE_GROUP_PATH, data)

        self._validate_response(response)

        return response.json()["success"]

    def start_round(self, group_id):
        """
        :param group_id: string
        :return: Round
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnConfig.START_ROUND_PATH, data)

        self._validate_response(response)

        return Round(response.json()["round_id"], [])

    def _post(self, url, json):
        """
        :param url: string
        :param json: json
        """
        return requests.post(url, json=json)

    def _get(self, url, json):
        """
        :param url: string
        :param json: json
        """
        return requests.get(url, json=json)

    def _validate_response(self, response):
        if response.status_code == 200 or response.status_code == 204:
            return
        elif response.status_code == 400:
            raise FedLearnApiException(response.text)
        else:
            raise FedLearnException(response.text)
