#Take user age as string and: 
#○ convert to int 
#○ check if eligible to vote

num_str=input("Enter your age")
num_int=int(num_str)

if num_int >18:
    print("You are eligible")
else:
    print("You are'nt eligible")
