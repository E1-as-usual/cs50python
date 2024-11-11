try:
    x = int(input("Number? "))
except ValueError:
    print("Your chosen... something... is not a number.")
else:
    print(f"Your number is {x}.")
