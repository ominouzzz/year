import datetime
current_year = datetime.datetime.now().year

print('Прога определяет сколько лет тебе будет в будущем 8)')

while True:
    current_age = int(input('Сколько тебе сейчас полных лет? Введи число в интервале от 0 до 130:'))
    if 0 <= current_age < 130:
        break
    else:
        print('Введен некорректный возраст!')

while True:
    future_year = int(input('Введи год, в котором ты хочешь узнать свой будущий возраст:'))
    if current_year <= future_year <= 9999:
        break
    else:
        print('Введен некорректный год! Введи год в интервале от текущего до 9999 года')

future_age = future_year - current_year + current_age
print('Итак, в', future_year, 'году тебе будет', future_age, 'лет')

