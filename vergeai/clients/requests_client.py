import requests

from .abstract_client import AbstractClient
from .object_conversion import convert_to_vergeai_object
from .api_response import APIResponse


class RequestsClient(AbstractClient):

    def post(self, headers: dict, url: str, data: dict) -> APIResponse:
        response = requests.post(url, json=data, headers=headers)

        return convert_to_vergeai_object(response.status_code, response.json())

    def get(self, headers: dict, url: str) -> APIResponse:
        response = requests.get(url, headers=headers)

        return convert_to_vergeai_object(response.status_code, response.json())
