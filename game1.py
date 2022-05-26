from random import randint

print('Игра Отгадай число. Я загадываю число от 1 до 100, а ты пытаешься угадать его. '
      'На каждый твой ответ я буду говорить больше оно или меньше загаданного числа.')

hidden_number = randint(1,100)

print('Итак, я загадал число. Попробуй угадать')

while True:
    user_number = int(input('Введи число в интервале от 1 до 100:'))
    if 1 <= user_number <= 100:
        if user_number < hidden_number:
            print('Твое число', user_number, 'меньше загаданного. Попробуй угадать снова!')
        elif user_number > hidden_number:
            print('Твое число', user_number, 'больше загаданного. Попробуй угадать снова!')
        else:
            print('Ты угадал! Загаданное число:', hidden_number)
            break
    else:
        print('Ты ввел некорректное число!')


