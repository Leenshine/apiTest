from behave import *
from common.utils import *
import requests


@given('User send request with "{instrument_name}" and "{interval}"')
def user_send_request(context, instrument_name, interval):
    context.instrument_name = instrument_name
    context.interval = interval
    api_name = get_api_name('get-candlestick')
    api_version = get_rest_config('uat', 'version')
    api_url = get_rest_config('uat', 'env_path') + '/' + api_version + '/' + api_name
    content_type = {"ContentType": "application/json"}
    params = {"instrument_name": context.instrument_name, "timeframe": context.interval}
    context.rsp = requests.get(api_url, params=params, headers=content_type)
    context.rsp_data = context.rsp.json()


@then('check the "{response_status}" is expected')
def check_response_status(context, response_status):
    assert context.rsp.status_code == int(response_status)


@then('check the "{response_code}" is correct')
def check_response_code(context, response_code):
    print(context.rsp_data.get('code') )
    assert context.rsp_data.get('code') == int(response_code), f"expected is {response_code},  but the current was {context.rsp_data.get('code')}"


@then('check the "{response_method}" is expected method')
def check_responsedata_methed(context, response_method):
    assert context.rsp_data.get('method') == response_method


@then('check the instrument name in result is correct')
def check_instrument_name(context):
    current_instrument = context.rsp_data.get("result").get("instrument_name")
    assert current_instrument == context.instrument_name, f'expected is {context.instrument_name},  but the current was {current_instrument}'


@then('check the interval in result is correct')
def is_intercal_correct(context):
    current_interval = context.rsp_data.get("result").get("interval")
    assert current_interval == context.interval, f'expected is {context.interval},  but the current was {current_interval}'


@then('verify the k-line data is correct at the "{specified_time}"')
def verify_kline_data_by_selected_date(context, specified_time):
    dt = unix_time(specified_time)
    expected_data = {'t': 1593043200000, 'o': 2084.1, 'h': 2084.1, 'l': 1825.0, 'c': 1825.0, 'v': 315.166}
    current_data = context.rsp_data.get("result").get("data")
    for data in current_data:
        if data['t'] == dt:
            assert expected_data == data, f"current_data:{expected_data} not expexted:{data}"
            break


@then('check the response is invalid')
def check_invalid_instrument(context):
    current_data = context.rsp_data.get("result").get("data")
    assert current_data == None


@then('check the response is invalid interval')
def check_invalid_interval(context):
    current_code = context.rsp_data.get('code')
    assert current_code != 0













