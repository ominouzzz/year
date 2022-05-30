from random import randint


def game(number_of_attempts):
    hidden_number = randint(1, 100)
    print('Итак, я загадал число. Попробуй угадать')
    attempt_counter = 0
    while attempt_counter < number_of_attempts:
        print('Число попыток:', number_of_attempts - attempt_counter)
        user_number = int(input('Введи число в интервале от 1 до 100:'))
        if 1 <= user_number <= 100:
            attempt_counter += 1
            if user_number < hidden_number:
                print('Твое число', user_number, 'меньше загаданного.')
            elif user_number > hidden_number:
                print('Твое число', user_number, 'больше загаданного.')
            else:
                print('Ты угадал! Загаданное число:', hidden_number)
                break
            if attempt_counter == number_of_attempts:
                print('Ты проиграл!')
        else:
            print('Ты ввел некорректное число!')


print('Игра Отгадай число. Я загадываю число от 1 до 100, а ты пытаешься угадать его. '
      'На каждый твой ответ я буду говорить больше оно или меньше загаданного числа.')

while True:
    game_level = int(input('Выбери уровень сложности. Введи от 1 (легкий) до 3(тяжелый):'))
    if 1 <= game_level <= 3:
        break
    else:
        print('Введен некорректный уровень!')

game_number_of_attempts = 8 // game_level

game(game_number_of_attempts)
