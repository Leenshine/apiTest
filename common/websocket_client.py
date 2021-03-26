import json
import time

from websocket import create_connection


class WebSocketCli:

    def __init__(self, api_url):
        self.api_url = api_url
        self.running = False
        self.ws_cli = None
        self.rsp = {}

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

    def get(self, req, timeout=10):
        print("ws cli get ...")
        self.send(req)

        print("ws cli recv ...")
        end_time = time.time() + timeout
        while self.running:
            if end_time < time.time():
                print('request timeout!!!')
                break
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

