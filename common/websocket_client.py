import json
import time

from websocket import create_connection


class WebSocketCli:
    running = False
    ws_cli = None
    rsp = {}

    def __init__(self, api_url):
        self.recv_list = []
        self.api_url = api_url

    def connect(self):
        self.ws_cli = create_connection(self.api_url)

        self.running = True
        time.sleep(1)

        print("ws_cli connected...")

    def close(self):
        self.running = False
        self.ws_cli.close()
        print("ws_cli closeed...")

    def send(self, raw_req):
        self.ws_cli.send(json.dumps(raw_req))
        print("send completed.")

    def get(self, req):
        print("ws cli get ...")
        self.send(req)

        print("ws cli recv ...")
        while self.running:
            raw_rsp_data = self.ws_cli.recv()
            json_rsp_data = json.loads(raw_rsp_data)

            if json_rsp_data.get("method") == "public/heartbeat":
                self.do_hb(json_rsp_data)
            elif json_rsp_data.get("method") == "subscribe":
                self.do_subscribe(json_rsp_data)
            else:
                print("recv some noise data...")
                pass

        return self.rsp

    # def get2(self, req):
    #     print("ws cli get ...")
    #     self.send(req)
    #     raw_rsp_data = self.ws_cli.recv()
    #     self.rsp["initial_rsp"] = json.loads(raw_rsp_data)
    #
    #     raw_rsp_data = self.ws_cli.recv()
    #     self.rsp["real_rsp"] = json.loads(raw_rsp_data)
    #
    #     return self.rsp


    def do_hb(self, json_rsp_data):
        print("do hb ...")
        hb_ack = {
            "id": json_rsp_data.get("id"),
            "method": "public/respond-heartbeat",
        }
        self.send(hb_ack)

    def do_subscribe(self, json_rsp_data):
        print("do subscribe ...")
        if json_rsp_data.get("id", None) != None:
            self.rsp["initial_rsp"] = json_rsp_data
        else:
            self.rsp["real_rsp"] = json_rsp_data
            self.running = False


if __name__ == "__main__":
    cli = WebSocketCli("wss://uat-stream.3ona.co/v2/market")
    cli.connect()

    req = {
        "id": 11,
        "method": "subscribe",
        "params": {"channels": ["book.ETH_CRO.150"]},
        "nonce": 1587523073344,
    }
    rsp = cli.get(req)
    time.sleep(10)
    print(rsp)
    cli.close()