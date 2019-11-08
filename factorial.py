# Assignment - Factorial
# Dan Ochs     11/8/2019
#
# compute factorial of a given number
# (non-recursive implementation)

# clear the terminal
from os import system
system('clear') 

# banner and get input from user
print("Factorial Calculator")
while True:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a positive whole number.")
        continue
    else:
        if n<=0:
            print("Please enter a positive whole number.")
            continue
        else:
            break

fact = 1
for i in range(1,n+1):
    fact = fact * i

print(f"{n}! = {fact}")
