# покер на костях
# версия 0.01

from copy import copy
from random import randint as rndint
import combinations as comb


def shake():
    board = [rndint(1, 6) for i in range(5 - len(saveDice))]
    return board


def calc_comb(a):

    temp_comb['pair'] = comb.pair(finishBoard)
    temp_comb['two pairs'] = comb.two_pairs(finishBoard)
    temp_comb['trips'] = comb.trips(finishBoard)
    temp_comb['full house'] = comb.full_house(finishBoard)
    temp_comb['straight'] = comb.straight(finishBoard)
    print('--choose available combination--')
    for keys, values in temp_comb.items():
        if keys in combinations:
            print(keys, values)


def save_score(ch):

    total_score[combinations[ch]] = (temp_comb[combinations[ch]] if temp_comb[combinations[ch]] > 0 else '---')
    print(f'total score - {total_score}')
    combinations.pop(choose)


combinations = ['pair', 'two pairs', 'trips', 'full house', 'straight']

temp_comb = {'pair': 0,
             'two pairs': 0,
             'trips': 0,
             'full house': 0,
             'straight': 0
             }
total_score = {'pair': 0,
               'two pairs': 0,
               'trips': 0,
               'full house': 0,
               'straight': 0
               }

for i in range(5):
    saveDice = []
    board = shake()
    print('--start board--')
    print(board)
    for k in range(2):
        print('--select numbers of dice you want save. if nothing to save press enter--')
        choose = [int(i) for i in input().split()]
        for i in choose:
            saveDice.append(board[i - 1])

        print(f'save dice - {saveDice}')
        board = shake()
        print(f'new board - {board}')
    finishBoard = saveDice + board
    print(f'finish board {finishBoard}')

    calc_comb(finishBoard)
    choose = int(input())-1
    save_score(choose)
print('-----------')
print('-----------')
summary=0
for value in total_score.values():
    if isinstance(value, int):
        summary +=value

print(total_score)
print(f'summary score - {summary}')


