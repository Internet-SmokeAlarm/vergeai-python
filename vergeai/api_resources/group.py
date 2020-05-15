from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource

class Group(
    AbstractAPIResource,
    CreatableAPIResource,
    DeletableAPIResource,
    RetrievableAPIResource):

    OBJECT_NAME = "group"

    @classmethod
    def active_rounds(cls, api_key=None, api_version=None, gateway=None, **parameters):
        """
        :param api_key: string
        :param api_version: string
        :param gateway:string
        """
        return RetrievableAPIResource._simple_request(cls, "get", "current_round_ids", api_key, api_version, gateway, **parameters)
