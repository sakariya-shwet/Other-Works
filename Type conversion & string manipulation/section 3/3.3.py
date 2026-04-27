#Count number of vowels in a string
s = "Hello World "
vowels="aeiouAEIOU"
count=0
for char in s:
    if char in vowels:
       count=count+1


print("number of vowels",count) 
