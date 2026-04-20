#Discount calculation

price=int(input("Enter the price:-"))
discount=int(input("Enter the discount:-"))

total=(price * discount) / 100
price -= discount
print("Discount :- ", discount)
print("Total:- ", price)

