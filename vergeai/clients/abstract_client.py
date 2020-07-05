from abc import abstractmethod
from .api_response import APIResponse


class AbstractClient:

    @abstractmethod
    def post(self, headers: dict, url: str, data: dict) -> APIResponse:
        raise NotImplementedError("post() not implemented")

    @abstractmethod
    def get(self, headers: dict, url: str) -> APIResponse:
        raise NotImplementedError("get() not implemented")
