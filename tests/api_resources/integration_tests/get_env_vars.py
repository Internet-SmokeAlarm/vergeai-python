import os

def load_env_vars():
    return os.environ["CLOUD_GATEWAY_URL"], os.environ["API_KEY"]
