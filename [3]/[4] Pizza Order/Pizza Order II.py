# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 0

# Calculate bill functions
def bill(size, pepperoni, cheese):
    global total
    if (size == "S"):
        total += 15
    elif (size == "M"):
        total += 20
    elif (size == "L"):
        total += 25

    if pepperoni == "Y":
        if (size == "S"):
            total += 2

        else:
            total += 3

    if (cheese == "Y"):
        total += 1

# End of code
bill(size, add_pepperoni, extra_cheese)
print(f"Your final bill is: ${total}.")