#validate input (age>18 and city== "surat"
age = int(input("Enter your age"))
city = (input("Enter your city"))

valid_city = "surat"

if age>18 and valid_city==city:

    print("Approved")
else:
    print("not approved")
