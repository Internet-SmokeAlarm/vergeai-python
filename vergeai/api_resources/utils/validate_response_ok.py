def validate_response_ok(status_code: int) -> bool:
    return status_code == 200 or status_code == 204
