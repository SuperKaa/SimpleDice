import random
import time

print("Very Cool Dice")

time.sleep(1.5)

while True:
    num = random.randint(1,6)
    print(num)
    q = input("again? y/n ==>")
    if q == "n":
        print("Bye")
        break
    
