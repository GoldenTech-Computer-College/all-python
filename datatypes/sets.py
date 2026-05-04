# empty dictionary
items = {}
empty_set = set()
print(type(items))
print(type(empty_set))

# set of unique items
items = {1, 2, 3, 4, 5}
print(type(items))

# set of unique items
fruits = set(['apple', 'banana', 'banana', 'cherry'])
print(fruits)

# set of unique items
fruits = {'apple', 'banana', 'cherry'}
print(fruits)

# set of unique items
mixed_set = {1, 'hello', 3.14, True, False, None}
print(mixed_set)

# set with tuples
nested_set = {1, 2, (3, 4), 5, 6, (True, False, ('Nested', 'Set'))}
print(nested_set)

items = {1, 2, 3, 3, 3, 4, 4, 5}
print(items)