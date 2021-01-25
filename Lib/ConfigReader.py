from configparser import ConfigParser
from pathlib import Path


'''
This function will load config property file 
from "./Config/input.cfg" location by default
in case, user provided any specific path, it will read from there
'''


def load_config_file(path="./Config/input.cfg"):
    global parser
    path = Path(__file__).parent.parent/"Config/input.cfg"
    parser = ConfigParser()
    return parser.read(path)

'''
it will take section and propertyname as arguments.
if property found in property it will return result 
otherwise, it will return "None"
'''


def get_config_property(section, prop_name):
    try:
        load_config_file()
        return parser.get(section, prop_name)
    except:
        return None

'''
it will return baseurl property from info section 
'''


def get_base_url():
    return get_config_property("info","baseURL")

'''
it will return symbol property from info section 
'''


def get_symbol():
    return get_config_property("info","symbol")


'''
it will return apiKey property from info section 
'''


def get_api_key():
    return get_config_property("info","apiKey")
