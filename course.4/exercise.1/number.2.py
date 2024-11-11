try:
    x = int(input("Number? "))
except ValueError:
    print("Your chosen... something... is not a number.")


print(f"Your nunmber is {x}.")