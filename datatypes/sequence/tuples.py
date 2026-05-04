empty_tuple = ()
print(empty_tuple)

numbers = (1, 2, 3, 4, 5)
print(numbers)

fruits = ('apple', 'banana', 'cherry')
print(fruits)

mixed_tuple = (1, 'hello', 3.14, True, False, None)
print(mixed_tuple)

nested_tuple = (1, 2, (3, 4), 5, 6, (True, False, ('Nested', 'Tuple')))
print(nested_tuple)

# accessing tuple elements using indexing
numbers = (10, 20, 30, 40, 50)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

# Immutability 
items = (1, 2, 3, 4, 5, 6)
# items[1] = 20 # This will raise a TypeError because tuples are immutable
print(items)

# tuple slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
