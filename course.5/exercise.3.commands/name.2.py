from sys import argv

try:
    print("Hello! My name is" , argv[1])
except IndexError:
    print("Too few arguments, sorry, pal...")
    
