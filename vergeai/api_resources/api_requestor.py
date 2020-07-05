import vergeai
from .utils import url_builder
from .utils import assemble_headers
from ..logging import log_info
from ..logging import log_debug
from ..logging import log_error
from ..clients import APIResponse
from .utils import validate_response_ok


class APIRequestor:

    def __init__(self, api_key: str = None, api_version: str = None, gateway: str = None):
        self.gateway = gateway or vergeai.gateway
        self.api_key = api_key or vergeai.api_key
        self.api_version = api_version or vergeai.api_version

        self.client = vergeai.client()

    def request(self, method: str, url: str, action: str, parameters: dict) -> APIResponse:
        log_info("API Request Captured")
        log_debug("Method: {}".format(method))
        log_debug("URL: {}".format(url))
        log_debug("Action: {}".format(action))
        log_debug("Params: {}".format(str(parameters)))

        # TODO: user an Enum here maybe?
        if method == "post":
            response = self._request_post(url, action, parameters)
        elif method == "get":
            response = self._request_get(url, action, parameters)

        log_debug("Response: {}".format(str(response)))
        if not validate_response_ok(response.status_code):
            log_error("Response was not OK")

        return response

    def _request_post(self, url: str, action: str, parameters: str) -> APIResponse:
        headers = assemble_headers(self.api_key)
        complete_url = url_builder(self.gateway, self.api_version, url, action, {})

        log_debug("Assembled URL: {}".format(complete_url))

        return self.client.post(headers, complete_url, data=parameters)

    def _request_get(self, url: str, action: str, parameters: str) -> APIResponse:
        headers = assemble_headers(self.api_key)
        complete_url = url_builder(self.gateway, self.api_version, url, action, parameters)

        log_debug("Assembled URL: {}".format(complete_url))

        return self.client.get(headers, complete_url)
