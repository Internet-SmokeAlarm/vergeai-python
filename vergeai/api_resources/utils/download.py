import requests
import json

def download_model_from_s3_helper(url_info):
    """
    :param url_info: json
    :return: json
    """
    return requests.get(url_info["model_url"])
