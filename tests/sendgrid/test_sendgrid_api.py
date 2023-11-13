"""
This module contains test file related to SendGrid, example API used for onboarding

Author: Anubhav Sanyal
Creation Date: 13/11/2023
"""
import sys
import pytest
import os
import json
from utils import http_requests
from services.service_endpoints import sendgrid_endpoints
from services import service_names
import sendgrid_constants
def test_send_email_to_recipient_with_correct_key():
    """
    Happy Flow to Check if email is being sent correctly when key is being correctly passed
    """
    SEND_GRID_API_KEY_CORRECT=os.environ.get("SENDGRID_API_KEY_CORRECT","")
    COMPLETE_KEY="Bearer "+SEND_GRID_API_KEY_CORRECT
    headers={"Content-Type":"application/json","Authorization":COMPLETE_KEY}
    ##HardCoding Body for as of now
    body={"personalizations":[{"to":[{"email":"anubhavsanyal9@gmail.com"}]}],"from":{"email":"princebest3@rediffmail.com"},"subject":"Hello, World!","content":[{"type":"text/plain","value":"Heya!"}]}
    body=json.dumps(body)

    response=http_requests.invoke_post_request(service_names.SEND_GRID_URL,sendgrid_endpoints.SEND_EMAIL_ENDPOINT_POST,headers=headers,body=body)
    status_code=response.status_code
    assert status_code==202,f"Expected response was 201, got different status code"

def test_send_email_to_recipient_with_incorrect_key():
    """
    Negative Scenario to check unauthorised error when wrong key is passed
    """
    SEND_GRID_API_KEY_INCORRECT=os.environ.get("SENDGRID_API_KEY_INCORRECT","")
    COMPLETE_KEY="Bearer "+SEND_GRID_API_KEY_INCORRECT
    headers={"Content-Type":"application/json","Authorization":COMPLETE_KEY}
    ##HardCoding Body for as of now
    body={"personalizations":[{"to":[{"email":"anubhavsanyal9@gmail.com"}]}],"from":{"email":"princebest3@rediffmail.com"},"subject":"Hello, World!","content":[{"type":"text/plain","value":"Heya!"}]}
    body=json.dumps(body)
    response=http_requests.invoke_post_request(service_names.SEND_GRID_URL,sendgrid_endpoints.SEND_EMAIL_ENDPOINT_POST,headers=headers,body=body)
    status_code=response.status_code
    assert status_code==401,f"Expected response was 401, got different status code"
