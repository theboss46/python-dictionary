weight = int(input('Weight: '))
Lbs_or_Kg = input('(L)bs or (K)g: ')

if Lbs_or_Kg.upper == 'L':
    converted = weight / 2.2
    print(f'You are {converted} kilograms')

else:
    converted = weight * 2.2
    print(f'You are {converted} pounds')
