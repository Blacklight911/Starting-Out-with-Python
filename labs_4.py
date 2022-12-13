""" Algorithmic simulator"""
import turtle

# product = 1
#
#
# while product < 100:
#     num = int(input('Enter number: '))
#     product += num * 10
# done = False
#
# while done is False:
#     num1 = int(input('Enter first number: '))
#     num2 = int(input('Enter second number: '))
#     print('Amount =',num1 + num2)
#     question = input('Would you like to perform the operation again? Enter y - yes, n - no ')
#     if question.lower() == 'n':
#         done = True
#
# for i in range(0, 1001, 10):
#     print(i, end=' ')
# amount = 0
#
# for _ in range(10):
#     num = int(input('Enter number: '))
#     amount += num
#     print(amount)
#
# num1 = 1
# num2 = 30
# for _ in range(30):
#     print(f'{num1 / num2:.2f}')
#     num1 += 1
#     num2 -= 1


# x += 1
# x *= 2
# x /= 10
# x -= 100

# for _ in range(10):
#     for _ in range(15):
#         print('#', end='')
#     print()
#
# done = False
#
# while done is False:
#     try:
#         num = int(input('Enter positive non-zero number: '))
#         if num > 0:
#             done = True
#         else:
#             print('Error, enter positive non-zero number.')
#     except ValueError:
#         print('Error, enter positive non-zero number.')
#
# done = False
#
# while done is False:
#     try:
#         num = int(input('Enter value (1 - 100):'))
#         if 1 <= num <= 100:
#             done = True
#         else:
#             print('Error, enter valid value')
#     except ValueError:
#         print('Error, enter valid value')

# Programming exercises.
# Errors collector.
done = False
amount = 0
end_of_day = 1
while done is False:
    print('Day: ', end_of_day)
    errors = int(input('Enter number of errors per day: '))
    amount += errors
    if end_of_day == 5:
        done = True
    day = input('Day end? y or n: ')
    if day == 'y':
        end_of_day += 1

print('total errors:', amount)

# Calories burned.
calories_per_min = 4, 2

for i in range(10, 31, 5):
    print('Calories burned per', i, 'minutes:', i * 4.2)

# Budget analysis.
done = False
dollars_per_month = int(input('Enter budget for a month: '))
sum_dollars = 0

while done is False:
    costs = int(input('Enter the expense of funds: '))
    sum_dollars += costs
    end_count = input('End counting? y - yes, n - no: ')
    if end_count.lower() == 'y':
        done = True

print('Expenses were $', dollars_per_month - sum_dollars)


# Distance traveled.
# User input.
speed = int(input('Enter vehicle speed: '))
hours = int(input('Enter number of hours: '))

# Markup.
print('Hour   Distance traveled')
print('-------------------------')

# Main program loop.
for hour in range(1, hours+1):
    print(f'{hour:>} {speed * hour:8}')

# Average rainfall layer thickness.
# User input.
years = int(input('Enter number of years: '))
total_rainfall = 0

# Main program loop.
for year in range(1, years+1):
    for month in range(1, 13):
        rainfall_amount = int(input('Enter the amount of rainfall during the month: '))
        total_rainfall += rainfall_amount

print('Number of months: ', years * 12, 'Total millimeters of rainfall:', total_rainfall,
      'The average thickness of the rainfall layer per month during the entire period',
      total_rainfall // (years * 12))

# Correspondence table between degrees Celsius and degrees Fahrenheit.
for t in range(21):
    print(f'Temperature in Celsius: {t:<2} Temperature in Fahrenheit {9 / 5 * t + 32:.0f}')

# Small coin for salary.
num_days = int(input('Enter the number of days worked: '))
total_salary = 0
print('Day    Salary')
print('-------------')

for day in range(1, num_days+1):
    total_salary += day * 2
    print(f'{day:<2}  -  {day * 2:<2} cents')

print('-----------------------------')
print(f'Salary before taxes: ${total_salary * 100 / 100:}c')
print(f'Total salary:        ${(total_salary * 100 - (total_salary * 100 * 0.13)) / 100:}c')

# Sum of numbers.
num = int(input('Enter number, for sum, to stop program enter negative number: '))
all_num = 0

while num > 0:
    num = int(input('Enter number: '))
    all_num += num

print('Sum numbers =', all_num)

# Ocean Level.
# Variables.
ocean_level = 1.6
all_level = 0

# Main program loop.
for year in range(1, 26):
    all_level += ocean_level
    print(f'In Year: {2022 + year} Ocean level: {all_level:.1f}mm')

# Growth in tuition fees.
per_year = 290000.0
percent_per_year = 0.03
for year in range(1, 5 + 1):
    print(f'In year: {2022 + year} The tuition fee will be: {per_year:,.2f} rubles')
    per_year = per_year + (per_year * percent_per_year)

# Loss of mass.
COLORY = 500
person_height = int(input('Enter your height: '))

print('Month    Height')
print('-------------------------')

for month in range(1, 7):
    print(f'{month:3}    {person_height * COLORY * (month * 30) // 1000000:8}'
          f'.{person_height * COLORY * (month * 30) % 1000000 // 10000} kg')

# Calculation of the factorial.
num = int(input('Enter number factorial: '))
factorial = 1

for n in range(1, num+1):
    factorial *= n
print('Factorial number', num, '=', factorial)

# Population.
# Starting fields
quantity = float(input('Starting number of organisms: '))
average_population = float(input('average daily population increase (as a percentage): ')) / 100
reproduction_days = float(input('number of days for reproduction: '))
s = 0

print('Day      Population')

for day in range(1, int(reproduction_days + 1)):
    print(f'{day:<2}       {quantity:.7}')
    quantity += quantity * average_population

# Draw loops.
n = int(input('Enter value for draw: '))
for i in range(n):
    for j in range(n - i):
        print('*', end=' ')
    print()

# Next loop.
n_2 = int(input('Enter value for draw: '))
for i in range(7):
    print('#', end='')
    for k in range(i):
        print(' ', end='')
    for j in range(1):
        print('#', end='')
    print()

# Turtle Graphics: Star pattern
Star = turtle.Turtle()
n = 8
sum_angle = (n-2)*180
angle = sum_angle // n

for i in range(n):
    Star.fd(250)
    Star.lt(angle)

# Turtle Graphics: Hypnotic pattern.
Hyp = turtle.Turtle()
size = 10

for i in range(50):
    for _ in range(1):
        Hyp.fd(size * i)
        Hyp.lt(90)

# Turtle Graphics: Stop sign.
Stop = turtle.Turtle()

for _ in range(8):
    Stop.fd(300)
    Stop.rt(45)
Stop.pu()
Stop.fd(100)
Stop.rt(90)
Stop.fd(400)
Stop.write('STOP')
