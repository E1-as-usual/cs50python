
def get_int():
    while True:
        try:
            x = int(input("Number? "))
        except ValueError:
            print("Your chosen... something... is not a number.")
        else:
            break
    return x

num = get_int()
print(f"Your number is {num}.")

