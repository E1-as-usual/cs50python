def main():
    num = get_int()
    print(f"Your number is {num}.")

def get_int():
    while True:
        try:
            return int(input("Number? "))
        except ValueError:
            print("Your chosen... something... is not a number.")
main()
