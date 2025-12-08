students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student ={"name": name, "house": house}
        students.append(student)

  
for student in sorted(students, key=lambda student: student["name"]):   #Folosim Lambda, o functie "no-name", care este chemat\a si folosit\a doar \in acest context, careia ii dam direct obiectul student, si valoarea, fara return
    print(f"{student['name']} is in {student['house']}.")

