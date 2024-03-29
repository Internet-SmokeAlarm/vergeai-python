from .. import APIRequestor
from ...logging import log_debug

class AbstractType:

    @staticmethod
    def _simple_request(cls, method, action, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param method: string
        :param action: string
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        if api_key is not None:
            log_debug("Using different API key for request: {}".format(api_key))

        requestor = APIRequestor(
            api_key=api_key,
            api_version=api_version,
            gateway=gateway)
        url = cls.class_url()

        return requestor.request(method, url, action, parameters)
