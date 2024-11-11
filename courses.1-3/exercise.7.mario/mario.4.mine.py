def main(a):
    print_row(a)

def print_row(length):
    print("?" * length , end = "")

num = int(input("Insert number please: "))
main(num)
