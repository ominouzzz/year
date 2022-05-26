from random import randint

print('В 16 этажном доме есть 2 лифта. Прога определяет, какой из 2 лифтов поедет к тебе при вызове с указанного '
      'тобой этажа')

while True:
    your_floor = int(input('С какого этажа ты вызываешь лифт? Введи число в интервале от 1 до 16:'))
    if 1 <= your_floor <= 16:
        break
    else:
        print('Введен некорректный этаж!')

elevator1_floor = randint(1,16)
elevator2_floor = randint(1,16)
print('Лифт 1 сейчас на',elevator1_floor,'этаже', '\nЛифт 2 сейчас на',elevator2_floor,'этаже')

elevators_state = {'Лифт 1':abs(elevator1_floor - your_floor), 'Лифт 2':abs(elevator2_floor - your_floor)}
what_elevator_coming = min(elevators_state, key=elevators_state.get)
print('К тебе едет',what_elevator_coming)
