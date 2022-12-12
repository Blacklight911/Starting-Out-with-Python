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
# #
# if 100 <= turtle.xcor() <= 200 and 100 <= turtle.ycor() <= 200:
#     turtle.hideturtle()
# #
# # Programming Exercises
# # Day of week
# value = input('Input day of week (1-7): ')
# week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
#
# try:
#     if int(value) > 0:
#         print(week[int(value)-1])
#
# except ValueError:
#     print('Enter value in range 1 - 7')
#
# else:
#     print('Enter value in range 1 - 7')
# #
# # Area of rectangles
# # User input first rect.
# first_rect_width = int(input('Enter width first rectangle: '))
# first_rect_height = int(input('Enter height first rectangle: '))
#
# # User input second rect.
# second_rect_width = int(input('Enter width second rectangle: '))
# second_rect_height = int(input('Enter height second rectangle: '))
#
# # Calculation of the area of the rectangles
# first_rect = first_rect_width * first_rect_height
# second_rect = second_rect_width * second_rect_height
#
# # Calculation the largest rectangle.
# if first_rect > second_rect:
#     print('Area of first rectangle largest:', first_rect)
# elif second_rect > first_rect:
#     print('Area of first rectangle largest:', second_rect)
# else:
#     print('Area of rectangles equals:', first_rect, second_rect)
# #
# #
# # Classifier of age.
# # User input.
# person_age = int(input('Enter your age: '))
#
# # Age check.
# if person_age <= 1:
#     print('Person is baby')
# elif 1 < person_age < 13:
#     print('Person is child')
# elif 13 <= person_age < 20:
#     print('Person is teenager')
# elif person_age <= 20:
#     print('Person is adult')
# #
# # Roman numbers.
# # User input.
# number = input('Enter number in range 1 - 10: ')
#
# # List of Roman numbers.
# roman_numbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
#
# # Check number.
# try:
#     if int(number) > 0:
#         print(f'For {number} Roman number is {roman_numbers[int(number) - 1]}')
#     else:
#         print('Input correct number')
# except ValueError:
#     print('Input correct number')
# #
# # Mass & Weight.
# # User input
# mass = int(input('Enter mass: '))
#
# # Calculate weight.
# weight_in_newtons = mass * 9.8
#
# # Check weight in newtons.
# if weight_in_newtons > 500:
#     print('Weight is to heavy')
# elif weight_in_newtons < 100:
#     print('Weight is to light')
#
# # Magical dates.
# # User input.
# month = int(input('Enter number of month'))
# day = int(input('Enter number of day'))
# year = int(input('Enter last two numbers of year'))
#
# # Is magic number ?
# magic_num = month * day
#
# # Check magic number
# if magic_num == year:
#     print('The entered date is magic!')
# else:
#     print('This date is magic')
# #
# # Color mixer.
# # User input.
# color_1 = input('Input color(red, blue or yellow) ')
# color_2 = input('Input color(red, blue or yellow) ')
#
# if color_1 == 'red' and color_2 == 'blue' or color_1 == 'blue' and color_2 == 'red':
#     print('Color mixing result: purple color')
# elif color_1 == 'red' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'red':
#     print('Color mixing result: orange color')
# elif color_1 == 'blue' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'blue':
#     print('Color mixing result: green color')
# else:
#     print('Enter correct color(red, blue or yellow) not the same colors.')
# #
# # Picnic Sausage Calculator.
# # User input.
# num_of_persons = int(input('Enter number of persons: ')) # 10
# num_of_hot_dogs = int(input('Enter number of hot dogs per person: ')) # 5
#
# print('The minimum required number of packages with sausages: ', num_of_persons * num_of_hot_dogs // 10)
# print('The minimum required number of packages with buns: ', num_of_persons * num_of_hot_dogs // 8)
# print('Number of sausages left: ', (num_of_persons * num_of_hot_dogs // 10) // 10)
# print('Number of buns left: ', (num_of_persons * num_of_hot_dogs // 8) // 8)
#
# # Roulette wheel colors.
# # User input.
# num = int(input('Enter number in range 0 - 36: '))
#
# if num == 0:
#     print('Pocket is green')
# elif 1 <= num <= 10:
#     if num % 2 == 0:
#         print('Pocket is black')
#     else:
#         print('Pocket is red')
# elif 11 <= num <= 18:
#     if num % 2 == 0:
#         print('Pocket is red')
#     else:
#         print('Pocket is black')
# elif 19 <= num <= 28:
#     if num % 2 == 0:
#         print('Pocket is black')
#     else:
#         print('Pocket is red')
# elif 29 <= num <= 36:
#     if num % 2 == 0:
#         print('Pocket is red')
#     else:
#         print('Pocket is black')
# else:
#     print('Input valid number')
# #
# # Coin counting game.
# # You need to collect 100 coins to get 1 dollar.
#
# # Constants.
# DONE = False
#
# # Variables.
# dollar = 0
#
# # Cycle end if DONE is True.
# while DONE is False:
#     coins = int(input('Input number of cents(1, 5, 10, 50): '))
#     dollar += coins
#     if dollar == 100:
#         DONE = True
#         print('Congratulations you win, you get one dollar')
#     elif dollar > 100:
#         print('You lose, you get', dollar // 100, 'dollar and', dollar // 10, 'cents')
#         DONE = True
# #
# # Book club points.
# # User input
# customer_books = int(input('Enter the number of books you bought this month: '))
#
# # Checking number of books.
# if customer_books == 0:
#     print('You have 0 points')
# elif customer_books == 2:
#     print('You have 5 points')
# elif customer_books == 4:
#     print('You have 15 points')
# elif customer_books == 6:
#     print('You have 30 points')
# elif customer_books <= 8:
#     print('You have 60 points')
# #
# # Software Implementation.
# # User input.
# num_s_packs = int(input('Enter number of software packages purchased: '))
#
# # Variables.
# one_s_pack = 99
#
# # Check number of packs.
# if 10 <= num_s_packs <= 19:
#     print('Your discount is 10%, price is:', num_s_packs * 99 * 0.1)
# elif 20 <= num_s_packs <= 49:
#     print('Your discount is 20%, price is:', num_s_packs * 99 * 0.2)
# elif 50 <= num_s_packs <= 99:
#     print('Your discount is 30%, price is:', num_s_packs * 99 * 0.3)
# elif num_s_packs <= 100:
#     print('Your discount is 40%, price is:', num_s_packs * 99 * 0.4)
# else:
#     print('Your price is', num_s_packs * 99)
#
# # Delivery cost.
# # User input.
# weight = int(input('Enter package weight: '))
#
# # Check weight package.
# if weight <= 200:
#     print('Shipping a parcel weighing:', weight, 'will cost:', weight * 150)
# elif 200 < weight <= 600:
#     print('Shipping a parcel weighing:', weight, 'will cost:', weight * 300)
# elif 600 < weight <= 1000:
#     print('Shipping a parcel weighing:', weight, 'will cost:', weight * 400)
# elif weight > 1000:
#     print('Shipping a parcel weighing:', weight, 'will cost:', weight * 475)
#
# # Body mass index.
# # Catching a ValueError
# try:
#     # User input and calculation of body weight according to the formula.
#     mass = int(input('Enter your weight: '))
#     height = int(input('Enter your height: '))
#     bmi = mass / (height / 100) ** 2
#
#     # Checking bmi value.
#     if 18.5 <= bmi <= 25:
#         print(f'Your bmi is {bmi:.2f} You are normal weight')
#     elif bmi < 18.5:
#         print(f'Your bmi is {bmi:.2f} You are underweight')
#     elif bmi > 25:
#         print(f'Your bmi is {bmi:.2f} You are overweight')
# except ValueError:
#     print('Enter normal value.')
#
# Time calculator.
# User input.
# sec = int(input('Enter number of second: '))
#
# # Checking time in second.
# if 60 <= sec < 3600:
#     print(f'minutes: {sec // 60}, seconds: {sec % 60}')
# elif 3600 <= sec < 86400:
#     print(f'hours: {sec // 3600}, minutes: {sec % 3600 // 60}, seconds: {sec % 60}')
# elif sec >= 86400:
#     print(f'days {sec // 86400} ,hours: {sec % 86400 // 3600}, minutes: {sec % 3600 // 60}, seconds: {sec % 60}')
#
# # Days of February.
# # User input.
# year = int(input('Enter year: '))
#
# #Checking year.
# if year % 100 == 0 and year % 400 == 0 or year % 4 == 0:
#     print(f'In {year} year in february 29 days.')
# else:
#     print(f'In {year} year in february 28 days')
#
#
# # Diagnostic tree quality control Wi-Fi.
# print('Reboot your pc and try reconect')
# question = input('Problem solved? Enter y - yes, or n - no ')
# if question.lower() == 'y':
#     print('Have a nice day.')
# elif question.lower() == 'n':
#     print('Rebot your router and try reconnect.')
#     question = input('Problem solved? Enter y - yes, or n - no ')
#     if question.lower() == 'y':
#         print('Have a nice day.')
#     elif question.lower() == 'n':
#         print('Make sure that the cables between the router and the modem are firmly sub-eaten.')
#         question = input('Problem solved? Enter y - yes, or n - no ')
#         if question.lower() == 'y':
#             print('Have a nice day.')
#         elif question.lower() == 'n':
#             print('Move the router to a new location.')
#             question = input('Problem solved? Enter y - yes, or n - no ')
#             if question.lower() == 'y':
#                 print('Have a nice day.')
#             elif question.lower() == 'n':
#                 print('Take a new router')
#
#
# # Restaurant selector.
# # User input, who will come to dinner.
# vegeterian = input('Will there be a vegetarian at dinner? Enter y - yes, n - no. ')
# vegan = input('Will there be a vegan at dinner? Enter y - yes, n - no. ')
# gluten_free = input('Will there be a gluten-free diet adherent at dinner? Enter y - yes, n - no. ')
#
# print('Your restaurant options.')
#
# # Check.
# if vegeterian == 'n' and vegan == 'n' and gluten_free == 'n':
#     print('Exquisite hamburgers from Joe.')
#
# elif vegeterian == 'y' and vegan == 'n' and gluten_free == 'y':
#     print('Central pizzeria.')
#
# elif vegeterian == 'y' and vegan == 'y' and gluten_free == 'y':
#     print('Cafe around the corner.')
#
# elif vegeterian == 'y' and vegan == 'y' and gluten_free == 'y':
#     print("Chef's kitchen.")

