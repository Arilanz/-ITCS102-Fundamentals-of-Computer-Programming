num=int(input("Enter a num --->"))

def factorial_ko_ito(tamang_sagot):
    fact= 1
    for x in range (tamang_sagot,0,-1):
       fact *= x
    return fact

print("output",factorial_ko_ito(num))

age=int(input("Enter your age --->"))

def agelimit(eded):
    if age >= 18:
        return("Pwede Ka")
    else:
        return("bwal ka, patuli muna")
        

print("output",agelimit(age))


def ekis(num):
    for x in range(num+1):
        for y in range(num+1):
            if x == y or x + y == num:
                print('*', end='')
            else:
                print(' ', end='')
        print()

ekis(4)
