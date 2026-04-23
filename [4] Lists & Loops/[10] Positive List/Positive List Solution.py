# Starter Code
import random

positive_list = []
negative_list = []


# Write your code below!


for _ in range(35):
    number = random.randint(-20, 20)

    if (number >= 0): positive_list.append(number)
    else: negative_list.append(number)

print(f"Positive list: {positive_list}")
print(f"Negative list: {negative_list}")