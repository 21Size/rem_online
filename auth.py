import requests as rq
import json


def get_token():
    data = {
        "api_key": "9b704468b33547849fd1e692b3dc8d10"
    }
    token = rq.post("https://api.remonline.ru/token/new", data=data).text
    token = json.loads(token)
    print(token)

    return token["token"]

