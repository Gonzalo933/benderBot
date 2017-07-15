import requests
import sys
import os

class Telegram:
    def __init__(self):
        try:
            self.api_token = os.environ['TELEGRAM_TOKEN']
        except KeyError:
            print("Enviroment var TELEGRAM_TOKEN not found, make sure you add it with your api token")
            sys.exit(1)

    def getUpdates(self):
        r = requests.get("https://api.telegram.org/bot"+self.api_token+"/getUpdates")
        print(r.json())

Telegram().getUpdates()
