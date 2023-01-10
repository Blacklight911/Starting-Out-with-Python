"""Algorithmic simulator"""
# my_set = {1, 2, 3, 4}
# nomy_set = {4, 3, 5, 8}
# my_set |= nomy_set  # |= is union update method.
# my_set -= nomy_set  # -= is difference with assignment in first set.
# my_set &= nomy_set  # &= Intersection with assignment in first set.
#
#
# print(my_set | nomy_set)  # Union set.
# print(my_set)  # |= update method.
#
# print(my_set - nomy_set)  # Difference set.
# print(my_set & nomy_set)  # Intersection set. &
# print(my_set ^ nomy_set)  # Symmetric difference set. ^

# 1.
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 2.
my_dict_2 = {}

# 3.
dct = {}
if 'James' in dct:
    print(dct['James'])
else:
    print('There is no such key.')

# 4.
if 'Jim' in dct:
    del dct['Jim']
else:
    print('There is no such key.')

# 5.
my_set = set(range(10, 41, 10))


# 6.
set_1 = {1, 2, 3, 4}
set_2 = {5, 6, 7, 8}
set_3 = set_1 | set_2


# 7.
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 5, 6}
set_4 = set_1 & set_2
print(set_4)
"""Programing exercises"""
