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
                   
                   
# TIME DELTA #######################################
# it's basically a span of time, helpful for time-based mathematics  
from date time import timedelta     
                   
# just create the timedelta class and pass in the amount of time  that you want it to represent                  
# construct a basic timedelta
print(timedelta(days=365, hours=5, minutes=1)
      
#print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now
print("In one year from now, it will be: " + str(now + timedelta(365))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + 
      str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks =1)
s = t.strftime("%A %B %d, %Y)
print("One week ago it was " + s)

# Calculate how many days it is until the next April Fool's
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone this year
# if it has, use replace() function to get the date for next year               
if afd < today:
  print("April Fool's Day already went by %d days ago" % ((today - afd).day
  afd = afd.replace(year = today.year+1)

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print("It's just ", time_to_afd.days, "days to April Fool's Day")
      
      
                   
