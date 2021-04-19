from main import *
from time import time
from random import choice

stone = int(input('Введите количество камней: '))

stones = stone_combo(stone)
game = []

def get_tactics(game, fstart):
    tactics = []
    bad_tactics = []
    for i in stones:
        if fstart == 1:
            if len(game) != 0:
                if i[:len(game)] == game:
                    if len(i) % 2 != 0:
                        tactics.append(i)
                    else:
                        bad_tactics.append(i)
            else:
                if len(i) % 2 != 0:
                    tactics.append(i)
                else:
                    bad_tactics.append(i)
        else:
            if i[:len(game)] == game:
                if len(i) % 2 == 0:
                    tactics.append(i)
                else:
                    bad_tactics.append(i)
                
    if len(tactics) != 0:
        return sorted(tactics, key=lambda x: len(x))
        
    return sorted(bad_tactics, key=lambda x: len(x))
    
start = choice([0, 1])
fstart = start
    
while True:
    if start == 0:
        you = int(input('Выберите число [1,3,4]: '))
        if you not in [1,3,4]:
            print('Неправильный ввод!')
            continue
        elif sum(game) > stone:
            print('Слишком большое число!')
            continue
        else:
            game.append(you)
            if sum(game) == stone:
                break
            start = 1
            
    elif start == 1:
        tactics = get_tactics(game, fstart)
        opponent_choice = tactics[0][len(game)]
        game.append(opponent_choice)
        print('Оппонент выбрал:', opponent_choice)
        if sum(game) == stone:
            break
        start = 0
        
if start == 0:
    print('Ты победил!')
else:
    print('Компьютер победил!')