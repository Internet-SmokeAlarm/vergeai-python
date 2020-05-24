from .endpoint_type import CreatableAPIResource
from .endpoint_type import DeletableAPIResource
from .endpoint_type import RetrievableAPIResource
from .abstract import AbstractAPIResource

class JobSequence(
    AbstractAPIResource,
    DeletableAPIResource,
    CreatableAPIResource):

    OBJECT_NAME = "job_sequence"
