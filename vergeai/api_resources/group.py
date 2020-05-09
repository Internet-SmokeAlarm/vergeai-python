from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .abstract import AbstractAPIResource

class Group(
    AbstractAPIResource,
    CreatableAPIResource,
    DeletableAPIResource):

    OBJECT_NAME = "group"
