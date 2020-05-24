from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource

class Project(
    AbstractAPIResource,
    CreatableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "project"

    @classmethod
    def active_jobs(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return RetrievableAPIResource._simple_request(cls, "get", "active_jobs", api_key, api_version, gateway, **parameters)
