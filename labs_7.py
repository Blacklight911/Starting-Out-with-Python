"""Algorithmic simulator"""
import random

# # 1.
# my_list = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
#
# # 2.
# names = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
# for name in names:
#     print(name)
#
# # 3.
# numbers1 = [random.randint(1, 100) for i in range(100)]
# numbers2 = numbers1
# print(numbers1, numbers2, sep='\n')
#
# # 5.
# def take_list_return_sum(array):
#     total = 0
#     for num in array:
#         total += num
#     return total
#
# # 6.
# names = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
# if 'Rubi' in names:
#     print('Hello, Rubi!')
# else:
#     print('Ruby is missing.')
#
# # 8.
# list1 = [40, 50, 60]
# list2 = [num * 2 for num in list1]
#
# # 9,
# list3 = [random.randint(50, 150) for i in range(10)]
# list4 = [item for item in list3 if item > 100]
#
# # 10.
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = [item for item in list_1 if item % 2 == 0]

# 11.
def create_array_list():
    my_list = [[int(input('Enter value: ')) for col in range(3)] for row in range(5)]
    print(my_list)

"""Programming exercises."""
# Total Sales.
def total_sales():
    total = []

    for day in range(7):
        day = int(input(f'Enter sales volume from {day+1}: '))
        total.append(day)

    print('Total: ', sum(total))

def lottery_number_generator():
    numbers_list = []

    for number in range(7):
        numbers_list.append(random.randint(0, 9))

    print(*numbers_list)

def rainfall_statistics():
    rainfall_stat = []
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec']

    for month in range(12):
        rainfall_stat.append(int(input(f'Enter the rainfall for {months[month]}: ')))

    print('Rainfall per year:', sum(rainfall_stat))
    print('Average rainfall per month:', sum(rainfall_stat) / len(rainfall_stat))
    print(f'Maximum rainfall was in {months[rainfall_stat.index(max(rainfall_stat))]}, {max(rainfall_stat)}')
    print(f'Minimum rainfall was in {months[rainfall_stat.index(min(rainfall_stat))]}, {min(rainfall_stat)}')

def number_analysis_program():
    nums = []

    for num in range(20):
        nums.append(int(input(f'Enter {num+1} number: ')))

    print('Min', min(nums))
    print('Max', max(nums))
    print('Sum', sum(nums))
    print('Avg', sum(nums) / len(nums))

def exp_account_number_validation_check():
    accounts = []

    with open('Data/charge_accounts.txt', 'r', encoding='utf-8') as file:
        for line in file:
            accounts.append(int(line))
        file.close()

    user_account = int(input('Enter number you account: '))

    if user_account in accounts:
        print('Number is valid')
    else:
        print('Number invalid')

def greater_than_the_number_n():
    num = int(input('Enter value: '))
    numbers = [random.randint(1, 100) for _ in range(10)]

    def greater_n(array, n):
        for number in array:
            if number > n:
                print(num, end=' ')

    greater_n(numbers, num)

def driving_license_exam():
    right_answers = []
    user_answers = []
    incorrect_answers = []
    correct = 0
    incorrect = 0


    with open('Data/student_solution.txt', 'r', encoding='utf-8') as file:
        for line in file:
            right_answers.append(line.rstrip('\n'))
        file.close()

    for question in range(20):
        user_input = input(f'Enter correct answer on {question+1} question'
                           '(A, B, C, D): ').upper()
        user_answers.append(user_input)

        if user_input == right_answers[question]:
            correct += 1
        else:
            incorrect += 1
            incorrect_answers.append(question+1)


    if correct >= 15:
        print('Congratulations you passed the exam!')
    else:
        print('Exam failed.')

    print(f'Total number of correct answers: {correct}')
    print(f'Total number of wrong answers: {incorrect}')
    print('Numbers of wong questions ', *incorrect_answers)

def name_search():
    girls_names = []
    boys_names = []
    DONE = False

    with open('Data/GirlNames.txt', 'r', encoding='utf-8') as girls_file:
        for line in girls_file:
            girls_names.append(line.rstrip('\n'))
        girls_file.close()

    with open('Data/BoyNames.txt', 'r', encoding='utf-8') as boys_file:
        for line in boys_file:
            boys_names.append(line.rstrip('\n'))
        boys_file.close()

    print('Welcome to name search program.')
    while DONE is False:
        choose = input('Enter gender(b - for boys, g - for girls: ').lower()
        name = input('Enter name: ')

        if choose == 'b' and name in boys_names:
            print(f'{name}, among the most popular.')
        elif choose == 'g' and name in girls_names:
            print(f'{name}, among the most popular.')
        else:
            print(f'{name}, not on the list.')

        cont = input('Do you want to find another name? y - for yes, or n to exit: ').lower()
        if cont == 'y':
            continue
        else:
            DONE = True

def population_data():
    data_pop = []
    start_year = 1950

    try:
        with open('Data/USPopulation.txt', 'r', encoding='utf-8') as file:
            for line in file:
                data_pop.append(int(line))
            file.close()

        print(f'Average annual population change: {sum(data_pop) / len(data_pop):.2f}')
        print('Year with the largest increase in population:', 1950 + data_pop.index(max(data_pop)))
        print('Year with least population increase:', 1950 + data_pop.index(min(data_pop)))



    except IOError:
        print('Error. File not exits.')
    except IndexError:
        print('Error. Index error.')

def world_series_champions():
    teams_champions = []
    win_count = 0

    try:
        with open('Data/WorldSeriesWinners.txt', 'r', encoding='utf-8') as file:
            for line in file:
                teams_champions.append(line.rstrip('\n'))
            file.close()

        user_input = input('Enter team name: ')

        if user_input not in teams_champions:
            print(f"Team {user_input}, Didn't win these years")
        else:
            for team in teams_champions:
                if user_input == team:
                    win_count += 1
            print(f'Team {user_input}, won {win_count} times, in')


    except IOError:
        print('Open Error. File not exits')
    except IndexError:
        print('Index Error index out of range.')
    except:
        print('An Error has occurred.')

def luo_shu_magic_square():

    my_list = [[4, 9, 2],
               [3, 5, 7],
               [8, 1, 6]]

    def is_magic(array):
        row_1 = sum(array[0])
        row_2 = sum(array[1])
        row_3 = sum(array[2])
        col_1 = array[0][0] + array[1][0] + array[2][0]
        col_2 = array[0][1] + array[1][1] + array[2][1]
        col_3 = array[0][2] + array[1][2] + array[2][2]
        diagonal_1 = array[0][0] + array[1][1] + array[2][2]
        diagonal_2 = array[0][2] + array[1][1] + array[2][0]

        if row_1 == 15 and row_2 == 15 and row_3 == 15 \
        and col_1 == 15 and col_2 == 15 and col_3 == 15 \
        and diagonal_1 == 15 and diagonal_2 == 15:
            return True
        else:
            return False

    if is_magic(my_list):
        print('Square is truly magical.')
    else:
        print('Square not magical.')

def generating_prime_number():
    pass

generating_prime_number()
