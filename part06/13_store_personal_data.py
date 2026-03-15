# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "w") as f:
        name, age, height = person
        f.write(f"{name};{age};{height}")