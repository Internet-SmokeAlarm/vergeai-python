from .abstract import CreateableAPIResource
from .abstract import AbstractAPIResource

class Round(
    AbstractAPIResource,
    CreateableAPIResource):

    OBJECT_NAME = "round"
