#box
n=int(input('Enter A Number ---------->: '))
for x in range (n):
    for y in range (n):
        if x == n-1 or x == 0 or y == n-1 or y == 0:
            print('*',end = ' ')
        else:
            print(' ', end = ' ')
    print()