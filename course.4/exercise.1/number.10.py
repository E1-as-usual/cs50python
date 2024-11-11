def main():
    num = get_int("Number? ")
    print(f"Your number is {num}.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()
