# CHECK PALINDROME

a=int(input("Enter a number"))
orignal=0
rev=0

while a >0:
    digit = a % 10
    rev=rev*10+digit
    a=a//10
if orignal ==rev:
        print("It's palindrome")
else:
         print("It's not palindrome")
