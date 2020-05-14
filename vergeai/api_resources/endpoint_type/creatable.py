from .. import APIRequestor
from ..abstract import AbstractType

class CreatableAPIResource(AbstractType):

    @classmethod
    def create(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return CreatableAPIResource._simple_request(cls, "post", "create", api_key, api_version, gateway, **parameters)
