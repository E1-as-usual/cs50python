from sys import argv , exit

if len(argv) < 2:
    exit("Not enough arguments!")
elif len(argv) > 2:
    exit("Too many arguments")



print("Hello! My name is" , argv[1])

