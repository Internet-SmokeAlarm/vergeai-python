from ...api_response import APIResponse

def convert_to_vergeai_object(status_code, json_data):
    return APIResponse(status_code, json_data)
