#!/usr/bin/python3
list_copy = __import__('list_copy').list_copy

my_list = [1, 2, 3]
print(my_list)

new_list = list_copy(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
