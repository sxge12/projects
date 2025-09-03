    # For this question you will define a Python function that processes dictionaries, and devise a
    # testing plan.
    # (a) Define a Python function add_items_from_second(first_dict,
    # second_dict) that takes two parameters, both dictionaries.
    # Both dictionaries map string keys to values. We are particularly interested in cases where
    # both dictionaries map equal keys to a list value. Your function will make changes to the
    # values in first_dict only for keys that appear and are mapped to list values in both
    # dictionaries.
    # If a key appears in both first_dict and second_dict and is mapped to a list in both,
    # then your function should change the value list in first_dict so that it also contains
    # all items in second_dict, but where any duplicate values appear only once. You may
    # assume that neither list contains duplicates before your function executes.
    # For example, after the execution of:
    # dict_1 = {'a':[1], 'b':[2], 'c':['apple'], 'e': 2, 'f':[4]}
    # dict_2 = {'a':[3], 'c':['apple'], 'd':[13], 'e':[2], 'f':'banana'}
    # add_items_from_second(dict_1, dict_2)
    # the variable dict_1 should have the value {'a':[1, 3], 'b':[2],
    # 'c':['apple'], 'e': 2, 'f':[4]}

def add_items_from_second(first_dict, second_dict):
i











dict_1 = {'a': [1], 'b': [2], 'c': ['apple'], 'e': 2, 'f': [4]}
dict_2 = {'a':[3], 'c':['apple'], 'd':[13], 'e':[2], 'f':'banana'}