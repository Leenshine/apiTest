import os
import sys
import json
import time
from datetime import datetime

root_path = str(os.path.abspath(__file__).split('cryptoTest')[0]) + 'cryptoTest'
print(root_path)
sys.path.append(root_path)

def get_config(env, parameter, file_name):
    json_file_path = os.path.join(root_path, 'config', file_name)
    try:
        with open(json_file_path, 'r') as read_file:
            config_json = json.load(read_file)
            value = config_json[env][parameter]
            return value
    except Exception as e:
        raise e


def get_rest_config(env, parameter):
    return get_config(env, parameter, 'general.json')

def get_websocket_config(env, parameter):
    return get_config(env, parameter, 'websocket_general.json')


def get_api_name(name):
    json_file_path = os.path.join(root_path, 'config', "api_name.json")
    try:
        with open(json_file_path, 'r') as read_file:
            config_json = json.load(read_file)
            value = config_json[name]
            return value
    except Exception as e:
        raise e


def unix_time(dt):
    datetime_obj = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    ret_stamp = int(time.mktime(datetime_obj.timetuple()) * 1000.0 + datetime_obj.microsecond / 1000.0)
    return ret_stamp