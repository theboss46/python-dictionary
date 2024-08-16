previous = 'stop'
while True:
    instruction = input('>').lower()

    if instruction == 'help':
        print('start - to start the car\nstop - to stop the car\nquit - to exit')

    elif instruction == 'start':
        if previous != 'start':
            print('The car has started...')
        else:
            print('The car has already started!')

    elif instruction == 'stop':
        if previous != 'stop':
            print('The car has been stopped!')
        else:
            print('The car is already stopped!')

    elif instruction == 'quit':
        break

    else:
        print('Invalid instruction')
    previous = instruction
