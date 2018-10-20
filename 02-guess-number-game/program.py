import random

print('--------------------------------------------------')
print('             GUESS THAT NUMBER GAME')
print('--------------------------------------------------')
print()

the_number = random.randint(0, 100)

name = input('Welcome, player. What is your name? ')

guess = None

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess > the_number:
        print('Sorry, {1}, your guess of {0} is TOO HIGH!'.format(guess, name))
    elif guess < the_number:
        print('Sorry, {}, your guess of {} is TOO LOW!'.format(name, guess))
    else:
        print('Excellent work, {}! Your guess of {} is correct. YOU WIN!'.format(name, guess))

print('\nEND')
