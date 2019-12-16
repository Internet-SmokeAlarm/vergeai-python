import requests
from .config import FedLearnConfig
from .exceptions import FedLearnApiException

from .models import Group

class ApiClient:

    def __init__(self, api_key):
        """
        :param api_key: string
        """
        self.api_key = api_key

    def create_group(self, group_name):
        """
        :param group_name: string
        """
        data = {"group_name" : group_name}
        response = self._post(FedLearnConfig.CREATE_GROUP_PATH, data)

        response.raise_for_status()

        group_id = response.json()["group_id"]
        group = Group(group_id)

        return group

    def delete_group(self, group_id):
        """
        :param group_id: string
        """
        data = {"group_id" : group_id}
        response = self._post(FedLearnConfig.DELETE_GROUP_PATH, data)

        response.raise_for_status()

        success = response.json()["success"]

        return success

    def _post(self, url, json):
        """
        :param url: string
        :param json: json
        """
        return requests.post(url, json=json)
