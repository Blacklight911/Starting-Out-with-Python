"""Алгоритмический тренажер, Лабораторные работы часть 2"""
import turtle

height = input('Введите свой рост')
color = input('Введите свой любимый цвет')

a, b, c = 0, 0, 0

b = a + 2
a = b * 4
b = a / 3.14
a = b - 8

x, w, y, z = 4, 5, 8, 2
#
total = 10 + 14
down_payment = 10
due = total - down_payment
subtotal = 15000
total = subtotal * 0.15
sales = 1500.36910
print(f'{sales:.2f}')

number = 1234567.456
print(f'{number:,.1f}')


turtle.forward(100)
turtle.setheading(90)
turtle.forward(100)
turtle.setheading(180)
turtle.forward(100)
turtle.setheading(270)
turtle.forward(100)
turtle.penup()
turtle.setheading(0)
turtle.forward(90)
turtle.setheading(90)
turtle.forward(50)
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
turtle.done()

print('Дмитрий')
print('Белгород, улица Некрасова 7, индекс 13378')
print('89978861974')
print('Информационные Технологии')

# Упражнения по программированию.
# Прогноз продаж.
total_sum = int(input('Введите плановую сумму объема продаж '))
print(int(total_sum * 0.23))

# Расчет площади земельного участка.
land_plot = int(input('Введите общее количество квадратных метров земельного участка '))
print(land_plot / 4047)

# Общий объём продаж.
TAX = 0.07
all_tax = 0
all_price = 0
for i in range(5):
    price = int(input('Введите цену товара '))
    all_price += price
    all_tax += price * TAX
print('Сумма товара', all_price)
print('Налог составил', all_tax)
print('Итоговая стоимость составила', all_price + all_tax)

# Пройденное расстояние.
print('Расстояние, которое автомобиль пройдет за 6 часов:', 70 * 6)
print('Расстояние, которое автомобиль пройдет за 10 часов:', 70 * 10)
print('Расстояние, которое автомобиль пройдет за 15 часов:', 70 * 15)

# Налог с продаж.
buy_value = int(input('Введите величину покупки: '))
federal_tax = 0.05
regional_tax = 0.025
sum_federal_tax = buy_value * federal_tax
sum_regional_tax = buy_value * regional_tax
print('Сумма покупки: ', buy_value)
print('Федеральный налог составил:', sum_federal_tax)
print('Региональный налог составил:', sum_regional_tax)
print('Сумма покупки с налогом составила:', buy_value + sum_regional_tax + sum_federal_tax)

# Расход бензина в расчете на километры пройденного пути.
kilometers_covered = int(input('Количество пройденных километров'))
fuel_on_kilo = int(input('Введите расход бензина в литрах'))
print('Расход ', kilometers_covered / fuel_on_kilo)

# Чаевые налог и общая сумма.
food_cost = int(input('Стоимость еды: '))
print('Общая стоимость:', food_cost + food_cost * 0.18 + food_cost * 0.07)

# Преобразователь температуры.
num = int(input('Введите температуру: '))
print('Температура в Фаренгейтах:', 9 / 5 * num + 32)

# Регулятор ингридиентов.
how_much_buns = int(input('Какое количество булочек вы хотите испечь? '))
print(f'Стакана сахара {1.5 / 48 * how_much_buns:.2f}')
print(f'Стакана масла {1 / 48 * how_much_buns:.2f}')
print(f'Стакана муки {2.75 / 48 * how_much_buns:.2f}')

# Процент учащихся обоего пола.
how_much_man = int(input('Количество учащихся юношей: '))
how_much_woman = int(input('Количество учащихся девушек: '))
how_much_all = how_much_man + how_much_woman
print(f'Учащихся мужского пола {how_much_man / how_much_all:.0%}. \
Учащихся женского пола {how_much_woman / how_much_all:.0%}')

# Программа расчета купли-продажи акции.
total_shares = 2000
per_share = 40.00
spend_per_share = 42.75
total_spend = 2000 * 40.00
broker_commission = 0.03 * total_spend
spend_broker_commission = spend_per_share * total_shares * 0.03
print('Сумма денег уплаченная за акции составила', total_spend)
print('Сумма денег уплаченная брокеру при покупке акций', broker_commission)
print('Сумма денег за которую Джо продал акции', spend_per_share * total_shares)
print('Сумма комиссии уплаченную брокеру при продаже акции', spend_broker_commission)
print('Сумма денег которая осталась у Джо после продажи акций', spend_per_share * total_shares -
      broker_commission - spend_broker_commission)

# Выращивание винограда.
R = int(input('Введите длину гряды в метрах '))
E = int(input('Введите размер пространства занимаемого концевыми опорами в метрах '))
S = int(input('Введите расстояние между виноградными лозами в метрах '))
print('Количество виноградных лоз, которые поместятся на гряде', R - 2 * E / S)


# Сложный процент.
P = int(input('Введите основную сумму '))
r = int(input('Введите годовую процентную ставку(от 0 до 100) ')) / 100
n = int(input('Введите частоту начисления процентного дохода в год(Например, если проценты'
              'ежеквартально, то ввести 4 '))
