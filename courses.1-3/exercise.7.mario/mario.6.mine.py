def main(num):
    print_block(num)

def print_block(a):
    for _ in range(a):
        print('# ' * a)

size = int(input("Size? "))
main(size)
