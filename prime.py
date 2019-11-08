# Assignment - Prime
# Dan Ochs     11/8/2019
#
# check if a number is prime or not

# clear the terminal
from os import system
system('clear') 

# banner and get input from user
print("Prime Number Check")
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

is_prime = True

# exhaustive check
#if n!=1:     # 1 is prime, don't bother with loop
#    for i in range(2,n):
#        if (n%i)==0:
#            is_prime = False

# as soon as find a factor stop
i = 2
while is_prime and (i<n):
    if (n%i)==0:
        is_prime = False
    i = i + 1 

# output result to terminal 
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

