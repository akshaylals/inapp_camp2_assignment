# Assignment 3
# Make a two-player Rock-Paper-Scissors game. One of the
# players is the computer.
# 
# 5 chances. Print out the winner and points earned by both players.
# 
# Remember the rules:
# * Rock beats scissors
# * Scissors beats paper
# * Paper beats rock

from random import randint

opts = ('Rock', 'Paper', 'Scissors')

playerPoint = 0
computerPoint = 0


def getRes(p1, p2):
    #  1 - p1 scores
    # -1 - p2 scores
    #  0 - draw 
    if p1 == p2:
        return 0
    else:
        match (p1, p2):
            case (1, 2): return -1
            case (1, 3): return 1
            case (2, 1): return 1
            case (2, 3): return -1
            case (3, 1): return -1
            case (3, 2): return 1
            

for i in range(5):
    print('''
    1. Rock
    2. Paper
    3. Scissors
    ''')
    while(True):
        playerInput = int(input('> '))
        if(1 <= playerInput <= 3):
            break
        else:
            print('invalid input')
    computer = randint(1, 3)

    print(f'Computer: {opts[computer - 1]}')
    print(f'Player: {opts[playerInput - 1]}')

    res = getRes(computer, playerInput)
    if res > 0:
        computerPoint += 1
        print('Computer scores')
    elif res < 0:
        playerPoint += 1
        print('Player scores')
    else:
        print('Draw')
    

if playerPoint > computerPoint:
    print('Player wins')
elif playerPoint < computerPoint:
    print('Computer wins')
else:
    print('Draw')
