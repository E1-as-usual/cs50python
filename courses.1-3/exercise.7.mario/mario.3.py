def main(a):
    print_column(a)

def print_column(height):
    for _ in range(height):
        print("#")

num = int(input("Insert number please: "))
main(num)
