#Code Challange

print('=======================INFORMATION=====================')
input('Sender name: ')
input('Type of item: ')
k=input('Type of Item is it fragile,yes or no: ')
b=bool(input('Do you need it express{rush},yes or no: ')) == 'yes'
kg=float(input('Weight Of The Item In KG: '))
inter=bool(input('Is the location international,yes or no: ')) == 'yes'
dis=float(input('The distance to deliever the item in km: '))

BASE_COST=kg*2.5 + dis*0.15
print('=====================AMOUNT=====================')
if b == 'yes' and inter == 'yes' and k == d:
	print('AMOUNT TO PAY:₱',BASE_COST*1.40+50,)
	print('THE ITEM DETAILS')

elif b != 'no' and inter != 'no' and kg <= 2 and dis <= 100:
	print('AMOUNT TO PAY:₱ 0.00')
	print('THE SHIPPING IS FREE')
elif b == 'yes' or inter == 'yes' and kg > 20:
	print('AMOUNT TO PAY:₱',BASE_COST*1.20+25,)
elif kg > 30 or  dis > 1000:
	print('AMOUNT TO PAY:₱',BASE_COST+30,)
else:
	print('STANDARD RATE:₱',BASE_COST,)
