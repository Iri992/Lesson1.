profit = float(input('Введите выручку: '))
costs = float(input('Введите издержки фирмы: '))
result = profit - costs
if result > 0:
    print(f'Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}')
    workers = int(input('Введите количество сотрудников фирмы: '))
    print(f'прибыль в расчете на одного сотрудника составила {result / workers:.2f}')
elif result < 0:
    print('Фирма работает в ноль')
else:
    print('Фирма работает в убыток')

