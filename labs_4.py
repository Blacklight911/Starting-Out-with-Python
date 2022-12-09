# # Algorithmic simulator.
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
#
#
# x += 1
# x *= 2
# x /= 10
# x -= 100
#
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
#             done  = True
#         else:
#             print('Error, enter valid value')
#     except ValueError:
#         print('Error, enter valid value')
#
# # Programming exercises.
# # Errors collector.
# done = False
# amount = 0
# end_of_day = 1
# while done is False:
#     print('Day: ', end_of_day)
#     errors = int(input('Enter number of errors per day: '))
#     amount += errors
#     if end_of_day == 5:
#         done = True
#     day = input('Day end? y or n: ')
#     if day == 'y':
#         end_of_day += 1
#
# print('total errors:', amount)
#
# # Calories burned.
# calories_per_min = 4,2
#
# for i in range(10, 31, 5):
#     print('Calories burned per', i, 'minutes:', i * 4.2)
#
# # Budget analysis.
# done = False
# dollars_per_month = int(input('Enter budget for a month: '))
# sum_dollars = 0
#
# while done is False:
#     costs = int(input('Enter the expense of funds: '))
#     sum_dollars += costs
#     end_count = input('End counting? y - yes, n - no: ')
#     if end_count.lower() == 'y':
#         done = True
#
# print('Expenses were $', dollars_per_month - sum_dollars)

# Distance traveled.

