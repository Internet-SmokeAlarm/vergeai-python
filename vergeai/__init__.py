from .default_gateways import DefaultGateways
from .api_response import APIResponse
from .clients import RequestsClient

api_key = None
api_version = "v1"
gateway = DefaultGateways.DEV
client = RequestsClient

from .api_resources import *
