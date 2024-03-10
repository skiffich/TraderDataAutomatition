import json
import os

import eth_account
from eth_account.signers.local import LocalAccount

from hyperliquid.exchange import Exchange
from hyperliquid.info import Info

def get_config():
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    with open(config_path) as f:
        config = json.load(f)
        return config
    
def get_log_paths():
    paths = get_config()["log_paths"]
    logs_folder = os.path.join(os.path.dirname(__file__), "..//logs")
    for key in paths:
        paths[key] = os.path.join(logs_folder, paths[key])
    return paths

def clear_logs():
    logs_folder = os.path.join(os.path.dirname(__file__), "..//logs")
    if not os.path.exists(logs_folder):
        os.makedirs("logs")
    for log_path in get_log_paths().values():
        log_path = os.path.join("../logs", log_path)
        with open(log_path, 'w') as file:
            pass

def get_follow_user():
    return get_config()["follow_user"]

def get_net_url():
    return get_config()["net_url"]

def setup(base_url=None, skip_ws=False):
    config = get_config()
    account: LocalAccount = eth_account.Account.from_key(config["secret_key"])
    address = config["account_address"]
    if address == "":
        address = account.address
    print("Running with account address:", address)
    if address != account.address:
        print("Running with agent address:", account.address)
    info = Info(base_url, skip_ws)
    user_state = info.user_state(address)
    margin_summary = user_state["marginSummary"]
    if float(margin_summary["accountValue"]) == 0:
        print("Not running the example because the provided account has no equity.")
        url = info.base_url.split(".", 1)[1]
        error_string = f"No accountValue:\nIf you think this is a mistake, make sure that {address} has a balance on {url}.\nIf address shown is your API wallet address, update the config to specify the address of your account, not the address of the API wallet."
        raise Exception(error_string)
    exchange = Exchange(account, base_url, account_address=address)
    return address, info, exchange