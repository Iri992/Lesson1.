while True:
days = 1
start_km = float(input('Начальный результат: '))
last_km = float(input('Конечный результат: '))
if start_km <= 0 or last_km < 0:
print('Результаты должны быть больше нуля. Начальное значение !=0.')
else:
while start_km < last_km:
start_km += start_km * 0.1
days += 1
print(f'Спортсмен достигнет цели за {days} дней')
break
