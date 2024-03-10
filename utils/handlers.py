import json
from utils import config

def on_user_events(data) -> None:
        if "fills" in data["data"]:
            with open(config.get_log_paths()["user_events"], "a+") as f:
                jd = json.dumps(data["data"]["fills"])
                #print(jd)
                f.write(jd)
                f.write("\n")
            for operation in data["data"]["fills"]:
                execute_trade(operation)

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

def execute_trade(operation):
    coin = operation["coin"]
    px = float(operation["px"])
    sz = float(operation["sz"])
    side = operation["side"] == "B"
    cloid = operation.get("cloid")

    address, info, exchange = config.setup(config.get_net_url(), skip_ws=True)
    
    if operation["dir"].startswith("Open"):
        order_result = exchange.order(coin, side, sz, px, {"limit": {"tif": "Gtc"}}, cloid=cloid)
        with open(config.get_log_paths()["trade_user_events"], "a+") as f:
            order = {
                "coin": coin,
                "side": side,
                "sz": sz,
                "px": px,
                "order_type": {"limit": {"tif": "Gtc"}},
                "reduce_only": False,
                "cloid":cloid
            }
            f.write(json.dumps(order))
            f.write("\n")
    else:
        order_result = exchange.market_close(coin, sz=sz, px=px, slippage=0.01, cloid=cloid)
        with open(config.get_log_paths()["trade_user_events"], "a+") as f:
            order = {
                "coin": coin,
                "side": side,
                "sz": sz,
                "px": px,
                "slippage":0.01,
                "cloid": cloid,
            }
            f.write(json.dumps(order))
            f.write("\n")