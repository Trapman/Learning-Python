# CLASS ##########################################
# In Python, what is the correct way to develop a class called Person that has parameters in the initialize function 
# called name, age, and sex?

class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex   
    
# IF statements ###################################################################
# Sunita is adding conditional structures in Python. 
# What is the correct way to create an if conditional structure that loops 50 times and displays the food called "roast"?

food = 'roast'

if food == 'roast':
    print('Ummmm, my favorite!')
    print('I feel like saying it 50 times...')
    print(50 * (food + '! '))
    
# FUNCTIONS ####################################################################
# Robert is creating a basic function in Python. How should he create a function that displays "This is a basic Python function!"?

def funcBasic(): 
   print("This is a basic Python function!")

# CALENDARS ##################################################
#In Python, what is the correct code format for creating a work calendar with a month that starts on Monday, in June of 2019?


import calendar
cal = calendar.TextCalendar(calendar.Monday)
myCal = cal.formatmonth(2019, 6, 0, 0)
print(myCal)

# TIMEDELTA ##########################################################
#When using the timedelta object in Python, how do you use the max, min, and resolution attributes for timedelta?

print(timedelta.max)
print(timedelta.min)
print(timedelta.resolution)   

# DATE TIME ###########################################################
# Bailey needs to output times in her Python code. How can she display today's date in the main function?

from datetime import date
from datetime import time
from datetime import datetime
def main():
  today = date.today()
  print ("Today's date is", today)  
  
  # 
