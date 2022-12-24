def main():
    def product_search():
        prod_nums = ['V475', 'F987', 'Q143', 'R688']

        search = input('Enter part number: ')

        if search not in prod_nums:
            print(f'{search} in list')
        else:
            print(f'{search} not in list')

    def list_append():
        name_list = []

        again = 'y'

        while again == 'y':
            name = input('Enter name: ')

            name_list.append(name)

            print('Would you like to add another name?')
            again = input('y = yes, else = no: ')
            print()

        print('Names that have been entered')
        for name in name_list:
            print(name)

    def index_list():
        food = ['Pizza', 'Burgers', 'Chips']

        print('Here are the food list values:')
        print(food)

        item = input('What value should be changed? ')

        try:
            item_index = food.index(item)
            new_item = input('Enter new value: ')
            food[item_index] = new_item

            print('Here new list')
            print(food)
        except ValueError:
            print(f'This value({item}) in list')

    def insert_list():
        names = ['James', 'Katrin', 'Bill']

        print('List before insert')
        print(names)

        names.insert(0, 'Jo')

        print('List after insert')
        print(names)


if __name__ == '__main__':
    main()