import requests
import json
from ...clients import convert_to_vergeai_object
from ...clients import APIResponse


def download_model_from_s3_helper(url_info: dict) -> APIResponse:
    response = requests.get(url_info["model_url"])

    return convert_to_vergeai_object(response.status_code, response.json())
