import requests
import json
from ...clients import convert_to_vergeai_object

def download_model_from_s3_helper(url_info):
    """
    :param url_info: json
    :return: json
    """
    response = requests.get(url_info["model_url"])

    return convert_to_vergeai_object(response.status_code, response.json())
