#activity 13
#basic if else program
import getpass

print('==========================REGISTRATION=============================')
u=input('ENTER A USERNAME: ')
p=input('ENTER A PASSSWORD: ')
print('YOU SUCCESSFULLY CREATED AN ACCOUNT,PLEASE LOGIN IT BELOW')
print('\t\t\t||\n\t\t\t||\n\t\t\t||\n\t\t\t||\n\t\t\t\\/')
print('==========================LOGIN====================================')
username=input('ENTER A USERNAME: ')
password=getpass.getpass('ENTER A PASSSWORD: ')

if u == username and p == password: 
    print('YOU SUCCESSFULLY LOGGED IN, PLEASE FILL THE FORM BELOW')
    print('==========================LOAN ELIGIBILITY CHECKER=====================')
    name=input('FIRST NAME OF LOAN APPLICANT: ')
    age=int(input('YOUR AGE: '))
    employed=bool(input('ARE YOU EMPLOYED: {IF YES ANSWER true if not press enter only}: '))
    if employed == True:
        job_description=input('JOB DESCRIPTION: ')
        income=eval(input('YOUR ANNUAL INCOME: '))
        credit=eval(input('CREDIT SCORE HISTORY: '))
        collateral=bool(input('DO YOU HAVE COLLATERAL: {IF YES ANSWER true if press enter only}: '))
        type=('DESCRIPTION OF COLLATERAL: {eg. HOUSE, CAR, LAND, ETC}: ')
        if collateral == True:
            money=int(input('VALUE OF COLLATERAL: '))
        else:
            print('NO COLLATERAL, PLEASE PROCEED')
    if  age >= 21 and age <= 65 and employed == True and money >= 30000:
        if credit >= 750 :
            if income >= 100000:
                print('YOU ARE ELIGABLE>_>')
                print('INTEREST: 4.5%')
            else:
                print('YOU ARE ELIGABLE>_>')
                print('INTEREST: 5.0%')
        elif 600 <= credit < 750:
            if collateral == True :
                print('YOU ARE ELIGABLE>_>')
                print('INTEREST: 7.0%')
            elif income < 40000:
                print('YOU ARE ELIGABLE>_>')
                print('INTEREST: 9.5%')
            else:
                print('YOU ARE ELIGABLE>_>')
                print('INTEREST: 8.0%')
        elif credit < 600:
            print('YOU ARE NOT ELIGIBLE {Credit score too low} ')
            print('SORRY........')
    else:
        print('YOU ARE NOT ELIGIBLE {AGE OR EMPLOYMENT CRITERIA NOT MET}')
        print('SORRY........')
else:
	    print('The username or password is incorrect')
print('ACCESS DENIED, CHECK YOUR PASSWORD OR USERNAME IF ITS CORRECT')
