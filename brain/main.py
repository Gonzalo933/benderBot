import brain.actions.countdown
import re

def parse_command(command):
    regex_countdown = r"countdown" #maybe (?i)countdown
    if re.search(regex_countdown, command, re.IGNORECASE):
        countdown = brain.actions.countdown.Countdown()
        return countdown.getRemainingTime()
    return "Invalid Command"


def parse_message(message):
    msg_str = message['command']
    message['response_text'] = parse_command(msg_str)
    return message

def main():
    # my code here
    return


if __name__ == "__main__":
    main()