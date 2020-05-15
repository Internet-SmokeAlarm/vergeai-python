import requests
import json
from tempfile import NamedTemporaryFile
from ...clients import convert_to_vergeai_object

def upload_model_to_s3_helper(data, url_info):
    """
    :param data: serializable object
    :param url_info: json
    :return: requests response object
    """
    model_file = NamedTemporaryFile(delete=True)
    try:
        with open(model_file.name, 'w') as f:
            json.dump(data, f)

        with open(model_file.name, 'rb') as f:
            response = requests.post(
                url_info["model_url"]["url"],
                data=url_info["model_url"]["fields"],
                files={"file" : (url_info["model_url"]["fields"]["key"], f)})

        return convert_to_vergeai_object(response.status_code, {})
    finally:
        model_file.close()
