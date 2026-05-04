# How to create a function in Python
def function_name(parameters):
    # Function body
    # Code to be executed
    pass
# function_name(parameters="")  # Calling the function
# print('Not inside the function')

def add():
    print(10 + 30)
add()  # Calling the function

# Types of functions in Python
# 1. Built-in functions - predefined functions that are available in Python. E.g print(), len(), type(), etc. They are always available for use without the need for importing any module.
print("Hello, World!")  # Using the built-in print() function
# 2. User-defined functions - functions that are defined by the user to perform specific tasks. E.g def function_name(parameters): ... They are created by the user to perform specific tasks that are not covered by built-in functions.
def send_greeting():
    print("Hello! How are you?")
send_greeting()  # Calling the user-defined function
# 3. Anonymous functions (lambda functions) - functions that are defined without a name and are typically used for short, simple operations. E.g lambda parameters: expression. They are often used in situations where a small function is needed for a short period of time, such as in sorting or filtering operations.
add = lambda x, y: x + y  # Defining a lambda function to add two numbers
result = add(5, 3)  # Calling the lambda function
print(result)  # Output: 8
# 4. Recursive functions - functions that call themselves in order to solve a problem. E.g def function_name(parameters): ... They are used to solve problems that can be broken down into smaller, similar subproblems, such as calculating the factorial of a number or traversing a tree structure.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120