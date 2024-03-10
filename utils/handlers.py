import json
from utils import config

def on_user_events(data) -> None:
        if "fills" in data["data"]:
            with open(config.get_log_paths()["user_events"], "a+") as f:
                jd = json.dumps(data["data"]["fills"])
                #print(jd)
                f.write(jd)
                f.write("\n")

def on_order_updates(data) -> None:
    with open(config.get_log_paths()["order_updates"], "a+") as f:
        jd = json.dumps(data["data"])
        #print(jd)
        f.write(jd)
        f.write("\n")

def on_user_fills(data):
    with open(config.get_log_paths()["user_fills"], "a+") as f:
        jd = json.dumps(data["data"]["fills"])
        #print(jd)
        f.write(jd)
        f.write("\n")

def on_user_fundings(data):
    with open(config.get_log_paths()["user_fundings"], "a+") as f:
        jd = json.dumps(data["data"]["fundings"])
        #print(jd)
        f.write(jd)
        f.write("\n")