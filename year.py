import datetime

current_year = datetime.datetime.now().year
print('Прога определяет сколько лет тебе будет в будущем 8)')
current_age = -1
while current_age < 0 or current_age > 130:
    current_age = int(input('Сколько тебе сейчас полных лет? Введи число в интервале от 0 до 130:'))
    if current_age < 0 or current_age > 130:
        print('Введен некорректный возраст!')
    else:
        break
future_year = 9998
while future_year > current_year or future_year < 9999:
    future_year = int(input('Введи год, в котором ты хочешь узнать свой будущий возраст:'))
    if future_year < current_year or future_year > 9999:
        print('Введен некорректный год! Введи год в интервале от текущего до 9999 года')
    else:
        break
future_age = future_year - current_year + current_age
print('Итак, в', future_year, 'году тебе будет', future_age, 'лет')

