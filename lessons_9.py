"""Programs"""

# Program 9.2.
# This program uses dictionary for storage,
# the names and birthdays of friends.

# Global Constants.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


# main function.
def main():
    # Create empty dictionary.
    birthdays = {}

    # Initialize variable for user choice.
    choice = 0

    while choice != QUIT:
        # Get the menu item selected by the user.
        choice = get_menu_choice()

        # Handle the selected option
        if choice == LOOK_UP:
            look_up(birthdays)
        elif choice == ADD:
            add(birthdays)
        elif choice == CHANGE:
            change(birthdays)
        elif choice == DELETE:
            delete(birthdays)


def get_menu_choice():
    print()
    print('Friends and their birthdays.')
    print('----------------------------')
    print('1. Find birthday.')
    print('2. Add new birthday.')
    print('3. Change birthday.')
    print('4. Delete birthday.')
    print('5. Exit.')
    print()

    # Get the item selected by the user.
    choice = int(input('Enter selected item: '))

    # Check the selected item for validity.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter selected item: '))

    return choice


def look_up(birthdays):
    """Function look_up find name in birthdays dictionary."""

    # Get name.
    name = input('Enter name: ')

    # Find name in dict.
    print(birthdays.get(name, 'Not found'))


def add(birthdays):
    """The add function adds a new entry to the birthdays' dictionary."""
    # Get name and birthday.
    name = input('Enter name: ')
    b_day = input('Enter birthday: ')

    # If name does not exist.
    if name not in birthdays:
        birthdays[name] = b_day
    else:
        print('This entry already exists')


def change(birthdays):
    """The change function changes an existing entry in the birthday dictionary."""
    # Get name.
    name = input('Enter name: ')

    if name in birthdays:
        # Get new birthday.
        b_day = input('Enter new birthday')

        birthdays[name] = b_day
    else:
        print('This name was not found.')


def delete(birthdays):
    """Delete function removes an entry in the birthdays' dictionary."""
    # Get name.
    name = input('Enter name: ')

    # if the name is found, then delete this entry.
    if name in birthdays:
        del birthdays[name]
    else:
        print('This name was not found.')


# if __name__ == '__main__':
#     main()

numbers = [1, 2, 3, 4]

squares = {item: item**2 for item in numbers}


populations = {'New-York': 8398748, 'Los-Angeles': 3990456,
               'Chicago': 2705994, 'Houston': 2325502,
               'Phoenix': 1660272, 'Philadelphia': 1584138}

largest = {key: value for key, value in populations.items() if value > 2000000}


# 9.14.
names = ['Cris', 'Katty', 'Joanna', 'Kurt']

names_dict = {key: len(key) for key in names}


# 9.15.
phonebook = {'Cris': '919-555-1111', 'Katty': '828-555-2222',
             'Joanna': '704-555-3333', 'Kurt': '919-555-3333'}

new_phonebook = {key: value for key, value in phonebook.items() if value[:3] == '919'}


# 9.3 Sets.
def sets():
    baseball = {'Jodi', 'Carmen', 'Aida', 'Alicia'}
    basketball = {'Eva', 'Carmen', 'Alicia', 'Sara'}

    print('These students are on the baseball team:')
    for name in baseball:
        print(name)

    print()

    print('These students are on the basketball team:')
    for name in basketball:
        print(name)

    print()

    # Intersection.
    print('These students play both baseball and basketball:')
    for name in baseball.intersection(basketball):
        print(name)

    print()

    # Union.
    print('These students play one or both sports games:')
    for name in baseball.union(basketball):
        print(name)

    print()

    # The difference between baseball and basketball.
    print('These students play baseball but not basketball:')
    for name in baseball.difference(basketball):
        print(name)

    print()

    # The difference between basketball and baseball.
    print('These students play basketball but not baseball:')
    for name in basketball.difference(baseball):
        print(name)

    print()

    # Symmetric difference.
    print('These students play one of the sports but not both:')
    for name in baseball.symmetric_difference(baseball):
        print(name)

    print()


set_1 = {1, 2, 3, 4, 5, 6, 7}

set_2 = {item**2 for item in set_1}
print(set_1, set_2)
some_set = {'a', 'b', 'c', 'd'}
some_set_1 = {'b', 'c', 'd', 'g'}
print(some_set_1.difference(some_set))
