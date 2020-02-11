from datetime import date
from datetime import time
from datetime import datetime

## DATE OBJECTS
# Get today's date using today() method from the date class
today = date.today()
print("Today's date is ", today)

# Print out the date's individual components
print("Date component's: ", today.day, today.month, today.year)

# Retrieve today's weekday (0= Monday, 6=Sunday)
print("Today's weekday number is: ", today.weekday())
# add an additional layer to make it more informative:
days = ['mon', 'tues', 'weds', 'thurs', 'fri', 'sat', 'sun']
print("Which is a: ", days[today.weekday()])                 # indexing from days

## DATETIME OBJECTS ######################################
# Get today's date from the datetime class
today = datetime.now()
print("The current date and time is ", today)

# Get the current time
t = datetime.time(datetime.now())
print(t)

# FORMATTING TIME OUTPUT ###############################################
# Times and dates can be formatted using a set of predefined string control codes
# Use strftime() method
now = datetime.now()
print(now.strftime())

### Date Formatting ###
# lower for abbreviate, caps for full:
# %y/%Y - Year
# %a/%A - Weekday
# %b/%B - Month
# %d/%D - Day of Month

print(now.strftime("The current year is: %Y"))   #just plug in any of the above

print(now.strftime("%a, %d %B, %y))

# %c - locale's date and time
# %x - locale's date
# %X - locale's time

print(now.strftime("Locale date and time: %c"))
print(now.strftime("Locale date: %x"))
print(now.strftime("Locale time: %X"))

### Time Formatting ###

# %I/%H - 12/24 Hour
# %M - minute
# %S - second
# %p - locale's AM/PM

print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24-hour time: %H:%M"))
