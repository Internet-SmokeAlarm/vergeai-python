import unittest

import vergeai
from vergeai.clients import DummyClient
from vergeai import APIRequestor

class UT_APIRequestorTestCase(unittest.TestCase):

    def test_request_post_pass(self):
        vergeai.client = DummyClient
        api_requestor = APIRequestor()

        response = api_requestor._request_post("url1", "action1", {"group_id" : "woohoo"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"object_name" : "you called 'post'!"})
        self.assertEqual(response.json, {
            "status_code" : 200,
            "data" : {"object_name" : "you called 'post'!"}
        })

    def test_request_get_pass(self):
        vergeai.client = DummyClient
        api_requestor = APIRequestor()

        response = api_requestor._request_get("url1", "action1", {"group_id" : "woohoo"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"object_name" : "you called 'get'!"})
        self.assertEqual(response.json, {
            "status_code" : 200,
            "data" : {"object_name" : "you called 'get'!"}
        })

    def test_request_pass_1(self):
        vergeai.client = DummyClient
        api_requestor = APIRequestor()

        response = api_requestor.request("post", "url1", "action1", {"group_id" : "woohoo"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"object_name" : "you called 'post'!"})
        self.assertEqual(response.json, {
            "status_code" : 200,
            "data" : {"object_name" : "you called 'post'!"}
        })

    def test_request_pass_2(self):
        vergeai.client = DummyClient
        api_requestor = APIRequestor()

        response = api_requestor.request("get", "url1", "action1", {"group_id" : "woohoo"})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"object_name" : "you called 'get'!"})
        self.assertEqual(response.json, {
            "status_code" : 200,
            "data" : {"object_name" : "you called 'get'!"}
        })
