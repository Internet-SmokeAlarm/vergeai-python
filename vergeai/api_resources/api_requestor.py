import requests
import vergeai

from .utils import upload_data_to_s3_helper
from .utils import download_model_from_s3_helper

from .utils import url_builder
from .utils import assemble_headers

class APIRequestor:

    def __init__(self, api_key=None, api_version=None, gateway=None):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        self.gateway = gateway or vergeai.gateway
        self.api_key = api_key or vergeai.api_key
        self.api_version = api_version or vergeai.api_version

        self.client = vergeai.client()

    def request(self, method, url, action, parameters):
        """
        :param method: string
        :param url: string
        :param action: string
        :param parameters: dict
        """
        print("Method: " + method)
        print("URL: " + url)
        print("Action: " + action)
        print("Params: " + str(parameters))

        headers = assemble_headers(self.api_key)

        if method == "post":
            complete_url = url_builder(self.gateway, self.api_version, url, action, {})

            print("Complete URL: " + str(complete_url))

            response = self.client.post(headers, complete_url, data=parameters)
        elif method == "get":
            complete_url = url_builder(self.gateway, self.api_version, url, action, parameters)

            print("Complete URL: " + str(complete_url))

            response = self.client.get(headers, complete_url)

        print("Response: " + str(response))

        return response
