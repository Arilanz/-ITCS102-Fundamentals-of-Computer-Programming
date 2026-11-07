from getpass import getpass
login = False
attempts= 0

u= input('Enter your username: ')
p=input('Enter your password: ')

print('=====================')
while login == False:
    uname= input('Enter your username :')
    passwd= getpass('Enter your passwrod: ')
    if uname == u and passwd == p:
        print('Login Successful!')
        print('Attempts: ',attempts)
        login = True
    else:
        print('Incorrect username or password. Please Try Again')
        attempts += 1
        login = False
