from sys import argv

if len(argv) < 2:
    print("Not enough arguments!")
elif len(argv) > 2:
    print("Too many arguments")
else:
    print("Hello! My name is" , argv[1])

