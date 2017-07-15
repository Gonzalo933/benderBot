import brain.main
import platforms.telegram
from threading import Thread
from time import sleep


def telegram_thread(arg):
    telegram = platforms.telegram.Telegram()
    for i in range(arg):
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
    thread = Thread(target=telegram_thread, args=(20, ))
    thread.start()
    thread.join()

if __name__ == "__main__":
    main()