#left arrowhead

for x in range(7):
    for y in range(4):
        if y >= 3 - x and y >= x - 3 :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#timestable

n=0
for x in range (1,6):
    for y in range (1,6):
        print(x * y,end =' ') 
    print('')