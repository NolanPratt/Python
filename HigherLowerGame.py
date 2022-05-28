import random

print('Hello and welcome to my game!\n'
      'The rules are simple:\n'
      'You give me a set of bounds, then you guess the number that I choose.')
while True:
    LowerB = int(input('Please enter your lower bound: '))
    HigherB = int(input('Please enter your higher bound: '))
    if LowerB > HigherB:
        print('The bounds you entered are invalid. Please enter new bounds.')
        continue
    num = int(random.randint(LowerB, HigherB))

    while True:
        guess = int(input('Enter your guess: '))
        if (guess < LowerB) or (guess > HigherB):
            print('Invalid guess: not within bounds. Try again.')
            continue
        if guess > num:
            print('Lower')
            continue
        elif guess < num:
            print('Higher')
            continue
        else:
            print('Congratulations! You correctly guessed {}.'.format(num))
            play_check = input('Play again?\n(Y or N): ')
            if play_check != 'Y':
                print('Thank you for playing!')
                exit()
            else:
                break
    continue