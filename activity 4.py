import datetime

x=datetime.datetime.now()
print("current time is",x)
print ("current year is",x.year)
print("Today's date is",x.strftime('%d'))
print("Today is",x.strftime('%a'))

import calendar

print (calendar.calendar(2025))
