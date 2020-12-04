from .endpoint_type import CreatableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource
from ..clients import APIResponse
from .utils import validate_response_ok
from ..logging import log_debug
from time import sleep
from .utils import upload_model_to_s3_helper


class Experiment(
    AbstractAPIResource,
    CreatableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "experiment"

    @classmethod
    def submit_start_model(cls,
                           model: dict = None,
                           api_key: str = None,
                           api_version: str = None,
                           gateway: str = None,
                           block: bool = False,
                           **parameters) -> APIResponse:
        response = Experiment._simple_request(cls, "post", "submit_start_model", api_key, api_version, gateway, **parameters)

        if validate_response_ok(response.status_code):
            response = upload_model_to_s3_helper(model, response.data)

        if block:
            while Experiment._simple_request(cls,
                                             "get",
                                             "get",
                                             api_key,
                                             api_version,
                                             gateway,
                                             **parameters).data["configuration"]["parameters"] == {}:
                log_debug("Submitted start model...Waiting for DB update to complete...")
                sleep(1)

        return response
