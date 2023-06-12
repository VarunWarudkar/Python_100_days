#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D

import math
import random
x = 'Y'
while x != 'N':
    x = input("Do you want to play state Y or N :").upper()

    if x == 'N':
        break
    else:
        pChoise = int(input("0.Snake \t 1.Water \t 2.Gun\nPlease enter your choise: \t "))

        cChoise = random.choice([0, 1, 2])

        print(f"Your choise is {pChoise} and Computer's choise is {cChoise}")
        gameMatrix = [
            ['Draw','Win','Loose'],
            ['Loose','Draw','Win'],
            ['Win','Loose','Draw']
        ]
        if gameMatrix[pChoise][cChoise] == 'Draw':
            print(f"The game between you and computer ended in Draw.")
        elif gameMatrix[pChoise][cChoise] == 'Win':
            print(f"The game between you and computer ended in your Win.")
        else:
            print(f"The game between you and computer ended in your Loss.")