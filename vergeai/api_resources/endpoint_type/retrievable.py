from .. import APIRequestor
from ..abstract import AbstractType

class RetrievableAPIResource(AbstractType):

    @classmethod
    def get(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return RetrievableAPIResource._simple_request(cls, "get", "get", api_key, api_version, gateway, **parameters)
