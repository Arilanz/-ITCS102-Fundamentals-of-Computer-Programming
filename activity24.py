from activity23 import factorial_ko_ito
from activity23 import agelimit
from activity23 import ekis
import os

while True:

    print("\nSELECT AN OPTION")
    print("1 - Factorial")
    print("2 - Age Limit")
    print("3 - Ekis Pattern")
    print("4 - Exit")

    pili = int(input("Enter your choice ---> "))

    if pili == 1:
        os.system('cls')
        print("FACTORIAL")
        num = int(input("Enter a num ---> "))
        print("Output:", factorial_ko_ito(num))
        continue

    elif pili == 2:
        os.system('cls')
        print("AGE LIMIT")
        age = int(input("Enter your age ---> "))
        print("Output:", agelimit(age))
        continue

    elif pili == 3:
        os.system('cls')
        print("EKIS PATTERN")
        num = int(input("Enter a num ---> "))
        ekis(num)
        continue

    elif pili == 4:
        os.system('cls')
        print("SYSTEM EXIT")
        break

    else:
        os.system('cls')
        print("INVALID CHOICE")
        continue