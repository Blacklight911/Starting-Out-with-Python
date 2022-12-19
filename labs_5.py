"""Algorithmic simulator"""
import random
import turtle

# # 1
# def print_times_ten(num):
#     print(num * 10)
#
# # 2
# def show_value(quantity):
#     print('The quantity is:', quantity)
#
# show_value(12)
#
# # 5
# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)
#
# my_function(a= 2, b= 4, c=6)
#
# # 6
# def rand_num():
#     return random.randint(1, 100)
#
# rand = rand_num()
#
# # 7
# def half(num):
#     return num / 2
#
# # 8
# def cube(num):
#     return num ** 3
#
# result = cube(4)
#
# # 9
# def times_ten(number):
#     return number * 10
#
# # 10
# def get_first_name(first_name):
#     return first_name

"""Programming exercises"""


def main():
    # Kilometer converter.
    def kilometer_converter():
        def to_miles(kilometres):
            return kilometres * 0.6214

        number = float(input('Enter the distance in kilometers'))
        to_miles(number)

    # Modernization of the sales tax calculation program.
    def mod_of_sales_tax_p():
        buy_value = int(input('Enter purchase amount: '))

        def federal_tax(value):
            return value * 0.05

        def regional_tax(value):
            return value * 0.025

        def all_sum(value, regional_val, federal_val):
            return value + regional_val + federal_val

        fed_tax = federal_tax(buy_value)
        reg_tax = regional_tax(buy_value)
        print('Purchase amount:', buy_value)
        print('The federal tax amounted to:', fed_tax)
        print('The regional tax amounted to:', reg_tax)
        print('The amount of the purchase including tax was:', all_sum(buy_value, fed_tax, reg_tax))

    # What is the cost of insurance.
    def what_is_cost_of_insurance():
        cost = float(input('Enter building cost: '))
        number_percent = float(input('Enter number of percent(recommend minimum is 80%): ')) / 100

        def insured_sum(value, percent=0.8):
            return value * percent

        print(f'At building cost {cost}, sum insured will be: {insured_sum(cost, number_percent)}')

    # Car expenses.
    def car_expenses():
        car_costs = ['loan payments', 'insurance', 'petrol', 'machine oil', 'tires', 'maintenance']
        expenses = []
        for value in range(len(car_costs)):
            value_expenses = float(input(f'Enter the amount of expenses for the car {car_costs[value]}: '))
            expenses.append(value_expenses)

        print(f'Your monthly expenses were: {sum(expenses)}')
        print(f'Your annual expenses were: {sum(expenses) * 12}')

    # Real estate tax.
    def real_estate_tax():
        TAX = 72
        actual_cost = float(input('Enter actual cost: '))

        def assessed_cost(cost):
            return cost * 0.6

        def tax_calculation(tax_cost, act_cost, asses_cost):
            return tax_cost * asses_cost / act_cost

        print('Assessed value:', assessed_cost(actual_cost))
        print('Property tax:', tax_calculation(TAX, actual_cost, assessed_cost(actual_cost)))

    # Calories from fats and carbohydrates.
    def calories_f_fats_and_carbo():
        fats = float(input('Enter the amount of fat in grams per day: '))
        carbohydrates = float(input('Enter the amount of carbohydrates in grams per day: '))

        def calories_from_fat(value):
            return value * 9

        def calories_from_carbohydrates(value):
            return value * 4

        print(f'Number of calories: '
              f'Fats :{calories_from_fat(fats)}'
              f'Carbohydrates : {calories_from_carbohydrates(carbohydrates)}')

    # Seats in the stadium.
    def seats_in_the_stadium():
        seats = ['A', 'B', 'C']
        seats_values = (20, 15, 10)
        all_sum = 0

        for value in range(3):
            num = int(input(f'Enter the number of seats sold for {seats[value]}: '))
            all_sum += num * seats_values[value]

        print(f'Amount of proceeds from ticket sales: ${all_sum}')

    # Painting appraiser.
    def painting_appraiser():
        wall = float(input('Enter surface area of the painted wall: '))
        price = float(input('Enter the price of a 5 liter container of paint: '))

        print(f'Number of paint containers required for {wall} square meters: {0.5 * wall}')
        print(f'Number of working hours spent: {int(0.8 * wall)}')
        print(f'Paint all price: {(wall / 10) * price} rub')
        print(f'Total cost of painting work: {2000 * (0.8 * wall)} rub.')

    # Monthly sales tax.
    def month_sales_tax(value_sales, council_tax=0.025, federal_tax=0.05):
        print(f'Amount of municipal sales tax: {value_sales * council_tax}')
        print(f'Amount of federal sales tax: {value_sales * federal_tax}')
        print(f'General sales tax: {value_sales * council_tax + value_sales * federal_tax}')

    # Feet to inches.
    def converter_f_to_i():
        f = int(input('Enter feet : '))

        def feet_to_inches(feet):
            return feet * 12

        print(f'Number of inches in {f} feet = {feet_to_inches(f)}')

    # Math Test
    def math_test():
        value_a = random.randint(1, 500)
        value_b = random.randint(1, 500)
        print(f'  {value_a} \n'
              f'+ {value_b}')
        answer = int(input('Enter answer: '))
        correct_answer = value_a + value_b

        if correct_answer == answer:
            print(f'Congratulations your answer correct : {answer}')
        else:
            print(f'Your answer is wrong, correct answer: {correct_answer}')

    # Maximum of two values.
    def max_of_two_val():
        value_a = int(input('Enter first value: '))
        value_b = int(input('Enter second value: '))

        def my_max(a, b):
            return a if a > b else b

        print('Greater number is:', my_max(value_a, value_b))

    # Drop Height.
    def drop_height():

        def falling_distance(seconds):
            return 1 / 2 * 9.8 * seconds ** 2

        for sec in range(1, 11):
            print(f'{falling_distance(sec):.1f} m/s²')

    # Kinetic energy.
    def user_input_for_kinetic_en():
        mass = int(input('Enter body weight in kg: '))
        speed = int(input('Enter body speed in sc: '))

        def kinetic_energy(m, s):
            return 1 / 2 * m * s ** 2

        print('Kinetic energy is:', kinetic_energy(mass, speed))

    # Average score and its level.
    def average_score_level():
        avg_grade = []

        def calc_average(grade_list):
            return sum(grade_list) / len(grade_list)

        def determine_grade(av_grade):
            if av_grade >= 90:
                return 'A'
            if 80 <= av_grade <= 89:
                return 'B'
            if 70 <= av_grade <= 79:
                return 'C'
            if 60 <= av_grade <= 69:
                return 'D'
            else:
                return 'F'

        for i in range(5):
            grade = int(input(f'Enter your {i+1} exam grade: '))
            avg_grade.append(grade)

        average_grade = calc_average(avg_grade)

        print(f'Your grade is: {determine_grade(average_grade)}')

    # Counter even odd numbers
    def counter_even_odd_num():
        odd_num = 0
        even_num = 0

        for _ in range(100):
            num = random.randint(1, 100)
            if num % 2 == 0:
                even_num += 1
            else:
                odd_num += 1

        print(f'Even numbers: {even_num}')
        print(f'Odd numbers: {odd_num}')

    # Prime numbers.
    def is_prime(number):
        count = 0
        for num in range(1, number+1):
            if number % num == 0:
                count += 1
            if count == 3:
                return False
        if number > 1:
            return True

    def prime_numbers():
        usr_num = int(input('Enter your number: '))

        if is_prime(usr_num):
            print(f'Your number {usr_num} is prime number.')
        else:
            print(f'Your number {usr_num} is composite number.')

    # List of prime numbers.
    def list_of_prime_num():
        count = 0
        for num in range(1, 100):
            if is_prime(num):
                count += 1

        print('Number of prime numbers', count)

    # Future value.
    def future_value():
        balance = float(input('Enter current account balance: '))
        interest_rate = float(input('Enter you monthly interest rate: ')) / 100
        num_months = int(input('Enter number of months: '))

        def contribution_calc(b, i, m):
            return b * (1 + i) ** m

        print(f'After {num_months} months, your account will have the amount of '
              f'{contribution_calc(balance, interest_rate, num_months):.3f}')

    # Random number guessing game.
    def rand_num_guess_game():
        print('Guess a number from 1 to 100.')

        def new_guess_num():
            return random.randint(1, 100)

        def main_game():
            attempts = 0
            done = False

            while done is False:
                usr_input = int(input('Enter value: '))

                if guess_num > usr_input:
                    print('To little!')
                    attempts += 1
                elif guess_num < usr_input:
                    print('To much!')
                    attempts += 1
                else:
                    print(f'Congratulations you guessed the number {guess_num}.')
                    print(f'Number of attempts {attempts}.')
                    done = True

        guess_num = new_guess_num()
        main_game()
        new_game_done = False

        while new_game_done is False:
            new_game = input('Would you like to start a new game? y / n: ')
            if new_game.lower() == 'n':
                break

            guess_num = new_guess_num()
            main_game()

    # Game: rock, paper, scissors.
    def rock_paper_scissors():
        def choice(number):
            if number == 1:
                return 'Rock'
            if number == 2:
                return 'Scissors'
            if number == 3:
                return 'Paper'

        def main_loop():
            rnd_num = random.randint(1, 3)
            usr_num = int(input('Enter number: 1 for Rock. 2 for Scissors. 3 for Paper. '))

            pc_choice = choice(rnd_num)
            usr_choice = choice(usr_num)

            print(f'Computer chose: {pc_choice}.')

            if usr_choice == 'Rock' and pc_choice == 'Scissors':
                print('Congratulations You win!')
            elif usr_choice == 'Scissors' and pc_choice == 'Rock':
                print('Computer win!')
            if usr_choice == 'Scissors' and pc_choice == 'Paper':
                print('Congratulations You win!')
            elif usr_choice == 'Paper' and pc_choice == 'Scissors':
                print('Computer win!')
            if usr_choice == 'Paper' and pc_choice == 'Rock':
                print('Congratulations You win!')
            elif usr_choice == 'Rock' and pc_choice == 'Paper':
                print('Computer win!')
            if usr_choice == pc_choice:
                print('Draw. Starting over.')
                main_loop()

        main_loop()

    # Turtle graphics: triangle draw function.
    def triangle(x, y, fill_color):
        delta = turtle.Pen()

        delta.fillcolor(fill_color)
        delta.begin_fill()
        delta.setx(x)
        delta.fd(100-20)
        delta.sety(y)
        turtle.done()

    # Turtle graphics: modular snowman.
    def modular_snowman():
        def draw_base():
            circle_1 = turtle.Pen()
            circle_1.hideturtle()
            circle_1.circle(50)

        def draw_mid_section():
            circle_2 = turtle.Pen()
            circle_2.hideturtle()
            circle_2.up()
            circle_2.goto(0, 100)
            circle_2.down()
            circle_2.circle(30)

        def draw_arms():
            arm_1, arm_2 = turtle.Pen(), turtle.Pen()
            arm_1.hideturtle()
            arm_2.hideturtle()

            arm_1.up()
            arm_2.up()
            arm_1.goto(-30, 130)
            arm_2.goto(30, 130)
            arm_1.down()
            arm_2.down()

            arm_1.rt(25)
            arm_1.bk(15)
            arm_1.rt(55)
            arm_1.bk(15)
            arm_1.rt(35)
            arm_1.bk(5)
            arm_1.fd(5)
            arm_1.lt(45)
            arm_1.bk(5)

            arm_2.lt(35)
            arm_2.fd(30)
            arm_2.lt(55)
            arm_2.fd(5)
            arm_2.bk(5)
            arm_2.rt(85)
            arm_2.fd(5)

        def draw_head():
            head = turtle.Pen()
            head.hideturtle()
            head.up()
            head.goto(0, 160)

            head.down()
            head.circle(20)
            head.up()

            # eyes.
            head.goto(-10, 180)
            head.down()
            head.circle(3)
            head.up()
            head.fd(20)
            head.down()
            head.circle(3)

            # mouth.
            head.up()
            head.goto(-10, 170)
            head.down()
            head.fd(20)

        def draw_hat():
            hat = turtle.Pen()
            hat.hideturtle()
            hat.up()
            hat.goto(-15, 200)
            hat.down()
            hat.fillcolor('black')
            hat.begin_fill()
            for _ in range(4):
                hat.fd(30)
                hat.lt(90)
            hat.end_fill()
            hat.fd(45)
            hat.begin_fill()
            for _ in range(2):
                hat.rt(90)
                hat.fd(7)
                hat.rt(90)
                hat.fd(60)
            hat.end_fill()

        draw_base()
        draw_mid_section()
        draw_arms()
        draw_head()
        draw_hat()

    # Turtle graphics: rectangular pattern.
    def rect_pattern():
        width, height = int(input('Enter width: ')), int(input('Enter height: '))

        def draw_pattern(w, h):
            pass

    # Turtle graphics: chess board.
    def chess_board:
        pass

    # Turtle graphics: city silhouette.
    def city_silhoette():
        pass

if __name__ == '__main__':
    main()
