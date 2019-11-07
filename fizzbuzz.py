# Assignment - Fizz Buzz
# Dan Ochs     11/7/2019
#
# ask user for input
# if input is divisible by 3 print "Fizz"
# if input is divisible by 5 print "Buzz"
# if input is divisible by 3 and 5 print "Fizz Buzz"

# get input from user
while True:
    try: 
        n = int(input("Enter a whole number: "))
    except ValueError:
        print("A whole number was expected.")
        continue
    else:
        break

# check for divisibility and display appropriate message if
# one of the conditions is met
if ((n%3)==0) and ((n%5)==0):
    print("Fizz Buzz")
elif (n%3)==0:
    print("Fizz")
elif (n%5)==0:
    print("Buzz")

