from .endpoint_type import CreatableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource
from .utils import validate_response_ok
from .utils import upload_model_to_s3_helper
from ..logging import log_debug

from time import sleep

class Device(
    AbstractAPIResource,
    CreatableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "device"

    @classmethod
    def submit_model(cls,
                     model=None,
                     api_key=None,
                     api_version=None,
                     gateway=None,
                     block=False,
                     **parameters):
        """
        :param model: dict
        :param api_key: string
        :param api_version: string
        :param gateway: string
        :param block: boolean
        """
        response = Device._simple_request(cls, "post", "submit_model_update", api_key, api_version, gateway, **parameters)

        if validate_response_ok(response.status_code):
            response = upload_model_to_s3_helper(model, response.data)

        if block:
            while not Device.is_active(api_key=api_key,
                                       api_version=api_version,
                                       gateway=gateway,
                                       **parameters).data["is_device_active"]:
                log_debug("Submitted device model...Waiting for DB update to complete...")
                sleep(1)

        return response

    @classmethod
    def is_active(cls,
                  api_key=None,
                  api_version=None,
                  gateway=None,
                  **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        return Device._simple_request(cls, "get", "is_active", api_key, api_version, gateway, **parameters)

    @classmethod
    def register(cls,
                 api_key=None,
                 api_version=None,
                 gateway=None,
                 **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        return Device._simple_request(cls, "post", "register", api_key, api_version, gateway, **parameters)
