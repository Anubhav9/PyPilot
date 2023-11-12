import requests
import logging
import utility_helpers


def invoke_get_request(service_name,end_point,headers=None):
    generated_url=utility_helpers.generate_url_for_request(service_name,end_point)
    if(headers is not None):
        response=requests.get(generated_url,headers=headers)
    else:
        response=requests.get(generated_url)
    return response


def invoke_post_request(service_name, end_point, body, headers=None):
    generated_url = utility_helpers.generate_url_for_request(service_name, end_point)
    if not utility_helpers.is_valid_json(body):
        raise ValueError("Provided body is not a valid JSON")

    if headers is not None:
        response = requests.post(generated_url, headers=headers, data=body)
    else:
        response = requests.post(generated_url, data=body)

    return response