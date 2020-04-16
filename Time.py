#Units of Time

days = int(input("Please input the number of days: "))
hours = int(input("Please input the number of hours: "))
minutes = int(input("Please input the number of minutes: "))
seconds = int(input("Please input the number of seconds: "))

total = days * 86400 + hours * 3600 + minutes * 60 + seconds

print(total)

#Units of time (Again)
seconds = int(input("Insert time in seconds: "))

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

if seconds < 10:
    seconds = "0" + str(seconds)

if hours < 10:
    hours = "0" + str(hours)

if minutes < 10:
    minutes = "0" + str(minutes)

print(days, hours, minutes, seconds)

#Current time
from time import time, asctime

curr_time = time()
curr_time = asctime()

print(curr_time)
