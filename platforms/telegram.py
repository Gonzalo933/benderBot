import requests
import sys
import os
import json

class Telegram:
    def __init__(self):
        try:
            self.api_token = os.environ['TELEGRAM_TOKEN']
        except KeyError:
            print("Enviroment var TELEGRAM_TOKEN not found, make sure you add it with your api token")
            sys.exit(1)
        self.loadState()

    def processMessages(self, updates):
        responses = []
        for m in updates["result"]:
            response_entry = {
                "update_id": m["update_id"],
                "chat_id": m["message"]["chat"]["id"],
                "command": m["message"]["text"],
                "response_text": "" # we now pass this to the brain to know the appropiate response
            }
            responses.append(response_entry)
        return responses
    def getUpdates(self):
        options= {"offset": self.state["last_update_answered"]+1}
        r = requests.get("https://api.telegram.org/bot"+self.api_token+"/getUpdates", json=options)
        updates = r.json()
        if not updates["result"]:
            return updates
        #Sort
        updates["result"].sort(key=lambda x: x["update_id"])
        self.state["last_update_received"] = max([x['update_id'] for x in updates["result"]])
        return updates

    def saveState(self):
        f = open('telegram_state.txt', 'w')
        json.dump(self.state, f)
        f.close()

    def sendMessages(self, message_list):
        for m in message_list:
            response = {
                'chat_id': m['chat_id'],
                'text': m['response_text']
                }
            r = requests.post("https://api.telegram.org/bot"+self.api_token+"/sendMessage", json=response)
            if r.status_code == 200:
                print("Response:" + r.json()["result"]["text"])
                self.state["last_update_answered"] = m["update_id"]


    def loadState(self):
        f = open('telegram_state.txt', 'r')
        self.state = json.load(f)
        f.close()
#Telegram().getUpdates()
