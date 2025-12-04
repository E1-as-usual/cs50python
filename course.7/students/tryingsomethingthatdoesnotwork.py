name = ()
house = ()
file = open("students.csv", "a")


def main():
    while name != "end":
        request()
        file.write(name)
        file.write(",")
        file.write(house)
        file.write("\r")
    file.close()
    exit()


def request():
    name = input("What is the student's name?(Please write 'end' to exit the program)")
    if name != "end":
        house = input("What is the student's house?")
        return house
    return name



if __name__ == "__main__":
    main()

