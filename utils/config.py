import json
import os

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