from sys import argv , exit

if len(argv) < 2:
    exit("Not enough arguments!")


for arg in argv:
    print("Hello! My name is" , arg)


