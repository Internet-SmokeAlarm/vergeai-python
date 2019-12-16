class FedLearnConfig:

    # Flip between the following endpoints for local testing (using SAM) & production
    #PROD_ENDPOINT = "https://lnifk4x538.execute-api.us-east-1.amazonaws.com/Prod/"
    PROD_ENDPOINT = "http://127.0.0.1:3000/"

    CREATE_GROUP_PATH = PROD_ENDPOINT + "api/v1/group/create"
    DELETE_GROUP_PATH = PROD_ENDPOINT + "api/v1/group/delete"
