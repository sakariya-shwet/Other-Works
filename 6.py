print("1. Student marks → calculate total & average")
print("2. Bill generator (price + tax)")
print("3. Age calculator (current year - birth year)") 
print("4. Even/Odd + positive/negative check ")

choice=input("Enter your choice number:-")

if choice=="1":

     a=int(input("Enter the first number:-"))
     b=int(input("Enter the second number:-"))

print("Addition :- ", a + b)
print("Subtraction :- ", a - b)
print("Division :- ", a / b)
print("Multiplication:- ", a * b)
print("Modulus :- ", a%b)
print("Expontiation :- ", a**b)
print("Floor Division :- ", a//b)

elif choice=="2":

Price=int(input("Enter your bill amount:-"))
tax=int(input("Enter the tax % :-"))

Bill=Price+(Price*tax)/100
print("your total bill is",Bill)

elif choice=="3":

a=int(input("Enter the current year"))
b=int(input("Enter your birth year"))

print("your age is:- ", a - b)

elif choice=="4":

    a=int(input("Enter a number"))

if a % 2==0:

print("Even number")

else:
    print("Odd number")

if a>0:
    print("positive number")
elif a<0:
    print("Negative number")
else:
    print("Zero")

    
    



                    





