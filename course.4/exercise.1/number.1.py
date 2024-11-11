try:
    x = int(input("Number? "))
    print(f"Your nunmber is {x}.")
except ValueError:
    print("Your chosen... something... is not a number.")