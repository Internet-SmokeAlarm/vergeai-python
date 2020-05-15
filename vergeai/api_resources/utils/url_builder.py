def url_builder(gateway, version, url, action, parameters):
    """
    :param gateway: string
    :param version: string
    :param url: string
    :param action: string
    :param parameters: dict
    """
    base_url = gateway + "/" + version + "/" + url + "/" + action

    if "group_id" in parameters:
        base_url += "/" + parameters["group_id"]
    if "round_id" in parameters:
        base_url += "/" + parameters["round_id"]
    if "device_id" in parameters:
        base_url += "/" + parameters["device_id"]

    return base_url
