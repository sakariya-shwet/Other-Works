# check palindrome number

a=input("Enter a number")
rev=""

for i in a:
    rev=i+rev
if a==rev:
     print("yes the number is palindrome")

else:
    print("Number is'nt palindrome")
