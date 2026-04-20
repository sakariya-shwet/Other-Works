#check leap year

year=int(input("Enter a leap year:-"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("yes, this a leap year")
else:
    print("this is no laep year")
