from random import randint


def move(a):
    if a == 0:
        b = 'стоит'
    else:
        b = 'двигается'
    return b


def updown(a):
    if a == 0:
        b = 'вниз'
    else:
        b = 'вверх'
    return b


print('В 16 этажном доме есть 2 лифта. Прога определяет, какой из 2 лифтов поедет к тебе при вызове с указанного '
      'тобой этажа')

while True:
    your_floor = int(input('С какого этажа ты вызываешь лифт? Введи число в интервале от 1 до 16:'))
    if 1 <= your_floor <= 16:
        break
    else:
        print('Введен некорректный этаж!')

# определяем состояние лифтов

elevator1_move = randint(0, 1)  # 0 - стоит, 1 - двигается
elevator2_move = randint(0, 1)
elevator1_floor = randint(1, 16)  # этаж на котором находится лифт
elevator2_floor = randint(1, 16)
if elevator1_move == 1:
    elevator1_move_vector = randint(0, 1)  # 0 - едет вниз, 1 - едет вверх
if elevator2_move == 1:
    elevator2_move_vector = randint(0, 1)

print('Лифт 1 сейчас', move(elevator1_move), 'на', elevator1_floor, 'этаже')
if elevator1_move == 1:
    print('Лифт 1 едет', updown(elevator1_move_vector))

print('Лифт 2 сейчас', move(elevator2_move), 'на', elevator2_floor, 'этаже')
if elevator2_move == 1:
    print('Лифт 2 едет', updown(elevator2_move_vector))

if elevator1_move == 0 and elevator2_move == 0:  # оба лифта стоят
    elevators_state = {'Лифт 1': abs(elevator1_floor - your_floor), 'Лифт 2': abs(elevator2_floor - your_floor)}
    what_elevator_coming = min(elevators_state, key=elevators_state.get)
    print('К тебе едет', what_elevator_coming)

elif elevator1_move == 1 and elevator2_move == 0:  # Лифт 1 едет, Лифт 2 стоит
    if elevator1_move_vector == 1:  # и лифт 1 едет вверх
        print('К тебе едет Лифт 2')
    else:
        if your_floor <= elevator1_floor:  # лифт 1 едет вниз с этажа выше твоего
            print('К тебе едет Лифт 1')
        else:  # лифт 1 едет ввниз с этажа ниже твоего
            print('К тебе едет Лифт 2')

elif elevator1_move == 0 and elevator2_move == 1:  # Лифт 1 стоит, Лифт 2 едет
    if elevator2_move_vector == 1:  # и лифт 2 едет вверх
        print('К тебе едет Лифт 1')
    else:
        if your_floor <= elevator2_floor:  # лифт 2 едет вниз с этажа выше твоего
            print('К тебе едет Лифт 2')
        else:  # лифт 2 едет ввниз с этажа ниже твоего
            print('К тебе едет Лифт 1')

elif elevator1_move == 1 and elevator2_move == 1:  # оба лифта едут
    if elevator1_move_vector and elevator2_move_vector == 1:  # оба едут вверх
        print('К тебе приедет Лифт 1, после того, как освободится')
    elif elevator1_move_vector == 1 and elevator2_move_vector == 0:  # 1 вверх, 2 вниз
        print('К тебе едет Лифт 2')
    elif elevator1_move_vector == 0 and elevator2_move_vector == 1:  # 1 вниз, 2 вверх
        print('К тебе едет Лифт 1')
    else:  # оба едут вниз
        if your_floor <= elevator1_floor and your_floor <= elevator2_floor:  # лифт 1 и 2 едут вниз с этажа выше твоего
            elevators_state = {'Лифт 1': abs(elevator1_floor - your_floor), 'Лифт 2': abs(elevator2_floor - your_floor)}
            what_elevator_coming = min(elevators_state, key=elevators_state.get)
            print('К тебе едет', what_elevator_coming)
        elif your_floor <= elevator1_floor and your_floor > elevator2_floor:  # лифт 1 едет вниз с этажа выше твоего
            print('К тебе едет Лифт 1')
        else:  # лифт 2 едет вниз с этажа выше твоего
            print('К тебе едет Лифт 2')
