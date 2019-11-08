# Assignment - Palindrome
# Dan Ochs     11/8/2019
#
# check if an input word is a palindrome or not
# palindromes are same in forward or reverse order

from os import system
system('clear') 

# get input from user
print("Palindrome Checker")
word = input("Please input a word to check: ").lower()

# version 1 reverse string and compare
#rev = ""
#for i in range(len(word)-1,-1,-1):
#    rev = rev + word[i]
#if word==rev:
#    print(f"{word} is a palindrome.")
#else:
#    print(f"{word} is not a palindrome.")

is_a_palindrome = True
# version 2 check in place
#for i in range(len(word)):
#    if word[i]!=word[len(word)-(i+1)]:
#      is_a_palindrome = False

# better - but v2 runs in O(n), could make it faster...
# version 3 check in place but stop as soon as test fails
i = 0
while is_a_palindrome and (i<len(word)):
    if word[i]!=word[len(word)-(i+1)]:
      is_a_palindrome = False
    i += 1

# output result of check to user    
if is_a_palindrome:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")    

# version 4
# even simpler version using slices
#if word == word[::-1]:    # reverse slice notation
#    print(f"{word} is a palindrome.")
#else:
#    print(f"{word} is not a palindrome.")
