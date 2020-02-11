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
