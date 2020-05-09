from .abstract_client import AbstractClient
from .object_conversion import convert_to_vergeai_object

class DummyClient(AbstractClient):

    def post(self, headers, url, data={}):
        return convert_to_vergeai_object(200, {"object_name" : "you called 'post'!"})

    def get(self, headers, url):
        return convert_to_vergeai_object(200, {"object_name" : "you called 'get'!"})
