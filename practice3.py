age = int(input("Please enter your age: "))
cc = int(input("Enter your credit score: "))
rev=int(input("Enter your monthly revenue: "))
defaults= bool(input("Have you ever defaulted on a loan? {if you have enter true if not skip this part}: "))
years=int(input("Years of business operation: "))
collateral= input("Type of collateral: ")
value=int(input("value of collateral: "))
amount=int(input("amount of loan you want: "))

max_limit=0

#tier2 
if age >= 21 and years >= 2 and defaults == False:
    print("You are eligible for a loan")
    if cc >= 720:
        print("Your credit score is excellent")
        if rev >= 50000:
            max_limit = rev * 3
            print("BASE FEE: ", max_limit * 0.015)
        else:
            print("BASE FEE: ",max_limit * 0.025)
        
        if value >= max_limit:
            print("Your collateral is sufficient for the loan")
        else:
            print("Your collateral is not sufficient for the loan")
    
    elif cc <= 620 and cc <720:
        if years >= 5:
            max_limit = rev * 1.5
            print("BASE FEE: ", max_limit * 0.02)
        else:
            print("BASE FEE: ", max_limit * 0.035)
        if value >= max_limit:
            print("Your collateral is sufficient for the loan")
        else:
             print("Your collateral is not sufficient for the loan")
   
    elif cc < 620:
        print("sorry you are not eligible for a loan")
else:
    print("Rejected: You do not meet the minimum requirements for a loan")