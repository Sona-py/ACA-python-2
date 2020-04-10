x = [[1, 2], [1, 2, 3], [1, 2]]
def remove_values_from_list(the_list, val):
    for i in range(the_list.count(val)):
        the_list.remove(val)

remove_values_from_list(x, [1,2])

print(x)