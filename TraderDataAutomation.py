from hyperliquid.info import Info

from utils import config
from utils.handlers import (
    on_user_events,
    on_order_updates,
    on_user_fills,
    on_user_fundings
    )


def main():
    config.clear_logs()

    info = Info(config.get_net_url(), skip_ws=False)
    info.subscribe({"type": "userEvents", "user":   config.get_follow_user()}, on_user_events)
    info.subscribe({"type": "orderUpdates", "user": config.get_follow_user()}, on_order_updates)
    info.subscribe({"type": "userFills", "user":    config.get_follow_user()}, on_user_fills)
    info.subscribe({"type": "userFundings", "user":    config.get_follow_user()}, on_user_fundings)


if __name__ == "__main__":
    main()
