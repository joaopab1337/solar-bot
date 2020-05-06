import requests

from actions import *

init_webhook = lambda url: requests.get(url)

# TODO: Add actions..
actions = {
    '/ednaldo': ednaldo
}

handle_action = lambda request, action: actions.get(action, invalid_action)(request)


parse_webhook_data = lambda parameter_list: expression
