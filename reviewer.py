age=int(input('ENTER AGE: '))
monthly_income=int(input('MONTHLY INCOME: '))
credit=int(input('ENTER YOUR CREDIT SCORE: '))
years=float(input('YEARS IN BUSINESS: '))
bankcrupcy=bool(input('BANKCRUPT RECORD {IF YOU HAVE ANSWER TRUE IF NOT JUST SKIP THE PART}: '))
collateral=input('TYPE OF COLLATERAL: ')
collateral_value=int(input('COLLATERAL VALUE: '))

max_loan= 0
if age >= 21 and bankcrupcy == False :
    if credit >= 720 :
        max_loan=monthly_income* 3
        print('======SYSTEM======')
        print('MAXLOAN: ',max_loan,)
        if monthly_income > 5000:
            base_rate= 0.015
        else :
            base_rate= 0.035
        if collateral_value >= max_loan:
            print('Sufficient Collateral')
            processingfee= max_loan * base_rate
            if collateral_value % 5000 != 0 :
                print('FEE:',processingfee + 250)
            else:
                print('FEE: ',processingfee,)
        else:
            print('Insufficient Collateral REJECTED!!!')
    elif 620 <= credit < 720:
        max_loan=monthly_income*1.5
        print('======SYSTEM======')
        print('MAXLOAN: ',max_loan,)
        if years >= 5.0 :
            base_rate=0.02
        else:
            base_rate=0.035
        if collateral_value >= max_loan:
            print('Sufficient Collateral')
            processingfee= max_loan * base_rate
            if collateral_value % 5000 != 0 :
                print('FEE:',processingfee + 250)
            else:
                print('FEE: ',processingfee,)
        else:
            print('Insufficient Collateral REJECTED!!!')
    elif credit < 620:
        print('======SYSTEM======')
        print('Credit score below requirement')
else:
    print('The applicant did not meet the requirements')
