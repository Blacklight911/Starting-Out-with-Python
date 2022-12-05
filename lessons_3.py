"""Игра порази цель"""

import turtle

# Именованные константы
SCREEN_WIDTH = 600    # Ширина экрана.
SCREEN_HEIGHT = 600   # Высота экрана.
TARGET_LLEFT_X = 100  # Левая нижняя координата X цели.
TARGET_LLEFT_Y = 250  # Левая нижняя координата Y цели.
TARGET_WIDTH = 25     # Ширина цели.
FORCE_FACTOR = 30     # Фактор произвольной силы.
PROJECTILE_SPEED = 1  # Скорость анимации снаряда.
NORTH = 90            # Угол северного направления.
SOUTH = 270           # Угол южного направления.
EAST = 0              # Угол восточного направления.
WEST = 180            # Угол западного направления.

# Настроить окно.
turtle.title('Hit the target')
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Нарисовать цель.
Target = turtle.Turtle()
Target.hideturtle()
Target.penup()
Target.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
Target.pendown()
Target.setheading(EAST)
Target.fd(TARGET_WIDTH)
Target.setheading(NORTH)
Target.fd(TARGET_WIDTH)
Target.setheading(WEST)
Target.fd(TARGET_WIDTH)
Target.setheading(SOUTH)
Target.fd(TARGET_WIDTH)
Target.penup()

# Центрировать черепаху снаряд
Target.goto(0, 0)
Target.setheading(EAST)
Target.showturtle()
Target.speed(PROJECTILE_SPEED)

# Получить угол выстрела и силу от пользователя
angle = turtle.numinput('Введите угол выстрела снаряда', 'Введите число от 0 до 270:', minval=0, maxval=270)
force = turtle.numinput('Введите пусковую силу', 'Введите число от 0 до 10:', minval=0, maxval=10)

# Рассчитать расстояние.
distance = force * FORCE_FACTOR

# Задать направление.
Target.setheading(angle)

# Запустить снаряд.
Target.pendown()
Target.fd(distance)

# Логика поражения цели снарядом.
# В предыдущей главе было сказано про метод write а также про метод numinput.
# Почему бы не использовать их ? Welcome to the club budy.
if TARGET_LLEFT_X <= Target.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and TARGET_LLEFT_Y <= Target.ycor() <= (
        TARGET_LLEFT_Y + TARGET_WIDTH):
    Target.write('Есть пробитие!', align='left', font=('Arial', 16, 'normal'))
else:
    Target.write('Промах!', align='left', font=('Arial', 16, 'normal'))

# Выход по клику левой кнопкой мыши.
turtle.exitonclick()
