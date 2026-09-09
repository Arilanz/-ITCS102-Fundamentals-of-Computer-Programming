#multiple if and elif conditions

#Create a python program that would capture age group
print('======================Age Group Identifier==============')

name= input('Enter your Name: ')
age=int(input('Enter your Age: '))

if age >=0 and age <=5:
	print('The age is condsidered as INFANT')
	print('\t{AGE IS NOT VALID}')

elif age >=6 and age <=12:
	print('The age is condsidered as CHILD')
	print('\t{AGE IS NOT VALID}')

elif age >=13 and age <=15:
	print('The age is condsidered as PRE TEEN')
	print('\t{AGE IS NOT VALID}')

elif age >=16 and age <=19:
	print('The age is condsidered as TEENAGER')
	print('\t{AGE IS VALID}')

elif age >=20 and age <=29:
	print('The age is condsidered as EARLY ADULT')
	print('\t{AGE IS VALID}')

elif age >=30 and age <=58:
	print('The age is condsidered as ADULT')
	print('\t{AGE IS VALID}')

if age >=59 and age <=150:
	print('The age is condsidered as ADULT')
	print('\t{AGE IS VALID}')

else:
	print('\tTHANK YOU FOR ANSWERING')

