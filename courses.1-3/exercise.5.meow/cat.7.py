def main():
    number = get_number()
    meow(number)

def getnumber():
    while True:
        n = int(input("What is the number? "))
        if n > 0:
            return n 

def meow(x):
    for _ in range( x ):
        print("meow")
