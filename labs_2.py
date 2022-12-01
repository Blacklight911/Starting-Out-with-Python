"""Алгоритмический тренажер"""
import turtle

# height = input('Введите свой рост')
# color = input('Введите свой любимый цвет')
#
# a, b, c = 0, 0, 0
#
# b = a + 2
# a = b * 4
# b = a / 3.14
# a = b - 8
#
# x, w, y, z = 4, 5, 8, 2

# total = 10 + 14
# down_payment = 10
# due = total - down_payment
# subtotal = 15000
# total = subtotal * 0.15
# sales = 1500.36910
# print(f'{sales:.2f}')

# number = 1234567.456
# print(f'{number:,.1f}')


# turtle.forward(100)
# turtle.setheading(90)
# turtle.forward(100)
# turtle.setheading(180)
# turtle.forward(100)
# turtle.setheading(270)
# turtle.forward(100)
# turtle.penup()
# turtle.setheading(0)
# turtle.forward(90)
# turtle.setheading(90)
# turtle.forward(50)
# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(40)
# turtle.end_fill()
# turtle.done()

# print('Дмитрий')
# print('Белгород, улица Некрасова 7, индекс 13378')
# print('89978861974')
# print('Информационные Технологии')

# # Прогноз продаж.
# total_sum = int(input('Введите плановую сумму объема продаж '))
# print(int(total_sum * 0.23))

# # Расчет площади земельного участка
# land_plot = int(input('Введите общее количество квадратных метров земельного участка '))
# print(land_plot / 4047)

# # Общий объём продаж
# TAX = 0.07
# all_tax = 0
# all_price = 0
# for i in range(5):
#     price = int(input('Введите цену товара '))
#     all_price += price
#     all_tax += price * TAX
# print('Сумма товара', all_price)
# print('Налог составил', all_tax)
# print('Итоговая стоимость составила', all_price + all_tax)

# # Пройденное расстояние
# print('Расстояние, которое автомобиль пройдет за 6 часов:', 70 * 6)
# print('Расстояние, которое автомобиль пройдет за 10 часов:', 70 * 10)
# print('Расстояние, которое автомобиль пройдет за 15 часов:', 70 * 15)

# buy_value = int(input('Введите величину покупки: '))
# federal_tax = 0.05
# regional_tax = 0.025
# sum_federal_tax = buy_value * federal_tax
# sum_regional_tax = buy_value * regional_tax
# print('Сумма покупки: ', buy_value)
# print('Федеральный налог составил:', sum_federal_tax)
# print('Региональный налог составил:', sum_regional_tax)
# print('Сумма покупки с налогом составила:', buy_value + sum_regional_tax + sum_federal_tax)

# # Расход бензина в расчете на километры пройденного пути.
# kilometers_covered = int(input('Количество пройденных километров'))
# fuel_on_kilo = int(input('Введите расход бензина в литрах'))
# print('Расход ', kilometers_covered / fuel_on_kilo)

# # Чаевые налог и общая сумма
# food_cost = int(input('Стоимость еды: '))
# print('Общая стоимость:', food_cost + food_cost * 0.18 + food_cost * 0.07)

# # Преобразователь температуры
# num = int(input('Введите температуру: '))
# print('Температура в Фаренгейтах:', 9 / 5 * num + 32)

# # Регулятор ингридиентов.
# how_much_buns = int(input('Какое количество булочек вы хотите испечь? '))
# print(f'Стакана сахара {1.5 / 48 * how_much_buns:.2f}')
# print(f'Стакана масла {1 / 48 * how_much_buns:.2f}')
# print(f'Стакана муки {2.75 / 48 * how_much_buns:.2f}')

# # Процент учащихся обоего пола.
# how_much_man = int(input('Количество учащихся юношей: '))
# how_much_woman = int(input('Количество учащихся девушек: '))
# how_much_all = how_much_man + how_much_woman
# print(f'Учащихся мужского пола {how_much_man / how_much_all:.0%}. \
# Учащихся женского пола {how_much_woman / how_much_all:.0%}')

# # Программа расчета купли-продажи акции.
# total_shares = 2000
# per_share = 40.00
# spend_per_share = 42.75
# total_spend = 2000 * 40.00
# broker_commission = 0.03 * total_spend
# spend_broker_commission = spend_per_share * total_shares * 0.03
# print('Сумма денег уплаченная за акции составила', total_spend)
# print('Сумма денег уплаченная брокеру при покупке акций', broker_commission)
# print('Сумма денег за которую Джо продал акции', spend_per_share * total_shares)
# print('Сумма комиссии уплаченную брокеру при продаже акции', spend_broker_commission)
# print('Сумма денег которая осталась у Джо после продажи акций', spend_per_share * total_shares -
#       broker_commission - spend_broker_commission)
#
# # Выращивание винограда.
# R = int(input('Введите длину гряды в метрах '))
# E = int(input('Введите размер пространства занимаемого концевыми опорами в метрах '))
# S = int(input('Введите расстояние между виноградными лозами в метрах '))
# print('Количество виноградных лоз, которые поместятся на гряде', R - 2 * E / S)


# Сложный процент
# P = int(input('Введите основную сумму '))
# r = int(input('Введите годовую процентную ставку(от 0 до 100) ')) / 100
# n = int(input('Введите частоту начисления процентного дохода в год(Например, если проценты '
#               'ежеквартально, то ввести 4 '))
# t = int(input('Введите количество лет '))
# A = (P * ((1 + r) / n)) ** (n * t)
# print('Через', t, 'лет доход составит', A)

# Рисунки черепашьей графики
# Двойной ромб
Rhombus = turtle.Turtle()
Rhombus.penup()
# Rhombus.goto(-280, 250)
Rhombus.pendown()
Rhombus.color('brown')
Rhombus.begin_fill()
Rhombus.left(60)
Rhombus.fd(60)
Rhombus.left(90)
Rhombus.fd(60)
Rhombus.left(90)
Rhombus.fd(60)
Rhombus.left(90)
Rhombus.fd(60)
# for _ in range(3):
#     Rhombus.left(190)
#     Rhombus.forward(90)
Rhombus.end_fill()
turtle.done()
