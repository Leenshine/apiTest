from behave import *
from common.utils import *



@given('User send request with "{instrument_name}" and "{depth}"')
def user_send_request2(context, instrument_name, depth):
    req = {
        "id": 11,
        "method": "subscribe",
        "params": {"channels": ["book.ETH_CRO.150"]},
        "nonce": 1587523073344,
    }

    rsp = context.cli.get(req)
    print("111111/n")
    print(rsp)
    print("111111/n")


@then(u'check the "subscribe" is expected')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then check the "subscribe" is expected')
