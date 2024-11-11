def main(num):
    print_block(num)

def print_block(a):
    for i in range(a):
        for j in range(a):
            print("# " , end = "")
        print()


size = int(input("Size? "))
main(size)
