def calculate_area_of_circle(diameter):
    radius = diameter / 2
    area = 3.142 * (radius ** 2)
    return f"The area of a circle with diameter {diameter} is: {area}"
print(calculate_area_of_circle(21))
