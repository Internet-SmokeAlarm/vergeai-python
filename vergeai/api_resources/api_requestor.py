import vergeai

from .utils import upload_data_to_s3_helper
from .utils import download_model_from_s3_helper
from .utils import url_builder
from .utils import assemble_headers
from .utils import convert_to_vergeai_object

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
        print("API Request Captured")
        print("Method: " + method)
        print("URL: " + url)
        print("Action: " + action)
        print("Params: " + str(parameters))

        if method == "post":
            response = self._request_post(url, action, parameters)
        elif method == "get":
            response = self._request_get(url, action, parameters)

        print("Response: " + str(response))

        return response

    def _request_post(self, url, action, parameters):
        headers = assemble_headers(self.api_key)
        complete_url = url_builder(self.gateway, self.api_version, url, action, {})

        return self.client.post(headers, complete_url, data=parameters)

    def _request_get(self, url, action, parameters):
        headers = assemble_headers(self.api_key)
        complete_url = url_builder(self.gateway, self.api_version, url, action, parameters)

        return self.client.get(headers, complete_url)
