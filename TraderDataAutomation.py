from hyperliquid.info import Info
from hyperliquid.utils import constants

import logging

# Configure logging to display debug messages
#logging.basicConfig(level=logging.DEBUG)

def userEvents_callback_function(data):
    print("userEvents_callback_function:", data)

def orderUpdates_callback_function1(data):
    print("orderUpdates_callback_function:", data)

def userFills_callback_function(data):
    print("userFills_callback_function:", data)

def userFundings_callback_function(data):
    print("userFundings_callback_function:", data)

def main():
    info = Info(constants.MAINNET_API_URL, skip_ws=False)
    info.subscribe({"type": "userEvents", "user":   "0x0856a8e260d6189b8560f734e5e3c99208c86554"}, userEvents_callback_function)
    info.subscribe({"type": "orderUpdates", "user": "0x0856a8e260d6189b8560f734e5e3c99208c86554"}, orderUpdates_callback_function1)
    info.subscribe({"type": "userFills", "user":    "0x0856a8e260d6189b8560f734e5e3c99208c86554"}, userFills_callback_function)
    info.subscribe({"type": "userFundings", "user":    "0x0856a8e260d6189b8560f734e5e3c99208c86554"}, userFundings_callback_function)


if __name__ == "__main__":
    main()
