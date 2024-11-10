
def main():
    name = input("What is your name? \n My name is ").strip()

    if name == "Harry":
        Gryffindor()
    elif  name == "Hermione":
        Gryffindor()
    elif name == "Ron":
        Gryffindor()
    elif name == "Draco":
        Slytherin()
    else:
        Gandalf()

def Gryffindor():
    print("You've been assigned to Gryffindor")

def Slytherin():
    print("You've been assigned to Slytherin")

def Gandalf():
    print("YOU SHALL NOT PASS!")
    print("YOU DO NOT BELONG HERE!")

main()
