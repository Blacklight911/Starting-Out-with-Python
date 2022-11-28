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
t.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо
t.dot()
t.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Правое плесо
t.dot()
t.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
t.dot()
t.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
t.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)