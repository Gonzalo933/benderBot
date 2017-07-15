import actions.countdown
import re

def parse_command(command):
    regex_countdown = r"countdown"
    if re.search(regex_countdown, command):
        countdown = actions.countdown.Countdown()
        print(countdown.getRemainingTime())




def main():
    # my code here
    parse_command('holacountdown')


if __name__ == "__main__":
    main()