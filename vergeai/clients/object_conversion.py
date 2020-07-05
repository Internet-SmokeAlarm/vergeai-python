from .api_response import APIResponse


def convert_to_vergeai_object(status_code: int, data: dict) -> APIResponse:
    return APIResponse(status_code, data)
