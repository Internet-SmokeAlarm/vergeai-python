def validate_response_ok(status_code):
    """
    :param status_code: int
    """
    if status_code == 200 or status_code == 204:
        return True

    return False
