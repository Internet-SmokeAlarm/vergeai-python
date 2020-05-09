from .logging import *
initialize_logger("WARNING")

from .default_gateways import DefaultGateways
from .clients import *

api_key = None
api_version = "v1"
gateway = DefaultGateways.DEV
client = RequestsClient

from .api_resources import *
