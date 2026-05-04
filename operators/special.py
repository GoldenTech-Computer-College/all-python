# Identity operators are used to compare the memory locations of two objects. They check whether two variables refer to the same object in memory.
a = [1, 2, 3]
b = a  # b is assigned the same list as a, so they refer to the same object in memory
c = [1, 2, 3]  # c is assigned a new list with the same content as a, but it is a different object in memory

# IS operator - it returns True if both operands refer to the same **object** in memory. E.g a is b => this will return True if the value of a and the value of b refer to the same object in memory.
# IS NOT operator - it returns True if both operands do not refer to the same **object** in memory. E.g a is not c => this will return True if the value of a and the value of c do not refer to the same object in memory.
print(a is b)  # Output: True
print(a is c)  # Output: False
print(a is not c)  # Output: True
print(b is c)  # Output: False

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

# Membership operators - used to test whether a value/variable is present(is found) in a sequence (like a string, list, tuple, set, or dictionary) or not.
# IN operator - it returns True if a value is found in the sequence. E.g 'a' in 'banana' => this will return True because the character 'a' is found in the string 'banana'.
# NOT IN operator - it returns True if a value is not found in the sequence. E.g 'x' not in 'banana' => this will return True because the character 'x' is not found in the string 'banana'.
message = "Hello, welcome to Python programming!"
print('welcome' in message)  # Output: True
print('Python' in message)   # Output: True
print('Java' in message)     # Output: False

dict1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print('name' in dict1)      # Output: True
print('Alice' in dict1)     # Output: False
print('Alice' not in dict1) # Output: True