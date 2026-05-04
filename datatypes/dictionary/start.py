empty = {}
print(empty)

my_dict = {"brand": "Toyota", "model": "Camry", "year": 2020}
print(my_dict)

bigger = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "traveling", "cooking"],
    "education": {
        "degree": "Bachelor's",
        "major": "Computer Science",
        "university": "XYZ University"
    }
}
print(bigger)
print(bigger["city"])
print(bigger['education']['degree'])
print(bigger['hobbies'][1])