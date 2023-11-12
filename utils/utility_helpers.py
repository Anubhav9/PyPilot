import json
from utility_constants import *

"""
Utility Method to generate complete url of the request to be invoked while calling the API

Parameters
service_name (string): Name of the already onboarded Service
end_point (string): End Point that we want to invoke
is_secured (boolean): Parameter to set if we want to invoke http or https
"""
def generate_url_for_request(service_name,end_point,is_secured_protocol):
    if(is_secured_protocol==True):
        generated_url=HTTPS_PROTOCOL+service_name+SLASH+end_point
        
    else:
        generated_url=HTTP_PROTOCOL+service_name+SLASH+end_point
    
    return generated_url

"""
Utility Method to check if the json passed is a valid JSON or not

Parameters
suspect_string (json): Mostly the body to be passed in Post Request
"""
def is_valid_json(suspect_string):
    try:
        json.loads(suspect_string)
        return True
    except json.JSONDecodeError:
        return False
    
        
"""
Utility Method to replace values at run time. Usually in api calls where methods are placeholders.

Parameters
constant_name (string): The constant string where placeholder has been stored
placeholder (string): Passing the placeholder value
value (string): The value to be replaced for in placeholder
"""

def replace_placeholder(constant_name,placeholder,value):
    replace_string=constant_name.replace(placeholder,value)
    return replace_string