t = int(input('Введите количество лет '))
A = (P * ((1 + r) / n)) ** (n * t)
print('Через', t, 'лет доход составит', A)

# Рисунки черепашьей графики.
turtle.setup(800, 700)
# Двойной ромб.
Rhombus = turtle.Turtle()
Rhombus.penup()
Rhombus.goto(-280, 250)
Rhombus.pendown()
Rhombus.color('black')
Rhombus.begin_fill()
for _ in range(2):
    Rhombus.rt(120)
    Rhombus.fd(100)
    Rhombus.rt(120)
    Rhombus.fd(100)
    Rhombus.rt(60)
    Rhombus.fd(100)
    Rhombus.rt(120)
    Rhombus.fd(100)
    Rhombus.rt(120)
    Rhombus.goto(-280, 250)
Rhombus.end_fill()
Rhombus.hideturtle()

# Треугольник в треугольнике.
Triangle = turtle.Turtle()
Triangle.penup()
Triangle.goto(-40, 160)
Triangle.pendown()
Triangle.fd(120)
Triangle.lt(110)
Triangle.fd(180)
Triangle.lt(140)
Triangle.fd(180)
Triangle.begin_fill()
Triangle.lt(163)
Triangle.fd(100)
Triangle.rt(103)
Triangle.fd(103)
Triangle.end_fill()
Triangle.hideturtle()

# Круги.
Circle = turtle.Turtle()
Circle.penup()
for x in range(-50, 140, 70):
    Circle.goto(x, 20)
    Circle.pendown()
    Circle.circle(30)
    Circle.penup()
for x in range(-15, 110, 70):
    Circle.goto(x, -10)
    Circle.pendown()
    Circle.circle(30)
    Circle.penup()
Circle.hideturtle()

# Прямоугольный параллелепипед.
Parallelepiped = turtle.Turtle()
Parallelepiped.penup()
Parallelepiped.goto(-280, 20)
Parallelepiped.pendown()
for n in range(4):
    Parallelepiped.fd(50)
    Parallelepiped.lt(90)
Parallelepiped.penup()
Parallelepiped.fd(50)
Parallelepiped.pendown()
for n in range(4):
    Parallelepiped.fd(50)
    Parallelepiped.rt(90)
Parallelepiped.penup()
Parallelepiped.goto(-280, 20)
Parallelepiped.pendown()
Parallelepiped.rt(45)
Parallelepiped.fd(72)
Parallelepiped.penup()
Parallelepiped.goto(-230, 70)
Parallelepiped.pendown()
Parallelepiped.fd(72)
Parallelepiped.penup()
Parallelepiped.goto(-280, 70)
Parallelepiped.pendown()
Parallelepiped.fd(142)
Parallelepiped.hideturtle()

# Компас.
Compas = turtle.Turtle()
Compas.penup()
Compas.goto(-330, -220)
Compas.pendown()
Compas.fd(200)
Compas.penup()
Compas.goto(-230, -120)
Compas.rt(90)
Compas.pendown()
Compas.fd(200)
Compas.penup()
Compas.goto(-255, -220)
Compas.pendown()
Compas.circle(25)
Compas.penup()
Compas.goto(-230, -110)
Compas.write('Север', align='center', font=('Arial', 10, 'normal'))
Compas.penup()
Compas.goto(-230, -340)
Compas.pendown()
Compas.write('Юг', align='center', font=('Arial', 10, 'normal'))
Compas.penup()
Compas.goto(-360, -230)
Compas.pendown()
Compas.write('Запад', align='center', font=('Arial', 10, 'normal'))
Compas.penup()
Compas.goto(-100, -230)
Compas.pendown()
Compas.write('Запад', align='center', font=('Arial', 10, 'normal'))
Compas.hideturtle()

# Квадрат.
Square = turtle.Turtle()
Square.penup()
Square.goto(131, -221)
Square.dot(10)
Square.penup()
Square.goto(230, -120)
Square.pendown()
Square.dot(10)
Square.rt(90)
Square.fd(200)
Square.dot(10)
Square.rt(135)
Square.fd(282)
Square.dot(10)
Square.lt(135)
Square.fd(200)
Square.dot(10)
Square.lt(135)
Square.fd(283)

# Пунктирные лини квадрата.
Square.lt(135)
Square.fd(20)
Square.penup()
Square.fd(25)
Square.pendown()
Square.fd(40)
Square.penup()
Square.fd(35)
Square.pendown()
Square.fd(40)
Square.penup()
Square.fd(25)
Square.pendown()
Square.fd(20)
Square.penup()
Square.goto(230, -320)
Square.pendown()
Square.fd(20)
Square.penup()
Square.fd(25)
Square.pendown()
Square.fd(40)
Square.penup()
Square.fd(35)
Square.pendown()
Square.fd(40)
Square.penup()
Square.fd(25)
Square.pendown()
Square.fd(20)
Square.hideturtle()

turtle.exitonclick()
