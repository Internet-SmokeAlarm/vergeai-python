class FedLearnConfig:

    # Flip between the following endpoints for local testing (using SAM) & production
    #PROD_ENDPOINT = "https://lnifk4x538.execute-api.us-east-1.amazonaws.com/Prod/"
    PROD_ENDPOINT = "http://127.0.0.1:3000/"

    CREATE_GROUP_PATH = PROD_ENDPOINT + "api/v1/group/create"
    DELETE_GROUP_PATH = PROD_ENDPOINT + "api/v1/group/delete"
    SUBMIT_INITIAL_GROUP_MODEL_PATH = PROD_ENDPOINT + "api/v1/group/post/initial_model"
    GET_INITIAL_GROUP_MODEL_PATH = PROD_ENDPOINT + "api/v1/group/get/initial_model"

    START_ROUND_PATH = PROD_ENDPOINT + "api/v1/round/start"
    GET_ROUND_STATE_PATH = PROD_ENDPOINT + "api/v1/round/get"

    REGISTER_DEVICE_PATH = PROD_ENDPOINT + "api/v1/device/register"
    SUBMIT_MODEL_UPDATE_PATH = PROD_ENDPOINT + "api/v1/submit_model_update"
    IS_DEVICE_ACTIVE_PATH = PROD_ENDPOINT + "api/v1/device/get/active"
