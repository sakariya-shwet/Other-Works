# guess the number game

import random

secret=random.randint(1,5)
count=0

while True:
    ans= int(input("guess:"))
    if ans==secret:
        break
print("Correct ")
