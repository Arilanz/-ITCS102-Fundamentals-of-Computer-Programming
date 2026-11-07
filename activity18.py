# bool variables
kaya = True
while kaya == True:
    ask = input('Kaya paba? (yes/no): ')
    if ask.lower() == 'yes':
        print(' GO GO GO GO!')
        continue
    else:
        print('Pahinge muna ikaw!')
        break