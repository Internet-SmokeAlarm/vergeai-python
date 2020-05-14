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
