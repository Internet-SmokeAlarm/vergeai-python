class FedLearnEndpointConfig:

    # Flip between the following endpoints for local testing (using SAM) & production
    PROD_ENDPOINT = "https://u9d76daqf7.execute-api.us-east-1.amazonaws.com/Prod/"
    #PROD_ENDPOINT = "http://127.0.0.1:3000/"

    CREATE_GROUP = PROD_ENDPOINT + "v1/group/create"
    DELETE_GROUP = PROD_ENDPOINT + "v1/group/delete"
    SUBMIT_GROUP_INITIAL_MODEL = PROD_ENDPOINT + "v1/group/post/initial_model"
    GET_GROUP_INITIAL_MODEL = PROD_ENDPOINT + "v1/group/get/initial_model/GROUP_ID"
    GET_CURRENT_ROUND_ID = PROD_ENDPOINT + "v1/group/get/current_round_id/GROUP_ID"

    START_ROUND = PROD_ENDPOINT + "v1/round/start"
    GET_ROUND = PROD_ENDPOINT + "v1/round/get/GROUP_ID/ROUND_ID"
    GET_ROUND_AGGREGATE_MODEL = PROD_ENDPOINT + "v1/round/get/aggregate_model/GROUP_ID/ROUND_ID"
    GET_ROUND_START_MODEL = PROD_ENDPOINT + "v1/round/get/start_model/GROUP_ID/ROUND_ID"

    REGISTER_DEVICE = PROD_ENDPOINT + "v1/device/register"
    SUBMIT_MODEL_UPDATE = PROD_ENDPOINT + "v1/submit_model_update"
    IS_DEVICE_ACTIVE = PROD_ENDPOINT + "v1/device/get/active/GROUP_ID/ROUND_ID/DEVICE_ID"

    GET_GROUP = PROD_ENDPOINT + "v1/group/get/GROUP_ID"
