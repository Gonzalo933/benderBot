
import datetime as dt

class Countdown:

    def __init__(self, endDate=dt.datetime(2017, 12, 31, 23, 59, 59)):
        self.endDate = endDate
        self.now = dt.datetime.now()

    def getRemainingTime(self):
        now = dt.datetime.now()
        delta = self.endDate - now
        #chop_microseconds(delta)
        return str(delta).split(".")[0]

    def printCurrentDate(self):
        print(f"Current date: {self.now}")

    def chop_microseconds(self, delta):
        return delta - datetime.timedelta(microseconds=delta.microseconds)