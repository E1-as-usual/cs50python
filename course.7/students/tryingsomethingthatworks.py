import sys


def main():
    while True:
        name = input("What is the student's name? (Type 'exit' to exit)").strip()
        
        if not name:
            print("name cannot be empty")
            continue

        if name.lower() == "exit":
            exit_program()
        
        while True:
            house = input("What is the student's house?").strip()
            if not house:
                print("House cannot be empty")
                continue
            else:
                break
        write_info(name, house)



def exit_program():
    print("exiting")
    sys.exit()    

def write_info(x , y):
    with open("students.csv", "a") as file:
        file.write(f"{x},{y}\n")
    print("added to .csv file")

    
if __name__ == "__main__":
    main()



