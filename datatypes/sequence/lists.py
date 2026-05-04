empty_list = []
# print(empty_list)

numbers = [1, 2, 3, 4, 5]
# print(numbers)

fruits = ['apple', 'banana', 'cherry']
# print(fruits)

mixed_list = [1, "hello", 3.14, True, False, None]
# print(mixed_list)

nested_list = [1, 2, [3, 4], 5]
# print(nested_list)

# accessing list elements using indexing
numbers = [10, 20, 30, 40, 50]
print(numbers[0]) 
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

mixed_nested_list = [1, "hello", 4, [5, 6, "world"], True, [7, 8, [9, 10]]]
print(mixed_nested_list[0])
print(mixed_nested_list[3][0])
print(mixed_nested_list[3][2])

# changing list elements using indexing
numbers = [10, 20, 30, 40, 50]
numbers[0] = 100
print(numbers)
numbers[-1] = 500
print(numbers)

# list slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
