from behave import fixture, use_fixture

from common.websocket_client import WebSocketCli
from common.utils import get_websocket_config

@fixture
def websocket_connect(context):
    context.cli = WebSocketCli(get_websocket_config("uat", "env_path"))
    context.cli.connect()
    return context.cli

def before_scenario(context, scenario):
    use_fixture(websocket_connect, context)


def after_scenario(context, scenario):
    context.cli.close()
