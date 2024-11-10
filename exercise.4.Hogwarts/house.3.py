

name = input("Hello! What is your name? \n My name is ").strip()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("You are not allowed to be here. You have LGBTQ.")
