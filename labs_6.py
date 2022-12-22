"""Algorithmic simulator"""
import os


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

