"""Lessons 6"""
import os


def main():
    def file_wrtie():
        # Open file.
        outfile = open('philosophers.txt', 'w')

        # Write the names of three philosophers to a file.
        outfile.write('John Locke\n')
        outfile.write('David Hume\n')
        outfile.write('Edmund Burke\n')

        # Close file.
        outfile.close()

    def file_read():
        # Open file.
        infile = open('philosophers.txt', 'r')

        # Read file.
        file_contents = infile.read()

        # Close file.
        infile.close()

        # Print data, in RAM.
        print(file_contents)

    def line_read():
        infile = open('philosophers.txt', 'r')

        line1 = infile.readline()
        line2 = infile.readline()
        line3 = infile.readline()

        infile.close()

        print(line1)
        print(line2)
        print(line3)

    def write_names():
        # Get three names.
        print('Enter your friends names.')
        name1 = input('Friend # 1: ')
        name2 = input('Friend # 2: ')
        name3 = input('Friend # 3: ')

        # Open file.
        my_file = open('friends.txt', 'w')

        # Write names in file.
        my_file.write(f'{name1}\n')
        my_file.write(f'{name2}\n')
        my_file.write(f'{name3}\n')

        # Close file.
        my_file.close()
        print('Names were written in friends.txt.')

    def strip_newline():
        # Open file with name philosophers.txt.
        infile = open('philosophers.txt', 'r')

        # Read three lines and Del \n from each string value.
        line1 = infile.readline().rstrip('\n')
        line2 = infile.readline().rstrip('\n')
        line3 = infile.readline().rstrip('\n')

        # Close file.
        infile.close()

        # Print data.
        print(line1)
        print(line2)
        print(line3)

    def appending_to_file():
        # Open file.
        my_file = open('friends.txt', 'a')

        # Write in file.
        my_file.write('Mat\n')
        my_file.write('Harry\n')
        my_file.write('Petter\n')

        # Close file.
        my_file.close()

    def write_numbers():
        # Open file.
        outfile = open('numbers.txt', 'w')

        # Get three numbers from the user.
        # And write them to a file.
        for _ in range(3):
            outfile.write(str(int(input('Enter number: '))) + '\n')

        outfile.close()
        print('Data recorded in numbers.txt')

    def read_numbers():
        # Open file.
        infile = open('numbers.txt', 'r')

        # Summ total nums.
        total = 0

        # Read three nums.
        for _ in range(3):
            num = int(infile.readline())
            total += num

        # Close file.
        infile.close()

        # Print nums
        print(f'Total sum: {total}')

    def write_sales():
        # Get number of days.
        num_days = int(input('For how many days'
                             ' You have sales? '))

        # Create and write file.
        # Get sum sales for each day.
        with open('sales.txt', 'w', encoding='utf-8') as sales_file:
            for count in range(1, num_days+1):
                # Get sales in a day
                sales = float(input(f'Enter daily sales № {count}: '))
                sales_file.write(f'{sales}\n')
            # Close file.
            sales_file.close()
            print('Data recorded in sales.txt.')

    def read_sales():
        with open('sales.txt', 'r', encoding='utf-8') as sales_file:
            line = sales_file.readline()
            while line != '':
                print(f'{float(line):.2f}')
                line = sales_file.readline()

            sales_file.close()

    def read_sales2():
        with open('sales.txt', 'r', encoding='utf-8') as sales_file:
            for line in sales_file:
                print(f'{float(line):.2f}')

            sales_file.close()

    def save_running_times():
        """
        This program saves a sequence of video clip
        lengths in the file video_times.txt
        """
        # Take value video clips in project.
        num_videos = int(input('How much video clips in project? '))

        with open('video_times.txt', 'w', encoding='utf-8') as video_file:
            # Get the duration of each video clip and write it to a file.
            for count in range(1, num_videos+1):
                video_file.write(f'{float(input(f"Video clip № {count}: "))}\n')
            video_file.close()
            print('Times are saved in video_times.txt')

    def read_running_times():
        """
        This program reads values from file
        video_times.txt and calculates their sum
        """
        total = 0.0
        count = 0

        with open('video_times.txt', 'r', encoding='utf-8') as video_file:
            for line in video_file:
                run_time = float(line)
                count += 1
                print(f'Video clip № {count}, : {run_time}')

                total += run_time
            video_file.close()
        print(f'The total duration is {total} seconds.')

    # 6.12.
    def write_program():
        with open('nums.txt', 'w', encoding='utf-8') as file:
            for line in range(1, 11):
                file.write(f'{line} \n')

            file.close()

    # 6.14.
    def read_data():
        with open('data.txt', 'r', encoding='utf-8') as file:
            line = file.readline()
            while line != '':
                print(line.rstrip())
                line = file.readline()

        file.close()

    # 6.15.
    def read_data_m():
        with open('data.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip())
            file.close()

    def save_emp_records():
        # Get the number of employee records to create.
        num_eps = int(input('How many records do you want to create?'))

        # Open file.
        with open('employees.txt', 'w', encoding='utf-8') as emp_file:
            # Get the details of each employee and record them.
            for count in range(1, num_eps+1):
                print(f'Enter details of employee № {count}')
                name = input('Enter name: ')
                id_num = input('Identification number: ')
                dept = input('Department: ')

                # Write data.
                emp_file.write(f'{name}\n')
                emp_file.write(f'{id_num}\n')
                emp_file.write(f'{dept}\n')

                # Empty str.
                print()

            # Close file.
            emp_file.close()
            print('Employee records are stored in employees.txt')

    def read_emp_records():
        with open('employees.txt', 'r', encoding='utf-8') as emp_file:
            name = emp_file.readline().rstrip('\n')
            while name != '':
                name = name.rstrip('\n')
                id_num = emp_file.readline().rstrip('\n')
                dept = emp_file.readline().rstrip('\n')

                print(f'Nane: {name}')
                print(f'ID: {id_num}')
                print(f'Dept: {dept}')
                print()

                name = emp_file.readline()

            emp_file.close()

    def add_coffee_record():
        another = 'y'

        with open('coffee.txt', 'a', encoding='utf-8') as coffee_file:
            while another == 'y':
                print('Enter next coffee mark.')
                descr = input('Description: ')
                qty = int(input('Quantity (in pounds): '))

                coffee_file.write(f'{descr}\n')
                coffee_file.write(f'{qty}\n')

                print('Would you like to add another entry ?')
                another = input('Y for yes, else n or no ').lower()

            coffee_file.close()
            print('Data add in coffee.txt.')

    def show_coffee_records():
        with open('coffee.txt', 'r', encoding='utf-8') as coffee_file:
            descr = coffee_file.readline()
            while descr != '':
                qty = float(coffee_file.readline())
                descr = descr.strip('\n')

                print(f'Description: {descr}')
                print(f'Quantity: {qty}')

                descr = coffee_file.readline()

            coffee_file.close()

    def search_coffee_records():
        found = False

        search = input('Enter the value you are looking for: ')

        with open('coffee.txt', 'r', encoding='utf-8') as coffee_file:
            descr = coffee_file.readline()

            while descr != '':
                qty = float(coffee_file.readline())

                descr = descr.rstrip('\n')

                if descr == search:
                    print(f'Description: {descr}')
                    print(f'Quantity: {qty}')
                    print()
                    found = True

                descr = coffee_file.readline()

            coffee_file.close()

            if not found:
                print('This value was not found in the file. ')

    def modify_coffee_records():
        found = False

        search = input('Enter search description: ')
        new_qty = int(input('Enter new quantity: '))

        with open('coffee.txt', 'r', encoding='utf-8') as coffee_file:
            with open('temp.txt', 'w') as temp_file:

                descr = coffee_file.readline()

                while descr != '':
                    qty = float(coffee_file.readline())
                    descr = descr.rstrip('\n')

                    if descr == search:
                        temp_file.write(f'{descr}\n')
                        temp_file.write(f'{new_qty}\n')

                        found = True
                    else:
                        temp_file.write(f'{descr}\n')
                        temp_file.write(f'{qty}\n')

                    descr = coffee_file.readline()

                coffee_file.close()
                temp_file.close()

                os.remove('coffee.txt')
                os.rename('temp.txt', 'coffee.txt')

                if found:
                    print('File updated.')
                else:
                    print('This value was not found in the file.')

    def delete_coffee_record():
        found = False

        search = input('Which brand do you want to remove? ')

        with open('coffee.txt', 'r', encoding='utf-8') as coffee_file:
            with open('temp.txt', 'w', encoding='utf-8') as temp_file:
                descr = coffee_file.readline()

                while descr != '':
                    qty = float(coffee_file.readline())

                    descr = descr.rstrip('\n')

                    if descr != search:
                        temp_file.write(f'{descr}\n')
                        temp_file.write(f'{qty}\n')
                    else:
                        found = True

                    descr = coffee_file.readline()

                coffee_file.close()
                temp_file.close()

                os.remove('coffee.txt')
                os.rename('temp.txt', 'coffee.txt')

                if found:
                    print('File updated.')
                else:
                    print('This value was not found in the file.')



# Call main function.
if __name__ == '__main__':
    main()
