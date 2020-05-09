import requests

from .abstract_client import AbstractClient

class RequestsClient(AbstractClient):

    def post(self, headers, url, data={}):
        response = requests.post(url, json=data, headers=headers)

        # TODO: Convet response into VergeAIResponse

        return response

    def get(self, headers, url):
        response = requests.get(url, headers=headers)

        # TODO: Convet response into VergeAIResponse

        return response
