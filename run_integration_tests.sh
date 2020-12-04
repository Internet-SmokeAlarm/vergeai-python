#!/bin/bash

DEV_AUTH_TABLE="dev-fl-auth-key"

export DEV_AUTH_TABLE=$DEV_AUTH_TABLE

python3 tests/publish_test_auth_keys.py
python3 -m unittest tests.api_resources.integration_tests
