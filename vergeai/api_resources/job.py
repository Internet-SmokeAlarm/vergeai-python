from .endpoint_type import CreatableAPIResource
from .endpoint_type import CancelableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource
from .utils import upload_model_to_s3_helper
from .utils import download_model_from_s3_helper
from .utils import validate_response_ok
from ..logging import log_debug

from time import sleep

class Job(
    AbstractAPIResource,
    CreatableAPIResource,
    CancelableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "job"

    @classmethod
    def submit_start_model(cls,
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
        response = Job._simple_request(cls, "post", "submit_start_model", api_key, api_version, gateway, **parameters)

        if validate_response_ok(response.status_code):
            response = upload_model_to_s3_helper(model, response.data)

        if block:
            while Job._simple_request(cls,
                                        "get",
                                        "get",
                                        api_key,
                                        api_version,
                                        gateway,
                                        **parameters).data["status"] == "INITIALIZED":
                log_debug("Submitted start model...Waiting for DB update to complete...")
                sleep(1)

        return response

    @classmethod
    def get_start_model(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        response = Job._simple_request(cls, "get", "start_model", api_key, api_version, gateway, **parameters)

        if validate_response_ok(response.status_code):
            response = download_model_from_s3_helper(response.data)

        return response

    @classmethod
    def get_aggregate_model(cls,
                            api_key=None,
                            api_version=None,
                            gateway=None,
                            **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        response = Job._simple_request(cls, "get", "aggregate_model", api_key, api_version, gateway, **parameters)

        if validate_response_ok(response.status_code):
            response = download_model_from_s3_helper(response.data)

        return response

    @classmethod
    def wait_for_completion(cls,
                             api_key=None,
                             api_version=None,
                             gateway=None,
                             **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway: string
        """
        while Job._simple_request(cls,
                                    "get",
                                    "get",
                                    api_key,
                                    api_version,
                                    gateway,
                                    **parameters).data["status"] != "COMPLETED":
                log_debug("Job is in progress...Waiting for round to end...")
                sleep(1)
