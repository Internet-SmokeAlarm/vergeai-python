class FedLearnEndpointConfig:

    CREATE_GROUP = "v1/group/create"
    DELETE_GROUP = "v1/group/delete"
    SUBMIT_GROUP_INITIAL_MODEL = "v1/group/post/initial_model"
    GET_GROUP_INITIAL_MODEL = "v1/group/get/initial_model/GROUP_ID"
    GET_CURRENT_ROUND_ID = "v1/group/get/current_round_id/GROUP_ID"

    START_ROUND = "v1/round/start"
    GET_ROUND = "v1/round/get/GROUP_ID/ROUND_ID"
    GET_ROUND_AGGREGATE_MODEL = "v1/round/get/aggregate_model/GROUP_ID/ROUND_ID"
    GET_ROUND_START_MODEL = "v1/round/get/start_model/GROUP_ID/ROUND_ID"

    REGISTER_DEVICE = "v1/device/register"
    SUBMIT_MODEL_UPDATE = "v1/submit_model_update"
    IS_DEVICE_ACTIVE = "v1/device/get/active/GROUP_ID/ROUND_ID/DEVICE_ID"

    GET_GROUP = "v1/group/get/GROUP_ID"
