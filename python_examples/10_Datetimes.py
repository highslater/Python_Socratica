#!/usr/bin/env python3.7

"""10_Datetimes.py.

Tenth Program of the Socratica Sexy Hologram Human/Computer Hybrid
Python Series.
"""

from platform import python_version
from sys import hexversion
import datetime

gvr = datetime.date(1956, 1, 31)
mill = datetime.date(2000, 1, 1)
dt = datetime.timedelta(100)
message = "GVR was born on {:%A, %B, %d, %Y}."

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

now = datetime.datetime.today()

moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")

print("The Python Version is:", python_version(), " #" + str((hexversion)))
print(dir(datetime), "\n\n")

for f in dir(datetime):
    if f.startswith('d') or f.startswith('t'):
        print(f, end=" ,    ")

print()
print()
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)
print(mill)
print(mill + dt)
print()

print(gvr.strftime("%A, %B, %d, %Y"))
print(mill.strftime("%A, %B, %d, %Y"))
print((mill + dt).strftime("%A, %B, %d, %Y"))
print(message.format(gvr))
print()

print(launch_date)
print(launch_date.year)
print(launch_date.month)
print(launch_date.day)
print()
print(launch_time)
print(launch_time.hour)
print(launch_time.minute)
print(launch_time.second)
print()
print(launch_datetime)
print(launch_datetime.year)
print(launch_datetime.month)
print(launch_datetime.day)
print(launch_datetime.hour)
print(launch_datetime.minute)
print(launch_datetime.second)
print()

print(now)
print(now.microsecond)
print()

print(moon_landing_datetime, type(moon_landing_datetime))
print()


"""./10_Datetimes.py
The Python Version is: 3.7.2  #50791152
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime',
'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


date ,    datetime ,    datetime_CAPI ,    time ,    timedelta ,
timezone ,    tzinfo ,

1956-01-31
1956
1
31
2000-01-01
2000-04-10

Tuesday, January, 31, 1956
Saturday, January, 01, 2000
Monday, April, 10, 2000
GVR was born on Tuesday, January, 31, 1956.

2017-03-30
2017
3
30

22:27:00
22
27
0

2017-03-30 22:27:00
2017
3
30
22
27
0

2019-03-05 14:12:02.696160
696160

1969-07-20 00:00:00 <class 'datetime.datetime'>
"""
