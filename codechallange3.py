#Code Challange
a='yes'
c='yes'
d='yes'

print('=======================INFORMATION=====================')
input('Sender name: ')
input('Type of item: ')
k=input('Type of Item is it fragile,yes or no: ')
b=input('Do you need it express{rush},yes or no: ')
kg=float(input('Weight Of The Item In KG: '))
inter=input('Is the location international,yes or no: ')
dis=float(input('The distance to deliever the item in km: '))

BASE_COST=kg*2.5 + dis*0.15
print('=====================AMOUNT=====================')
if a == b and c == inter and k == d:
	print('AMOUNT TO PAY:₱',BASE_COST*1.40+50,)
	print('THE ITEM DETAILS')

elif a != b and c != inter and kg <= 2 and dis <= 100:
	print('AMOUNT TO PAY:₱ 0.00')
	print('THE SHIPPING IS FREE')
elif a == b or c == inter and kg > 20:
	print('AMOUNT TO PAY:₱',BASE_COST*1.20+25,)
elif kg > 30 or  dis > 1000:
	print('AMOUNT TO PAY:₱',BASE_COST+30,)
else:
	print('STANDARD RATE:₱',BASE_COST,)
