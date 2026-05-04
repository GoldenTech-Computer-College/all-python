# Arrays of bytes representing Unicode characters. A character is a string of length one. Strings can be created using single quotes, double quotes, or even triple quotes:

s = "Welcome to the world of Python programming!"
# print(s)

s2 = 'This is a single quote string.'
# print(s2)

s3 = '''This is a multi-line string.
It can span multiple lines.'''
# print(s3)

s4 = """This is another multi-line string.
It can also span multiple lines."""
# print(s4)

# String breaks using breakers and escaping characters
single_quotes = 'This is a string with a single quote: \'Hello!\''
# print(single_quotes)

double_quotes = "This is a string with double quotes: \"Hello!\""
# print(double_quotes)

single_quotes_in_double = "This string contains a single quote: 'Hello!'"
# print(single_quotes_in_double)

# Breakers
new_string = "This is a string that \n\nbreaks into a new line."
# print(new_string)

tabbed_string = "This string contains a tab character:\t\tHello!"
# print(tabbed_string)

# string concatenation using +
name = "Thomas"
sms = "Hello, " + name + "! Welcome to Python programming."
# print(sms)

first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
# print(full_name)

# string concatenation using f-strings
student = "John"
greeting = "Goodmorning"
# print(greeting + ", " + student + "! Welcome to Python programming.")
print(f"{greeting}, {student}! \nWelcome to Python programming.")

name = "John Doe"
age = 18
print(f"My name is {name} and I am {age + 2} years old.")

# indexing
sentence = "Python programming is fun!"
print(sentence[0]) #P
print(sentence[1]) #y
print(sentence[2]) #t
print(sentence[3]) #h
print(sentence[4]) #o
print(sentence[5]) #n
print(sentence[6]) #

print(sentence[-1])
