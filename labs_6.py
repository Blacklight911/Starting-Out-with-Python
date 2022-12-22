"""Algorithmic simulator"""
import os
import random


# 1.
def my_func():
    with open('my_name.txt', 'w', encoding='utf-8') as my_file:
        my_file.write('Dmitrey')
        my_file.close()

# 2.
def print_my_name():
    with open('my_name.txt', 'r', encoding='utf-8') as my_file:
        print(my_file.readline())
        my_file.close()

# 3.
def nums_list():
    with open('number_list.txt', 'w', encoding='utf-8') as file:
        for num in range(1, 101):
            file.write(f'{num}\n')
        file.close()

# 4.
def open_nums_list():
    with open('number_list.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip('\n'))
        file.close()

# 5.
def sum_nums_list():
    with open('number_list.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += int(line)

        print(count)
        file.close()

# 6.
def read_nums_list():
    with open('number_list.txt', 'a', encoding='utf-8') as file:
        print('Job Done')
        file.close()

# 7
def del_an_entry():
    found = False
    search = input('Enter name student for search: ')

    with open('students.txt', 'r', encoding='utf-8') as file:
        with open('temp.txt', 'w', encoding='utf-8') as temp:
            name = file.readline()

            while name != '':
                grade = file.readline().rstrip('\n')
                name = name.rstrip('\n')

                if name != search:
                    temp.write(f'{name}\n')
                    temp.write(f'{grade}\n')
                else:
                    found = True

                name = file.readline()

            file.close()
            temp.close()

            os.remove('students.txt')
            os.rename('temp.txt', 'student.txt')

            if found:
                print('File update')
            else:
                print('No name in list')

# 8.
def change_an_entry():
    found = False
    search = input('Enter student name for search: ')
    new_grade = input('Enter new grade: ')

    with open('student.txt', 'r', encoding='utf-8') as file:
        with open('temp.txt', 'w', encoding='utf-8') as temp:
            name = file.readline()

            while name != '':
                grade = file.readline().rstrip('\n')
                name = name.rstrip('\n')

                if name == search:
                    temp.write(f'{name}\n')
                    temp.write(f'{new_grade}\n')

                    found = True
                else:
                    temp.write(f'{name}\n')
                    temp.write(f'{grade}\n')

                name = file.readline()

            file.close()
            temp.close()

            os.remove('student.txt')
            os.rename('temp.txt', 'student.txt')

            if found:
                print('File update')
            else:
                print('No name in list')

"""Programming exercises."""
# Output file to screen.
def output_file_to_screen():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(line.rstrip('\n'))
        file.close()

# Displaying the top of the file.
def display_top_of_file():
    filename = input("Input file name: ").lower() + '.txt'

    with open(filename, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            print(line.rstrip('\n'))
            count += 1
            if count == 5:
                break

    file.close()

# Line numbers.
def line_numbers():
    filename = input("Input file name: ").lower() + '.txt'

    with open(filename, 'r', encoding='utf-8') as file:
        for count, line in enumerate(file):
            print(f'{count+1}: {line.rstrip()}')
        file.close()

# Value counter.
def value_counter():
    with open('names.txt', 'r', encoding='utf-8') as file:
        count = 0
        for _ in file:
            count += 1
        print('Names in list:',count)
        file.close()

# Sum of numbers.
def sum_of_numbers():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        total = 0
        for line in file:
            total += int(line)
        print('Total sum:', total)
        file.close()

# Average of numbers.
def average_of_numbers():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        total = 0
        count = 0
        for line in file:
            count += 1
            total += int(line)
        print('Average:', total/count)
        file.close()

# Program for writing a file with random numbers.
def rand_number_writer():
    value = int(input('Enter the number of random numbers to write to the file: '))

    with open('random_numbers.txt', 'w', encoding='utf-8') as file:
        for line in range(value):
            file.write(f'{str(random.randint(1, 500))}\n')
        file.close()

# Random number file reader.
def rand_number_reader():
    with open('random_numbers.txt', 'r', encoding='utf-8') as file:
        count = 0
        total = 0
        for line in file:
            count += 1
            total += int(line)

        print(f'Total sum numbers: {total}')
        print(f'Numbers count: {count}')
    file.close()

# Exception Handling.
def exception_handling():
    with open('numbers.txt', 'r', encoding='utf-8') as file:
        total = 0
        count = 0
        try:
            for line in file:
                count += 1
                try:
                    total += int(line)
                except ValueError:
                    print('Error reading number. Number is string not number')
            print('Average:', total/count)
        except IOError:
            print('Error file not exits')
        file.close()

# Points in golf.
def golf_points():

    def write_points():
        with open('golf.txt', 'w', encoding='utf-8') as file:
            number_players = int(input('Enter number players: '))

            for _ in range(number_players):
                player_name = input('Enter player name: ')
                player_points = int(input(f'Enter {player_name} points: '))
                file.write(f'{player_name}\n')
                file.write(f'{player_points}\n')
            file.close()

    def read_points():
        with open('golf.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip('\n'))
            file.close()

    write_points()
    read_points()

# Personal web page generator.
def web_page_generator():
    with open('personal_site.html', 'w', encoding='utf-8') as file:
        user_name = input('Enter your name: ')
        describe = input('Describe yourself: ')
        file.write(f'<html>\n'
                   f'<head>\n'
                   f'</head>\n'
                   f'<body>\n'
                   f' <center>\n'
                   f'    <h1>{user_name}</h1>\n'
                   f' </center>\n'
                   f' <hr />\n'
                   f' {describe}\n'
                   f' <hr />\n'
                   f'</body>\n'
                   f'</html>\n')
        file.close()

# Average number of steps.
def average_num_of_steps():
    with open('steps.txt', 'r', encoding='utf-8') as file:
        count = 0
        month_steps = 0
        months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        str_months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sen', 'Okt', 'Nov', 'Dec')
        average_steps = []
        step = 0

        line = file.readline().rstrip('\n')
        while line != '':
            count += 1
            month_steps += int(line)
            line = file.readline().rstrip('\n')

            if step <= len(months) and count == months[step]:
                average_steps.append(month_steps)
                count = 0
                month_steps = 0
                step += 1

        file.close()
    for i, m in enumerate(months):
        print(f'Average for {str_months[i]} is {average_steps[i] / m:.2f}.')

average_num_of_steps()