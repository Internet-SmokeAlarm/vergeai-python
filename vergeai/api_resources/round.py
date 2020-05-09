from .endpoint_type import CreatableAPIResource
from .endpoint_type import CancelableAPIResource
from .abstract import AbstractAPIResource

class Round(
    AbstractAPIResource,
    CreatableAPIResource,
    CancelableAPIResource):

    OBJECT_NAME = "round"
