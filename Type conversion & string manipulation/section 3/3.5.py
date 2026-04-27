# Check if string is palindrome
a = input("Enter a number: ")

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
