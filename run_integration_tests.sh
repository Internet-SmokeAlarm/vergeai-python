#!/bin/bash

CLOUD_GATEWAY_URL="https://5fr43pjmc4.execute-api.us-east-1.amazonaws.com/dev/"
#CLOUD_GATEWAY_URL="http://127.0.0.1:3000/"

DEV_AUTH_TABLE="dev-fl-auth-key"
API_KEY="Pr9FDAEvCYY68XDZX5hH-V4DlDXx0oXx5vz0ndtuGUbjnuX4-U1ISNr3a_sgz9wWovd1Ujkks1xgt4JlQQxKIQ"

export CLOUD_GATEWAY_URL=$CLOUD_GATEWAY_URL
export DEV_AUTH_TABLE=$DEV_AUTH_TABLE
export API_KEY=$API_KEY

python publish_test_auth_keys.py
python -m unittest tests.api.integration_tests
