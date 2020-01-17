class FedLearnEndpointConfig:

    # Flip between the following endpoints for local testing (using SAM) & production
    # Production
    ENDPOINT = "https://ivcqfi3rrc.execute-api.us-east-1.amazonaws.com/prod/"
    # Dev
    #ENDPOINT = "https://5fr43pjmc4.execute-api.us-east-1.amazonaws.com/dev/"
    # Local
    #ENDPOINT = "http://127.0.0.1:3000/"

    CREATE_GROUP = ENDPOINT + "v1/group/create"
    DELETE_GROUP = ENDPOINT + "v1/group/delete"
    SUBMIT_GROUP_INITIAL_MODEL = ENDPOINT + "v1/group/post/initial_model"
    GET_GROUP_INITIAL_MODEL = ENDPOINT + "v1/group/get/initial_model/GROUP_ID"
    GET_CURRENT_ROUND_ID = ENDPOINT + "v1/group/get/current_round_id/GROUP_ID"

    START_ROUND = ENDPOINT + "v1/round/start"
    GET_ROUND = ENDPOINT + "v1/round/get/GROUP_ID/ROUND_ID"
    GET_ROUND_AGGREGATE_MODEL = ENDPOINT + "v1/round/get/aggregate_model/GROUP_ID/ROUND_ID"
    GET_ROUND_START_MODEL = ENDPOINT + "v1/round/get/start_model/GROUP_ID/ROUND_ID"

    REGISTER_DEVICE = ENDPOINT + "v1/device/register"
    SUBMIT_MODEL_UPDATE = ENDPOINT + "v1/submit_model_update"
    IS_DEVICE_ACTIVE = ENDPOINT + "v1/device/get/active/GROUP_ID/ROUND_ID/DEVICE_ID"

    GET_GROUP = ENDPOINT + "v1/group/get/GROUP_ID"
