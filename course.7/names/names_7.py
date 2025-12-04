with open("names.txt", "r") as file:
    lines = file.readlines()

#rstrip strips the end line symbil at the end of a line in lines for correct syntax
for line in lines:
    print(f"Hello, {line.rstrip()}!")


