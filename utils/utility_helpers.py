import json
from utility_constants import *

def generate_url_for_request(service_name,end_point,is_secured_protocol):
    if(is_secured_protocol==True):
        generated_url=HTTPS_PROTOCOL+service_name+SLASH+end_point
        
    else:
        generated_url=HTTP_PROTOCOL+service_name+SLASH+end_point
    
    return generated_url

def is_valid_json(suspect_string):
    try:
        json.loads(suspect_string)
        return True
    except json.JSONDecodeError:
        return False
    
        
def replace_placeholder(constant_name,placeholder,value):
    replace_string=constant_name.replace(placeholders,value)
    return replace_string
