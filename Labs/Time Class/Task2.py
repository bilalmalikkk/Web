class HoursException(Exception):
    pass

class MinutesException(Exception):
    pass

class SecondsException(Exception):
    pass

class NegativeTime(Exception):
    pass

class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        try:
            if hours <= 23 and hours >= 0:
                self.__hours = hours
            elif hours < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise HoursException("The Hours can't be greater than 23")
            if minutes <= 59 and minutes >= 0:
                self.__minutes = minutes
            elif minutes < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise MinutesException("The Minutes can't be greater than 59")
            if seconds <= 59 and seconds >= 0:
                self.__seconds = seconds
            elif seconds < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise SecondsException("The Seconds can't be greater than 59")
        except HoursException as e:
            print(str(e))
        except MinutesException as e:
            print(str(e))
        except SecondsException as e:
            print(str(e))
        except NegativeTime as e:
            print(str(e))

    @property
    def Hours(self):
        return self.__hours

    @property
    def Minutes(self):
        return self.__minutes

    @property
    def Seconds(self):
        return self.__seconds

    @Hours.setter
    def Hours(self, hours):
        try:
            if hours <= 23 and hours >= 0:
                self.__hours = hours
            elif hours < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise HoursException("The Hours can't be greater than 23")
        except HoursException as e:
            print(str(e))
        except NegativeTime as e:
            print(str(e))

    @Minutes.setter
    def Minutes(self, minutes):
        try:
            if minutes <= 59 and minutes >= 0:
                self.__minutes = minutes
            elif minutes < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise MinutesException("The Minutes can't be greater than 59")
        except MinutesException as e:
            print(str(e))
        except NegativeTime as e:
            print(str(e))

    @Seconds.setter
    def Seconds(self, seconds):
        try:
            if seconds <= 59 and seconds >= 0:
                self.__seconds = seconds
            elif seconds < 0:
                raise NegativeTime("The unit of time can't be negative")
            else:
                raise SecondsException("The Seconds can't be greater than 59")
        except SecondsException as e:
            print(str(e))
        except NegativeTime as e:
            print(str(e))

    def addTime(self, t1, t2):
        self.__seconds = t1.Seconds + t2.Seconds
        self.__minutes = self.__seconds // 60
        self.__seconds = self.__seconds % 60
        self.__minutes = self.__minutes + t1.Minutes + t2.Minutes
        self.__hours = self.__minutes // 60
        self.__minutes = self.__minutes % 60
        self.__hours = self.__hours + t1.Hours + t2.Hours
        self.__hours = self.__hours % 24

    def displayTime24(self):
        print("The 24-hour format Time is as follows:")
        print(f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}")

    def displayTime12(self):
        print("The 12-hour format Time is as follows:")
        period = "AM"
        hours = self.__hours
        if self.__hours >= 12:
            period = "PM"
            if self.__hours > 12:
                hours = self.__hours - 12
        if self.__hours == 0:
            hours = 12
        print(f"{hours:02}:{self.__minutes:02}:{self.__seconds:02} {period}")

    def displayMinute(self):
        totalMinutes = self.__hours * 60
        totalMinutes = totalMinutes + self.__minutes
        totalMinutes = totalMinutes + (self.__seconds / 60)
        print("Total number of Minutes in the time is:", end=" ")
        print(totalMinutes)

    def updateTime(self, totalMinutes):
        try:
            if totalMinutes < 0:
                raise NegativeTime("The minutes can't be negative")
        except NegativeTime as e:
            print(str(e))
        self.__hours = (self.__hours + (totalMinutes // 60)) % 24
        self.__minutes = (self.__minutes + (totalMinutes % 60)) % 60


t1 = Time(23, 59, 30)
t2 = Time(0, 30, 45)

t1.displayTime24()
t1.displayTime12()

t2.displayTime24()
t2.displayTime12()

t1.addTime(t1, t2)
t1.displayTime24()
t1.displayTime12()

t1.displayMinute()
t1.updateTime(200)
t1.displayTime24()
t1.displayTime12()
