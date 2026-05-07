example_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "experience": {
        "job1": "Software Engineer",
        "job2": "Data Scientist"
    }
}

# Dictionary Methods
# 1. get() method
# hobbies = example_dict['hobbis']
hobbies = example_dict.get('hobbies')
# print(hobbies)

# job2 = example_dict['experience']['job2']
job2 = example_dict.get('experience').get('job2')
# print(job2)

travelling = example_dict.get('hobbies')[1]
# print(travelling)

# 2. items() method
items = example_dict.items()
# print(items)

# 3. keys() method
keys = example_dict.keys()
# print(keys)

# 4. values() method
values = example_dict.values()
# print(values)

# 5. pop() method
popped = example_dict.pop("citi", "City is not found")
print(popped)