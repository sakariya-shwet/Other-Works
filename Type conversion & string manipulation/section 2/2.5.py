# Take price as float and: 
#● convert to int 
#● display rounded value 


price_input=input("Enter the price")
price_num=float(price_input)
price_int=int(price_num)


price_rounded=round(price_num)

print("integer value:",price_int)
print("rounded value:",price_rounded)

