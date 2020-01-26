#!/bin/bash

CLOUD_GATEWAY_URL="https://5fr43pjmc4.execute-api.us-east-1.amazonaws.com/dev/"

DEV_AUTH_TABLE="dev-fl-auth-key"
API_KEY="WknzO6H-rU5s_puTeorirwyf9gh6fTK1BAlfDNiyAEiz9kQAkfeU1M3my3H4bSjHa6sEJDRvvYRLUCTxYjW1yA"

export CLOUD_GATEWAY_URL=$CLOUD_GATEWAY_URL
export DEV_AUTH_TABLE=$DEV_AUTH_TABLE
export API_KEY=$API_KEY

python publish_test_auth_keys.py
python -m unittest tests.api.integration_tests
