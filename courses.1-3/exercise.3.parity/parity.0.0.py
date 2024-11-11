'''Aceasta este cea mai simpla versiune a acesui cod. Pentru o versiune mai complexa, verificati urmatoarele versiuni.'''

#Pentru inceput scriem programul general ca pe o functie "main"
def main():
    x = int(input("Please insert your desired number: X = "))
    if is_even(x):
        print(f"Your chosen number, {x}, is even.")
    else:
        print(f"Your chosen number, {x}, is odd.")

#Definim functia is_even, care se ocupa de verificarea propriu zisa a paritatii
def is_even(n):
    return n % 2 == 0

#O data ce toate functiile sunt definite, rulam functia main
main()