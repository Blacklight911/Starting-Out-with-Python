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
# Kilometer converter.
# def to_miles(kilometres):
#     return kilometres * 0.6214
#
# number = float(input('Enter the distance in kilometers'))
# to_miles(number)

# Modernization of the sales tax calculation program.
# def main ():
#     buy_value = int(input('Enter purchase amount: '))
#
#     def federal_tax(value):
#         return value * 0.05
#
#     def regional_tax(value):
#         return value * 0.025
#
#     def all_sum(value, regional_val, federal_val):
#         return value + regional_val + federal_val
#
#     fed_tax = federal_tax(buy_value)
#     reg_tax = regional_tax(buy_value)
#     print('Purchase amount:', buy_value)
#     print('The federal tax amounted to:', fed_tax)
#     print('The regional tax amounted to:', reg_tax)
#     print('The amount of the purchase including tax was:', all_sum(buy_value, fed_tax, reg_tax))

# What is the cost of insurance.
# # def main():
#     cost = float(input('Enter building cost: '))
#     number_percent = float(input('Enter number of percent(recommend minimum is 80%): ')) / 100
#
#     def insured_sum(value, percent=0.8):
#         return value * percent
#
#     print(f'At building cost {cost}, sum insured will be: {insured_sum(cost, number_percent)}')

# Car expenses.
# def main():
#     car_costs = ['loan payments', 'insurance', 'petrol', 'machine oil', 'tires', 'maintenance']
#     expenses = []
#     for value in range(len(car_costs)):
#         value_expenses = float(input(f'Enter the amount of expenses for the car {car_costs[value]}: '))
#         expenses.append(value_expenses)
#
#     print(f'Your monthly expenses were: {sum(expenses)}')
#     print(f'Your annual expenses were: {sum(expenses) * 12}')

# Real estate tax.
# def main():
#     TAX = 72
#     actual_cost = float(input('Enter actual cost: '))
#     def assessed_cost(cost):
#         return cost * 0.6
#
#     def tax_calculation(tax_cost, act_cost, asses_cost):
#         return tax_cost * asses_cost / act_cost
#
#
#
#     print('Assessed value:', assessed_cost(actual_cost))
#     print('Property tax:', tax_calculation(TAX, actual_cost, assessed_cost(actual_cost)))

# Calories from fats and carbohydrates.
def main():
    pass

if __name__ == '__main__':
    main()
