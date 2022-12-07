"""Алгоритмический тренажер"""
import turtle

# x = 100
# a = 9
#
# if x > 100:
#     y = 20
#     z = 40
#
# if a < 10:
#     b = 0
#     c = 1
#
# if a < 10:
#     b = 0
# else:
#     b = 99
#
# score = int(input('Введите вашу оценку от 0 до 100: '))
# A_SCORE = 95
# B_SCORE = 86
# C_SCORE = 69
# D_SCORE = 56
# F_SCORE = 40
#
# if score >= A_SCORE:
#     print('Ваш уровень - A')
# elif score >= B_SCORE:
#     print('Ваш уровень - B')
# elif score >= C_SCORE:
#     print('Ваш уровень - C')
# elif score >= D_SCORE:
#     print('Ваш уровень - D')
# else:
#     print('Ваш уровень - F')
#
# amount1 = 11
# amount2 = 99
#
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print('Большее', amount1)
#     else:
#         print('Большее', amount2)
#
# speed = 55
#
# if 24 < speed < 56:
#     print('Скорость нормальная')
# else:
#     print('Скорость аварийная')
#
# points = 50
#
# if not(9 <= points < 51):
#     print('Недопустимые точки')
# else:
#     print('Допустимые точки')
#
# if 0 <= turtle.heading() <= 45:
#     turtle.penup()
# print(turtle.isdown())
#
# if turtle.pencolor() == 'red' or turtle.pencolor() == 'blue':
#     turtle.pensize(5)

# if 100 <= turtle.xcor() <= 200 and 100 <= turtle.ycor() <= 200:
#     turtle.hideturtle()

# # Programming Exercises
# # Day of week
value = input('Input day of week (1-7): ')
week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

try:
    if int(value) > 0:
        print(week[int(value)-1])

except ValueError:
    print('Enter value in range 1 - 7')

else:
    print('Enter value in range 1 - 7')

# # Area of rectangles
# User input first rect.
first_rect_width = int(input('Enter width first rectangle: '))
first_rect_height = int(input('Enter height first rectangle: '))

# User input second rect.
second_rect_width = int(input('Enter width second rectangle: '))
second_rect_height = int(input('Enter height second rectangle: '))

# Calculation of the area of the rectangles
first_rect = first_rect_width * first_rect_height
second_rect = second_rect_width * second_rect_height

# Calculation the largest rectangle.
if first_rect > second_rect:
    print('Area of first rectangle largest:', first_rect)
elif second_rect > first_rect:
    print('Area of first rectangle largest:', second_rect)
else:
    print('Area of rectangles equals:', first_rect, second_rect)


# # Classifier of age.
# User input.
person_age = int(input('Enter your age: '))

# Age check.
if person_age <= 1:
    print('Person is baby')
elif 1 < person_age < 13:
    print('Person is child')
elif 13 <= person_age < 20:
    print('Person is teenager')
elif person_age <= 20:
    print('Person is adult')

# Roman numbers.
# User input.
number = input('Enter number in range 1 - 10: ')

# List of Roman numbers.
roman_numbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

# Check number.
try:
    if int(number) > 0:
        print(f'For {number} Roman number is {roman_numbers[int(number) - 1]}')
    else:
        print('Input correct number')
except ValueError:
    print('Input correct number')

# Mass & Weight.
# User input
mass = int(input('Enter mass: '))

# Calculate weight.
weight_in_newtons = mass * 9.8

# Check weight in newtons.
if weight_in_newtons > 500:
    print('Weight is to heavy')
elif weight_in_newtons < 100:
    print('Weight is to light')

# Magical dates.
# User input.
month = int(input('Enter number of month'))
day = int(input('Enter number of day'))
year = int(input('Enter last two numbers of year'))

# Is magic number ?
magic_num = month * day

# Check magic number
if magic_num == year:
    print('The entered date is magic!')
else:
    print('This date is magic')

# Color mixer. NOT COMPLITED.
# User input.
first_color = input('Input color(red, blue or green')
second_color = input('Input color(red, blue or green')

# Picnic Sausage Calculator.
