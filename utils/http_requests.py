import logging
import requests
import utility_helpers

"""
Utility Method to invoke get request by constructing the URL at run time

Parameters
service_name (string): Name of the already onboarded Service
end_point (string): End Point that we want to invoke
headers : header like Authorisation etc, if any
is_secured (boolean): Parameter to set if we want to invoke http or https
"""
def invoke_get_request(service_name,end_point,headers=None,is_secured=True):
    generated_url=utility_helpers.generate_url_for_request(service_name,end_point,is_secured)
    response=requests.get(generated_url,headers=headers)
    return response

"""
Utility Method to invoke post request by constructing the URL at run time

Parameters
service_name (string): Name of the already onboarded Service
end_point (string): End Point that we want to invoke
body (json): Constructing the body request at run time
headers : header like Authorisation etc, if any
is_secured (boolean): Parameter to set if we want to invoke http or https
"""
def invoke_post_request(service_name, end_point, body, headers=None,is_secured=True):
    generated_url = utility_helpers.generate_url_for_request(service_name, end_point,is_secured)
    if not utility_helpers.is_valid_json(body):
        raise ValueError("Provided body is not a valid JSON")

    response=requests.post(generated_url,headers=headers,data=body)

    return response
    