# Turtle Graphics: Hit the Target Game Mod.
# Constants
SCREEN_WIDTH = 600    # Screen width.
SCREEN_HEIGHT = 600   # Screen height.
TARGET_LLEFT_X = 100  # The bottom left X coordinate of the target.
TARGET_LLEFT_Y = 250  # The bottom left Y coordinate of the target.
TARGET_WIDTH = 25     # Target width.
FORCE_FACTOR = 30     # Force factor.
PROJECTILE_SPEED = 1  # Projectile animation speed.
NORTH = 90            # North direction corner.
SOUTH = 270           # South direction corner
EAST = 0              # East direction corner.
WEST = 180            # West direction corner.

# Customize window.
turtle.title('Hit the target')
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Draw a target.
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

# Center turtle projectile
Target.goto(0, 0)
Target.setheading(EAST)
Target.showturtle()
Target.speed(PROJECTILE_SPEED)

# Get shot angle and force from user
angle = turtle.numinput('Enter the angle of the projectile', 'Enter a number from 0 to 270', minval=0, maxval=270)
force = turtle.numinput('Enter starting force', 'Enter a number from 0.0 to 10.0:', minval=0, maxval=10)

# Calculate distance.
distance = force * FORCE_FACTOR

# Set direction.
Target.setheading(angle)

# Launch projectile.
Target.pendown()
Target.fd(distance)

# The logic of hitting a target with a projectile.
if TARGET_LLEFT_X <= Target.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and TARGET_LLEFT_Y <= Target.ycor() <= (
        TARGET_LLEFT_Y + TARGET_WIDTH):
    Target.write('Got it!', align='left', font=('Arial', 16, 'normal'))
else:
    if Target.ycor() > TARGET_LLEFT_Y:
        Target.write('Miss! Take more right', align='left', font=('Arial', 16, 'normal'))
    elif Target.ycor() < (TARGET_LLEFT_Y + TARGET_WIDTH):
        Target.write('Miss! Take more left', align='left', font=('Arial', 16, 'normal'))


# Exit by clicking the left mouse button.
turtle.exitonclick()
