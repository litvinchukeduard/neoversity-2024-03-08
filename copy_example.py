from copy import copy, deepcopy

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lst_deep = deepcopy(lst)
lst_copy = copy(lst)

lst[0][1] = 10

# print(lst_copy)
# print(lst)
# print(lst_deep)


simple_lst = [1, 2, 3, 4, 5]
simple_copy = copy(simple_lst)

simple_lst[3] = 9

# print(simple_lst)
# print(simple_copy)




