# Starter Code
import random

name_string = input("Enter the names of everyone, separated by a comma. \n")
names = name_string.split(", ")


# Write your code below!
print(names[random.randint(0, len(names) - 1)] + " will pay for dinner today!")
