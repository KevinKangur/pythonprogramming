import random

randomnumber = random.randint(0, 101)

guess = -1

while randomnumber != guess:

    guess = int(input('Paku arvu: '))

    if randomnumber > guess:
        print('Paku suurem arv: ')
    elif randomnumber < guess:
        print('Paku väiksem arv: ')
    elif randomnumber == guess:
        print('Õige!')