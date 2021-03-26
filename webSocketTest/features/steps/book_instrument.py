from behave import *
from common.utils import *



@given('User send request with "{instrument_name}" and "{depth}"')
def user_send_book_request(context, instrument_name, depth):
    params = "book." + instrument_name + "." + depth
    req = {
        "id": 11,
        "method": "subscribe",
        "params": {"channels": [params]},
        "nonce": 1587523073344,
    }

    context.rsp = context.cli.get(req).get('real_rsp', None)


@then('check the "{method}" is expected')
def check_the_request_method_is_expected(context, method):
    assert method == context.rsp.get('method'), f"expeted method {method}, current is : {context.rsp.get('method')}"


@then('check the "{instrument_name}" is correct')
def check_result_instrument_name(context, instrument_name):
    context.results = context.rsp.get('result')
    assert instrument_name == context.results.get('instrument_name')


@then('check the "{subscription}" is expected subscription')
def check_result_subscription(context, subscription):
    assert subscription == context.results.get('subscription')


@then('check the "{depth}" is expected depth')
def check_expected_result_depth(context, depth):
    assert int(depth) == context.results.get('depth')


@then('verify the invalid response message')
def check_expected_result_depth(context):
    assert context.rsp == None
