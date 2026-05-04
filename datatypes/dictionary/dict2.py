another = {
    "name": "John Doe",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "zip": "12345",
        "co-ordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    }
}
print(another["address"]["city"])
print(another["address"]["co-ordinates"]["latitude"])