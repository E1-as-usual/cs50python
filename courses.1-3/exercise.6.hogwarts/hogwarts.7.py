students = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel terrier"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None }
]

print("Name, House, Patronus")
for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")

