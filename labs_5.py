"""Algorithmic simulator"""
import random


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
        pass

    max_of_two_val()
if __name__ == '__main__':
    main()
