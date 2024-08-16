name = len(input('A name must be between 3 and 50 characters.\nEnter your name: '))

if name < 3 or name > 50:
    print('Your name must be between 3 and 50 characters.')
else:
    print('name looks good')
