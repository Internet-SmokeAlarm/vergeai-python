#!/bin/bash

CLOUD_GATEWAY_URL="https://5fr43pjmc4.execute-api.us-east-1.amazonaws.com/dev/"

DEV_AUTH_TABLE="dev-fl-auth-key"
API_KEY="Pr9FDAEvCYY68XDZX5hH-V4DlDXx0oXx5vz0ndtuGUbjnuX4-U1ISNr3a_sgz9wWovd1Ujkks1xgt4JlQQxKIQ"

export CLOUD_GATEWAY_URL=$CLOUD_GATEWAY_URL
export DEV_AUTH_TABLE=$DEV_AUTH_TABLE
export API_KEY=$API_KEY

python3 tests/publish_test_auth_keys.py
python3 -m unittest tests.api_resources.integration_tests
