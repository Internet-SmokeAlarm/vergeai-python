from .. import APIRequestor
from ..abstract import AbstractType

class DeletableAPIResource(AbstractType):

    @classmethod
    def delete(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return DeletableAPIResource._simple_request(cls, "delete", api_key, api_version, gateway, **parameters)
