print("Welcome to the Tip Calculator")

bill = float(input("What was the total of the bill? "))
people = int(input("How many people are paying? "))
tip = float(input("How much are you tipping? 10%, 15%, 20% ")) 
tip_percent = (tip / 100) + 1

pay = round((bill / people) * tip_percent, 2)

print(f"Each person should pay ${pay}")
