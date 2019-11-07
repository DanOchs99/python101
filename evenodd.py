# Assignment - Even Odd
# Dan Ochs     11/7/2019
#
# ask user for input
# display message indicating if input is even or odd

# get input from user
while True:
    try: 
        n = int(input("Enter a whole number: "))
    except ValueError:
        print("A whole number was expected.")
        continue
    else:
        break

# check odd or even and display message
if (n%2)==0:
    print(f"The number {n} is even.")
else:
    print(f"The number {n} is odd.")

