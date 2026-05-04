sample_data = {
    "name": "Alice",
    "age": 30,
    "location": {
        "country": "Wonderland",
        "city": "Heart City",
        "coordinates": {
            "latitude": 52.5163, 
            "longitude": 13.3777
        }
    },
    "skills": [
        {"name": "Python", "level": "advanced"},
        {"name": "Machine Learning", "level": "intermediate"},
        {"name": "Data Analysis", "level": "advanced"}
    ],
    "experience": [
        {"company": "TechCorp", "role": "Data Scientist", "years": 3},
        {"company": "InnoLab", "role": "ML Engineer", "years": 2}
    ]
}
def get_experience(dict):
    name = dict["name"]
    first_company = dict["experience"][0]["company"]
    years = dict["experience"][0]["years"]
    print(f"{name} worked with {first_company} for {years} years.")
# get_experience(sample_data)

def get_skills(dict):
    name = dict["name"]
    skills = dict["skills"]
    level1 = skills[0]["name"]
    level2 = skills[1]["name"]
    level3 = skills[2]["name"]
    return f"{name} is skilled in {level1}, {level2} and {level3}"
print(get_skills(sample_data))
# Alice is skilled in Python, Machine Learning and Data Analysis