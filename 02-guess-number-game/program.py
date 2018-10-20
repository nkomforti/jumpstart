import random

print('--------------------------------------------------')
print('             GUESS THAT NUMBER GAME')
print('--------------------------------------------------')
print()

the_number = random.randint(0, 100)

guess = None

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess > the_number:
        print('TOO HIGH!')
    elif guess < the_number:
        print('TOO LOW!')
    else:
        print('YOU WIN!')

print('DONE')