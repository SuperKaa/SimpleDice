import random
import time

print("Very Cool Dice")
loop = 1

time.sleep(1.5)

while loop == 1:
    num = random.randint(1,6)
    print(num)
    q = input("again? y/n ==>")
    if q == "n":
        print("Bye")
        loop = 2
    
