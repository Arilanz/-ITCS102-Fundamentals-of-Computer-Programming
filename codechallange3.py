#Code Challange
a='yes'
c='yes'
z='yes'

print('\t\t=======================INFORMATION=====================')
l=input('\t\tSender name: ')
p=input('\t\tType of item: ')
k=input('\t\tType of Item is it fragile,yes or no: ')
b=input('\t\tDo you need it express{rush},yes or no: ')
inter=input('\t\tIs the location international,yes or no: ')
kg=float(input('\t\tWeight Of The Item In KG: '))
dis=float(input('\t\tThe distance to deliever the item in km: '))

BASE_COST=kg*2.5 + dis*0.15

if a == b and c == inter :
	print('\t\t======INTERNATONAL AND EXPRESS======')
	print('\n\t\t======DETAILS======')
	print('\n\t\tNAME: ',l,)
	print('\t\tITEM: ',p,)
	print('\t\tEXPRESS: ',a == b,)
	print('\t\tFRAGILE: ',k == z,)
	print('\t\tINTERNATIONAL: ',c == inter,)
	print('\n\t\t======PAYMENT======')
	print('\t\tAMOUNT TO PAY:₱',BASE_COST*1.40+50,)
	
elif a != b and c != inter and kg <= 2 and dis <= 100 :
	print('\t\t======FREE SHIPPING======')
	print('\n\t\t======DETAILS======')
	print('\n\t\tNAME: ',l,)
	print('\t\tITEM: ',p,)
	print('\t\tFRAGILE: ',k == z,)
	print('\t\tEXPRESS: ',a == b,)
	print('\t\tINTERNATIONAL: ',c == inter,)
	print('\n\t\t======PAYMENT======')

	print('\t\tAMOUNT TO PAY:₱ 0.00')
	
elif a == b or c == inter and kg > 20:
	print('\t\t======INTERNATONAL OR EXPRESS{HEAVY ITEM}======')
	print('\n\t\t======DETAILS======')
	print('\n\t\tNAME: ',l,)
	print('\t\tITEM: ',p,)
	print('\t\tFRAGILE: ',k == z,)
	print('\t\tEXPRESS: ',a == b,)
	print('\t\tINTERNATIONAL: ',c == inter,)
	print('\n\t\t======PAYMENT======')
	
	print('\t\tAMOUNT TO PAY:₱',BASE_COST*1.20+25,)
elif kg > 30 or  dis > 1000:
	print('\t\t======OVERSIZED ITEM======')
	print('\n\t\t======DETAILS======')
	print('\n\t\tNAME: ',l,)
	print('\t\tITEM: ',p,)
	print('\t\tFRAGILE: ',k == z,)
	print('\t\tEXPRESS: ',a == b,)
	print('\t\tINTERNATIONAL: ',c == inter,)
	print('\n\t\t======PAYMENT======')

	print('\t\tAMOUNT TO PAY:₱',BASE_COST+30,)
else:
	print('\t\t======STANDARD RATE======')
	print('\n\t\t======DETAILS======')
	print('\n\t\tNAME: ',l,)
	print('\t\tITEM: ',p,)
	print('\t\tFRAGILE: ',k == z,)
	print('\t\tEXPRESS: ',a == b,)
	print('\t\tINTERNATIONAL: ',c == inter,)
	print('\n\t\t======PAYMENT======')

	print('\t\tSTANDARD RATE:₱',BASE_COST,)
