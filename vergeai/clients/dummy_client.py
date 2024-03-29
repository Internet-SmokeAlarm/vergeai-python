from .abstract_client import AbstractClient
from .api_response import APIResponse
from .object_conversion import convert_to_vergeai_object


class DummyClient(AbstractClient):

    def post(self, headers: dict, url: str, data: dict) -> APIResponse:
        return convert_to_vergeai_object(200, {"object_name" : "you called 'post'!"})

    def get(self, headers: dict, url: str) -> APIResponse:
        return convert_to_vergeai_object(200, {"object_name" : "you called 'get'!"})
