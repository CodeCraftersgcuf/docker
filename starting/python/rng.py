from random import randint

# Get user input and ensure it's valid
try:
    min_number = int(input('Please enter the min number: '))
    max_number = int(input('Please enter the max number: '))

    # Check if min_number is less than max_number
    if max_number < min_number:
        print('Invalid Input - shutting down...')
    else:
        rnd_number = randint(min_number, max_number)
        print('Random number:', rnd_number)

except ValueError:
    print('Invalid input! Please enter valid integers.')
