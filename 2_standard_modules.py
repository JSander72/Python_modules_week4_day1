from helper import d # best practices: All import should go always go at the top of your file

# in this lecture we will not be using this rule just becauase we are leanring some modules thoughout (outlire) 

import math 

root = math.sqrt(30) # square root 
print(root)

up = math.ceil(root) # round up 
print(up)

down = math.floor(root) # round down
print(down)

# built-in math module provides a wide range of mathematical functions and constants.
# website to modules: 

d()

import datetime as dt # importing module and giving it an aliase to make it easier to type and make your code more effecient 

now = dt.datetime.now() # get current date and time
print(now)

start_time = dt.datetime.now() # testig how fast looping though a list is compared to a tuple 

for _ in list(range(1000000)):
    pass
finished = dt.datetime.now()
print(f"The time it took to loop through 1 million numbers in a list: {finished - start_time}")

my_birthday = dt.date(1981, 7, 7) # takes in verialbes in this spcific order (datee, month, day)
print(f"My Birthday is: {my_birthday}") 

d()

# collections modules: This module implements specialized container fruitstypes providing alternatives to Python’s general purpose built-in containers, dict, list, set, and tuple.

from collections import Counter # you can use this instead of typing code that loops through a list or tuple 

fruits = ["apple", "banana", "apple", "orange", "banana", "banana"]
get_count = Counter(fruits) # creates a dictionary with keys as elements from the list and values as their counts
print(get_count) 

colors = ["red", "blue", "yellow", "black", "black", "blue", "red", "red", "white", "blue"]
color_counts = Counter(colors)
print(color_counts) # counts eaach color anf prints it for you 
print(color_counts["blue"]) #counts at the key of blue

d()







