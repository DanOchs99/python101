# Assignment - Calculator
# Dan Ochs     11/7/2019
#
# get three inputs from user:
# first number, operand (+,-,*,/), second number
# based on the operand perform the math and print result
# to the terminal
#
def plus(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

print("Four function calculator")
n1 = float(input("Input a number: "))
op = input("Provide an operand (+,-,*,/): ")
n2 = float(input("Input a second number: "))

op_ok = True
if op == '+':
    output = plus(n1,n2)
elif op == '-':
    output = sub(n1,n2)
elif op == '*':
    output = mult(n1,n2)
elif op == '/':
    output = div(n1,n2)
else:
    print("I don't know how to do that.")
    op_ok = False

if op_ok:
    print(f"The answer is: {output}")

