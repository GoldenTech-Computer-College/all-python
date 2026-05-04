# They act on operands as if they were strings of binary digits. They operate bit by bit hence the name bitwise.
a = 5  # In binary: 0101
b = 3  # In binary: 0011
c = 0  # In binary: 0000

# Bitwise AND(&) - it returns 1 only if both bits are 1. E.g a & b => this will return 1 if only the value of a and the value of b are equal to 1.
print(a & b)  # Output: 1 (In binary: 0001)
print(a & c)  # Output: 0 (In binary: 0000)

# Bitwise OR(|) - it returns 1 if at least one of the bits is 1. E.g a | b => this will return 1 if either the value of a or the value of b is equal to 1.
print(a | b)  # Output: 7 (In binary: 0111)
print(a | c)  # Output: 5 (In binary: 0101)
print(b | c)  # Output: 3 (In binary: 0011)

print(True | True)
print(True | False)
print(False | False)