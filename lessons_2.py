"""Lesson 2"""
import turtle

second_name = input('Введите фамилию: ')
week_sells = float(input('Введите объем продаж за неделю: '))

print('Black\nwatch')
print('Black\twatch')
print('Black\"watch')
print('Black\'watch\\')

DISCOUNT = 10000000000.0
print(f'{DISCOUNT:^20,.0f}')
VALUE = 987654.129
print(f'{VALUE:.2f}')

INTEREST_RATE = 0.10
print(f'{INTEREST_RATE:.0%}')

turtle.forward(200)
turtle.penup()
turtle.setheading(90)
turtle.forward(50)
turtle.down()
turtle.forward(50)
turtle.circle(50)
turtle.dot
turtle.bgcolor('gray')
turtle.pensize(5)
turtle.circle(70)
turtle.pencolor('red')
turtle.forward(50)
t = turtle
t.goto(100, 0)
t.goto(120, 70)
t.clear()
t.reset()
t.clearscreen()

t.goto(100, 200)
pos_turtle = t.pos()
pos_x = t.xcor()
pos_y = t.ycor()
t.speed(7)
t.hideturtle()
t.showturtle()
t.forward(50)
radius = t.numinput('Введите значение', 'Каков радиус окружности?')
t.textinput('input text',  'here')
t.circle(radius)
t.done()
