def url_builder(gateway: str, version: str, url: str, action: str, parameters: dict) -> str:
    base_url = gateway + "/" + version + "/" + url + "/" + action

    if "project_id" in parameters:
        base_url += "/" + parameters["project_id"]
    if "experiment_id" in parameters:
        base_url += "/" + parameters["experiment_id"]
    if "job_id" in parameters:
        base_url += "/" + parameters["job_id"]
    if "device_id" in parameters:
        base_url += "/" + parameters["device_id"]

    return base_url
