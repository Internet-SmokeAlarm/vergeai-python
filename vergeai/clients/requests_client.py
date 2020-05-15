import requests

from .abstract_client import AbstractClient
from .object_conversion import convert_to_vergeai_object

class RequestsClient(AbstractClient):

    def post(self, headers, url, data={}):
        response = requests.post(url, json=data, headers=headers)

        return convert_to_vergeai_object(response.status_code, response.json())

    def get(self, headers, url):
        response = requests.get(url, headers=headers)

        return convert_to_vergeai_object(response.status_code, response.json())
