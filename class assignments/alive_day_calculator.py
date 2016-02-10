import time
import datetime

year = int(input("year: "))
month = int(input("month: "))
day = int(input("day: "))

today = datetime.date.today()

days_lived = datetime.date(today.year, today.month, today.day)\
             - datetime.date(year, month, day)

print("You have lived: " + str(days_lived.days) + " days")
