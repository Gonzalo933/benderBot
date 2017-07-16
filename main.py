import brain.main
import platforms.telegram
from threading import Thread
from time import sleep
import sys

def telegram_thread(arg):
    telegram = platforms.telegram.Telegram()
    #for i in range(arg):
    while 1:
        print ("Running...")
        updates = telegram.getUpdates()
        responses = telegram.processMessages(updates)
        print(str(telegram.getUpdates())+"\n")
        responses = list(map(brain.main.parse_message, responses))
        print(responses)
        telegram.sendMessages(responses)
        print("\n")
        sleep(5)
    telegram.saveState()
def main():
    thread = Thread(target=telegram_thread, args=(20, ), daemon=True)
    thread.start()
    term_command =""
    while term_command != "quit":
        term_command = input('Running: ')
    sys.exit(0)
    #thread.join()

if __name__ == "__main__":
    main()