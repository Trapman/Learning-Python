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
  
 # OS PATH ###################################################
#Brittany is using the OS path utilities functions to find out information on her system. How can she find out which operating system is imported into Python and print out the current working directory?

import os
  print(os.name)
  print(os.getcwd())

# READ AND WRITE #############################################
# Carissa needs to implement reading and writing files in her Python code. Based on the information given, how do you read the breeders_for_cats.txt file that prints out the file to the console?

with open('breeders_for_cats.txt', 'r') as reader:
  print(reader.read())  

# JSON ###################################################################
# William is tasked with creating JSON functionality with Python code. What code can he create that reads in JSON data and prints it to the console?

import urllib.request
 def main():
    someUrlData = "http://somerandomJSONdata
    webUrl = urllib.request.urlopen(someUrlData)
    print("result number: " +str(webUrl.getcode()))
    if (webUrl.getcode() == 100):
       json_data = webUrl.read()      printResults(json_data)
    else:
       print("No JSON data received, ERROR!) 
             
# PARSING ############################################################################
# How can you fetch internet data in Python that reads in 200 results from the Bing search engine and prints it out on the display console?

import urllib.request
def main();
   webUrl = urllib.request.urlopen("http://www.bing.com")
   bing_search_results = webUrl.read()
print(bing_search_results)             
             
             
             
