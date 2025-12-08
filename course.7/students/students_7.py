import csv

name = input("What is your name?")
houme = input("Where is your home?")

with open("students.csv") as file:
    writer = csv.writer(file)
    writer.writerow([name], [home])

