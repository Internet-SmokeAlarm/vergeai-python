from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource
from ..clients import APIResponse


class APIKey(
    AbstractAPIResource,
    CreatableAPIResource):

    OBJECT_NAME = "auth"
