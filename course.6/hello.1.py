def main():
    name = input("What is your name?")
    hello(name)

def hello(to = "world"):
    print("Hello,", to)

if __name__ == "__main__":
    main()

