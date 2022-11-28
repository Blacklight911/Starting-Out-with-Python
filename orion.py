import turtle

t = turtle
# Задать размер окна
t.setup(500, 600)

# Установить черепаху
t.penup()
t.hideturtle()

# Константы координат
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Нарисуем звезды
# Левое плечо
t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.write('Бетельгейзе')
t.dot()

# Крайняя левая звезда в поясе
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.write('Альнитак')
t.dot()

# Левое колено
t.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
t.write('Саиф')
t.dot()

# Средняя звезда в поясе
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.write('Альнилам')
t.dot()

# Крайняя правая звезда в поясе
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.write('Минтака')
t.dot()

# Правое плечо
t.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
t.write('Хатиса')
t.dot()

# Правое колено
t.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
t.write('Ригель')
t.dot()

# Нанести линию из левого плеча в левую звезду пояса
t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
t.pendown()
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.penup()

# Нанести линию из правого плеча в правую звезду пояса
t.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
t.pendown()
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.penup()

# Нанести линию из левой звезды пояса в среднюю звезду пояса
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.pendown()
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.penup()

# Нанести линию из левой звезды пояса в левое колено
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.pendown()
t.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
t.penup()

# Нанести линию из правой звезды пояса в правое колено
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
t.pendown()
t.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
t.penup()

# Оставить окно программы открытым.
t.done()
