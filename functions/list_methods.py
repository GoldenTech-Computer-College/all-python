# append()
a = [1, 2, 3, 4, 5, 6]
a.append(7)
print(a)

empty_list = []
empty_list.append("apple")
print(empty_list)

# extend() 
a = [1, 2, 3, 4]
b = [5, 6, 7]
a.extend(b)
print(a)

# index()
a = [1, 2, 3, 3, 4, 5]
print(a.index(3))

# insert()
a = [1, 2, 3, 5]
a.insert(3, 4)
print(a)

# pop()
a = [1, 2, 3, 4, 5, 6]
a.pop()
print(a)

# remove()
a = [1, 2, 3, 3, 4, 5, 6]
a.remove(3)
print(a)

# reverse()
a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a) # Output: [6, 5, 4, 3, 2, 1]

# len() - returns the length(how many items) of the items in the list
a = [1, 2, 3, 4, 4, 5, 6, 6]
print(len(a))

# count() - returns the number of times a specified element appears in the list
a = [1, 2, 3, 4, 4, 5, 6, 6]
print(a.count(6))