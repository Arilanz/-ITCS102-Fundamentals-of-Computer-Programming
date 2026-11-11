#task 2
for x in range (1,8):
    for y in range(1,14):
        if x == 7 :
            print('*',end= " ")
        elif x + y == 8 or y - x == 6  :
            print('*',end=  " ")
        else:
            print(' ',end=" ")
    print()
print('\n\n\n')
#task 3
for x in range (1,6):
    for y in range(1,6):
        if x == 1 or x == 5 or x + y == 6:
            print('*',end= " ")
        else:
            print(' ',end=" ")
    print()

loan=int(input('Amount to loan----------------> '))
period=int(input('How long you will pay your loan in years--------------------> '))
principal=loan / (period * 12)
interest_rate=0.00256*loan
remaining_loan=loan - principal

print('\n\n')
print(' Month\t\t|Monthly Payment\t\t|Interest\t\t|Principal\t\t|Remaining Loan')
print('-'*120)
for x in range (1,period*12+1):
    for y in range(1,6):
        if y == 1:
            print(x,end='\t\t')
            print('|',end = ' ')
        elif y == 3:
            print(round(interest_rate,2), end='\t\t\t')
            loan=loan- principal
            interest_rate=loan*0.0025
            print('|',end = ' ')
        elif y == 2:
            print(round(interest_rate+principal,2), end='\t\t\t\t')
            print('|',end = ' ')
        elif y == 4:
            print(round(principal,2), end='\t\t\t')
            print('|',end = ' ')
        elif y == 5:
            print(round(remaining_loan,2), end='')
            remaining_loan=remaining_loan-principal

    print()