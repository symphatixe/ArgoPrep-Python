print("Welcome to the Fizz Buzz game, enter a number to test which one it is!")
num = int(input("Enter a number\n"))

if (num % 3 == 0):
    if (num % 5 == 0):
        print(str(num) + " entered, it is FizzBuzz!")
    else:
        print(str(num) + " entered, it is Fizz!")
elif (num % 5 == 0):
    print(str(num) + " entered, it is Buzz!")
else:
    print(str(num) + " entered, neither category!")