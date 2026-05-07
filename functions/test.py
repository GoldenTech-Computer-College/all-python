#  Write a function append_item(item, my_list=[]) that takes 4 items and returns the list of items.
# Create a function format_currency(amount, currency="KES") that returns something like "KES 1,000.00"
# The amount is assumed to be in USD and the conversion rate is 1 USD = Ksh 130

def append_item(item, my_list=[]):
    # my_list += [item]
    my_list.append(item)
    return my_list
print(append_item("apple"))  # Output: ['apple']
print(append_item("banana"))  # Output: ['apple', 'banana']
print(append_item("cherry"))  # Output: ['apple', 'banana', 'cherry']
print(append_item("date"))    # Output: ['apple', 'banana', 'cherry', 'date']

def format_currency(amount, currency="KES"):
    converted_amount = amount * 130
    return f"{currency} {converted_amount}"
print(format_currency(100))  # Output: KES 13,000.00

def different_currencies(amount, currency, rate):
    converted_amount = amount * rate
    return f"{currency} {converted_amount}"
print(different_currencies(100, "EUR", 0.85))  # Output
