#basic if else program

print('==========================REGISTRATION=============================')
u=input('ENTER A USERNAME: ')
p=input('ENTER A PASSSWORD: ')
print('YOU SUCCESSFULLY CREATED AN ACCOUNT,PLEAS LOGIN IT BELOW')
print('\t\t\t||\n\t\t\t||\n\t\t\t||\n\t\t\t||\n\t\t\t\\/')
print('==========================LOGIN====================================')
username=input('ENTER A USERNAME: ')
password=input('ENTER A PASSSWORD: ')

if u == username and p == password:
	print('The username and password is correct')
	print('YOU SUCCESSFULLY LOGIN,WELCOME TO ENJOY!')
else:
	print('The username or password is incorrect')
	print('ACCESS DENIED, CHECK YOUR PASSWORD OR USERNAME IF ITS CORRECT')