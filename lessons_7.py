import random
import matplotlib.pyplot as plt


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

    def random_numbers():
        ROWS = 3
        COLS = 4

        values = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                values[r][c] = random.randint(1, 100)

        return values

    # 7.23.
    def creating_nested_list(value):
        return [[value for col in range(4)] for row in range(3)]

    # 7.24.
    def print_random_lists(array):
        for row in array:
            for column in row:
                print(column, end=' ')
            print()

    # 7.27. - 7.28.
    def list_to_tuple_and_tuple_to_list():
        my_list = [1, 2, 3, 4, 5]
        my_tuple = tuple(my_list)
        change_to_list = list(my_tuple)

    def line_graph1():
        plt.title('My line graph')
        plt.xlabel('This is the x-axis')
        plt.ylabel('This is the y-axis')

        plt.grid(True)

        x_coords = [0, 1, 2, 3, 4]
        y_coords = [0, 3, 1, 5, 2]

        plt.plot(x_coords, y_coords)
        plt.show()

    def line_graph3():
        x_coords = [0, 1, 2, 3, 4]
        y_coords = [0, 3, 1, 5, 2]

        plt.plot(x_coords, y_coords)

        plt.title('Sample data')

        plt.xlabel('This is the x-axis')
        plt.ylabel('This is the y-axis')

        plt.xlim(xmin=-1, xmax=10)
        plt.ylim(ymin=-1, ymax=6)

        plt.grid(True)
        plt.show()

    def line_graph4():
        x_coords = [0, 1, 2, 3, 4]
        y_coords = [0, 3, 1, 5, 2]

        plt.plot(x_coords, y_coords)

        plt.title('Sales by year')

        plt.xlabel('Year')
        plt.ylabel('Volume of sales')

        plt.xticks([0, 1, 2, 3, 4], ['2016', '2016', '2018', '2019', '2020'])
        plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

        plt.grid(True)

        plt.show()

    def line_graph5():
        x_coords = [0, 1, 2, 3, 4]
        y_coords = [0, 3, 1, 5, 2]

        plt.plot(x_coords, y_coords, marker='o')
        plt.title('Sales by year')

        plt.xlabel('Year')
        plt.ylabel('Sales volume')

        plt.xticks([0, 1, 2, 3, 4], ['2016', '2017', '2018', '2019', '2020'])
        plt.yticks([0, 1, 2, 3, 4, 5], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

        plt.grid(True)
        plt.show()

    def bar_chart1():
        left_edges = [0, 10, 20, 30, 40]

        heights = [100, 200, 300, 400, 500]

        plt.bar(left_edges, heights)

        plt.show()

    def bar_chart2():
        left_edges = [0, 10, 20, 30, 40]

        heights = [100, 200, 300, 400, 500]

        bar_width = 5

        plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))
        plt.show()

    def bar_chart3():
        left_edges = [0, 10, 20, 30, 40]

        heights = [100, 200, 300, 400, 500]

        bar_width = 10

        plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))
        plt.title('Sales by year')

        plt.xlabel('Year')
        plt.ylabel('Sales volume')

        plt.xticks([5, 15, 25, 35, 45], ['2016', '2017', '2018', '2019', '2020'])
        plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

        plt.show()

    def pie_chart1():
        values = [20, 60, 80, 40]

        plt.pie(values)

        plt.show()

    def pie_chart2():
        sales = [100, 400, 300, 600]

        slice_labels = ['I quarter', 'II quarter', 'III quarter', 'IV quarter']

        plt.pie(sales, labels=slice_labels, colors=('r', 'g', 'b', 'm', 'k'))
        plt.title('sales by quarters')
        plt.show()

if __name__ == '__main__':
    main()
