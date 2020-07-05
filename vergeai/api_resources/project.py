from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource
from ..clients import APIResponse


class Project(
    AbstractAPIResource,
    CreatableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "project"

    @classmethod
    def active_jobs(cls, api_key: str = None, api_version: str = None, gateway: str = None, **parameters) -> APIResponse:
        return Project._simple_request(cls, "get", "active_jobs", api_key, api_version, gateway, **parameters)
