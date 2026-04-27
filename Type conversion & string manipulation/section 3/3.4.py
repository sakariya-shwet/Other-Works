# reverse a string

num=int(input("Enter a number"))
rev=0

while num>0:
    calc=num%10
    rev=rev*10+calc
    num//=10

print("Reversed:",rev)
