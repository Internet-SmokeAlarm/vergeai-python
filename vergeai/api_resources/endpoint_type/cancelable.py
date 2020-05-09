from .. import APIRequestor
from ..abstract import AbstractType

class CancelableAPIResource(AbstractType):

    @classmethod
    def cancel(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return CancelableAPIResource._simple_request(cls, "cancel", api_key, api_version, gateway, **parameters)
