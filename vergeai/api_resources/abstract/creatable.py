from .. import APIRequestor
from ..utils import convert_to_vergeai_object

class CreateableAPIResource:

    @classmethod
    def create(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        requestor = APIRequestor(
            api_key=api_key,
            api_version=api_version,
            gateway=gateway)
        url = cls.class_url()

        response = requestor.request("post", url, "create", parameters)

        return convert_to_vergeai_object(response, api_key, gateway, api_version)
