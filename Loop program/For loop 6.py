# find largest number in a list

a=input("Enter first number:-")
b=input("Enter second number:-")

number=[a,b]
largest=number[0] 

for num in number:
  if num>largest:
   largest=num
print("Largest",largest)

