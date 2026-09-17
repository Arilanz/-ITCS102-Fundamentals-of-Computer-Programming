#activity 13
print(('========================================================================='))
name=input('FIRST NAME OF LOAN APPLICANT: ')
age=int(input('YOUR AGE: '))
employed=bool(input('ARE YOU EMPLOYED: {IF YES ANSWER true if not press enter only}: '))
income=eval(input('YOUR ANNUAL INCOME: '))
credit=eval(input('CREDIT SCORE HISTORY: '))
collateral=bool(input('DO YOU HAVE COLLATERAL: {IF YES ANSWER true if press enter only}: '))
if  age >= 21 and age <= 65 and employed == True :
    if credit >= 750 :
        if income >= 100000:
            print('=========================================================================')
            print('YOU ARE ELIGABLE>_>')
            print('INTEREST: 4.5%')
        else:
            print('=========================================================================')
            print('YOU ARE ELIGABLE>_>')
            print('INTEREST: 5.0%')         
    elif 600 <= credit < 750:
        if collateral == True :
            print('=========================================================================')
            print('YOU ARE ELIGABLE>_>')
            print('INTEREST: 7.0%')
        elif income < 40000:
            print('=========================================================================')
            print('YOU ARE ELIGABLE>_>')
            print('INTEREST: 9.5%')
        else:
            print('=========================================================================') 
            print('YOU ARE ELIGABLE>_>')
            print('INTEREST: 8.0%')
    elif credit < 600:
        print('=========================================================================')
        print('YOU ARE NOT ELIGIBLE {Credit score too low} ')
        print('SORRY........')
else:
    print('=========================================================================')
    print('YOU ARE NOT ELIGIBLE {AGE OR EMPLOYMENT CRITERIA NOT MET}')
    print('SORRY........')
