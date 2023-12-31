"""
""Utilities for RESTful requests: GET, POST, PATCH, PUT."

Author: Anubhav Sanyal
Creation Date: 12/11/2023
"""
import logging
import requests
from utils.utility_helpers import *


def invoke_get_request(service_name,end_point,headers=None,is_secured=True):
    """
    Utility Method to invoke get request by constructing the URL at run time
    
    Parameters
    service_name (string): Name of the already onboarded Service
    end_point (string): End Point that we want to invoke
    headers : header like Authorisation etc, if any
    is_secured (boolean): Parameter to set if we want to invoke http or https
    """
    generated_url=generate_url_for_request(service_name,end_point,is_secured)
    response=requests.get(generated_url,headers=headers)
    return response


def invoke_post_request(service_name, end_point, body, headers=None,is_secured=True):
    """
    Utility Method to invoke post request by constructing the URL at run time
    
    Parameters
    service_name (string): Name of the already onboarded Service
    end_point (string): End Point that we want to invoke
    body (json): Constructing the body request at run time
    headers : header like Authorisation etc, if any
    is_secured (boolean): Parameter to set if we want to invoke http or https
    """
    generated_url = generate_url_for_request(service_name, end_point,is_secured)
    if not is_valid_json(body):
        raise ValueError("Provided body is not a valid JSON")
    response=requests.post(generated_url,headers=headers,data=body)
    return response
