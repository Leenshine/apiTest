from behave import fixture, use_fixture

from common.websocket_client import WebSocketCli

def before_feature(context, feature):
    context.cli = WebSocketCli("wss://uat-stream.3ona.co/v2/market")
    context.cli.connect()


def after_feature(context, feature):
    context.cli.close()