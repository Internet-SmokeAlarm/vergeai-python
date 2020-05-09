from .abstract import CreateableAPIResource
from .abstract import AbstractAPIResource

class Group(
    AbstractAPIResource,
    CreateableAPIResource):

    OBJECT_NAME = "group"
