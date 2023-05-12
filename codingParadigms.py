# *! To check: python3 codingParadigms.py 

# Activity: (Reflecting On Coding Paradigms)

# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm

# Remember when writing in a functional style:
# 1. Keep variables immutable (use tuples instead of lists)
# 2. Write only pure functions 
# 3. Functions may be higher order 

def flattenAndSort(array):
    # Initialising an empty list to store the flattened array 
    arr = []
    # Use a for loop to iterate through the array 
    for item in array: 
        # If the item is a list, then recursively call the function 
        if isinstance(item, list):
            arr += flattenAndSort(item)
        # Otherwise, append the item to the list 
        else:
            arr.append(item)
    return sorted(arr) 

# Test Cases 
test = [[3, 2, 1], [7, 9, 8], [6, 4, 5]] 
res = flattenAndSort(test) 
print(res) # Output should be [1, 2, 3, 4, 5, 6, 7, 8, 9] 

# Test Cases 2
test2 = [[1, 3, 5], [100], [2, 4, 6]] 
res2 = flattenAndSort(test2)
print(res2) # Output should be [1, 2, 3, 4, 5, 6, 100] 

# Test Cases 3
test3 = [["a", "c", "e"], ["b", "z", "f"], ["g", "i", "h"]] 
res3 = flattenAndSort(test3)
print(res3) # Output should be ["a", "b", "c", "e", "f", "g", "h", "i", "z"]


# First a general Racer class defined with the attributes of max_speed, condition and price
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition # (perfect, trashed, repaired)
        self.price = price

    # Defining a repair() method that will update the condition of the podracer to "repaired"   
    def repair(self):
        self.condition = "repaired"


# Defining a new class that inherits attributes and methods from the Podracer class using super() 
class wandaPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    # A special method called boost() that will double the max_speed of the podracer by multiplying it by 2
    def boost(self):
        self.max_speed *= 2     


# Defining another class that will inherit Podracer attributes and methods 
class spacePod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)

    # A special method called flame_jet() that will update the condition of the podracer to "trashed" 
    def flame_jet(self, other):
        other.condition = "trashed"  # other is the instance of the wandaPod class 


# Testing the classes 
# Creating an instance of wandaPod class 
wanda_pod = wandaPod(max_speed=100, condition="perfect", price=1000) 

# Creating an instance of spacePod class
space_pod = spacePod(max_speed=85, condition="perfect", price=700)


# Calling the boost() method on the wanda_pod instance 
wanda_pod.boost()
print(f"Wanda has used his boost and now has a max speed of {wanda_pod.max_speed} mph") # Output should be 200 mph


# Calling the flame_jet() method on the space_pod instance , in this we will trash wandas pod 
space_pod.flame_jet(wanda_pod) 
print(f"Space Pod {wanda_pod.condition} Wanda's Pod ! ") # Output should be "trashed"

# Calling the repair() method on the wanda_pod instance 
wanda_pod.repair()
print(f"Wanda's Pod Racer is now {wanda_pod.condition}") # Output should be repaired 

# How does this solution demonstrate the four pillars of OOP? 

# Encapsulation: The classes are defined with attributes and methods that are encapsulated within the class because they are only accessible through the class 

# Abstraction: The classes are defined with attributes and methods that are abstracted from the user and are only accessible through the class

# Inheritance: The wandaPod and spacePod classes inherit attributes and methods from the Podracer class

# Polymorphism: The wandaPod and spacePod classes inherit attributes and methods from the Podracer class but also have their own unique methods (boost() and flame_jet()) that are specific to their class !





