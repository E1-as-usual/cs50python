def main(a):
    print_column(a)

def print_column(a):
    for _ in range(a):
        print("#")

num = int(input("Insert number please: "))
main(num)
