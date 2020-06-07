import requests
import config

def request(extension, params=None):
    request_url = config.url + extension

    result = None
    if params:
        params["token"] = config.token
    else:
        params = {"token" : config.token}

    result = requests.get(request_url, params=params)
    return result