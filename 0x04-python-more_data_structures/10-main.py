#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))
my_dict = {'John': 12}
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))
my_dict = {}
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))
my_dict = None
best_key = best_score(my_dict)
print("Best score: {}".format(best_key))
